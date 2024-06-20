import hvac
import os
from prefect import get_run_logger

from kube_watch.enums.providers import Providers

logger = get_run_logger()

def login(url, app_role_id, secret_id, path):
    """
    Login to Vault, using an existing token if available, or via AppRole otherwise.
    
    Parameters:
        url (str): Vault server URL.
        app_role_id (str): AppRole ID.
        secret_id (str): AppRole Secret ID.
        path (str): Path where the AppRole is enabled.

    Returns:
        dict: Dictionary containing the initialized vault_client.
    """
    vault_client = hvac.Client(url=url)
    
    # Attempt to use an existing token from environment variables
    vault_token = os.getenv('VAULT_TOKEN', None)
    if vault_token:
        vault_client.token = vault_token
        # Verify if the current token is still valid
        try:
            if vault_client.is_authenticated():
                logger.info("Authenticated with existing token.")
                return vault_client
        except hvac.exceptions.InvalidRequest as e:
            logger.warning("Failed to authenticate with the existing token:", str(e))

    # If token is not valid or not present, authenticate with AppRole
    try:
        vault_client.auth.approle.login(
            role_id=app_role_id, 
            secret_id=secret_id, 
            mount_point=f'approle/{path}'
        )
        
        # Store the new token in environment variables for subsequent use
        os.environ['VAULT_TOKEN'] = vault_client.token
        logger.info("Authenticated with new token and stored in environment variable.")

        return vault_client
    except hvac.exceptions.InvalidRequest as e:
        logger.error("Authentication failed with provided secret_id:", str(e))
        raise RuntimeError("Authentication failed: unable to log in with the provided credentials.") from e



def get_secret(vault_client, secret_path, vault_mount_point):
    """
    Retrieve a secret from Vault
    """
    res = vault_client.secrets.kv.v2.read_secret_version(
        path=secret_path,
        mount_point=vault_mount_point,
        raise_on_deleted_version=True
    )
    return res.get('data', {}).get('data')


def update_secret(vault_client, secret_path, secret_data, vault_mount_point):
    """
    Update or create a secret in Vault at the specified path.
    
    Args:
        vault_client: The authenticated Vault client instance.
        secret_path (str): The path where the secret will be stored or updated in Vault.
        secret_data (dict): The secret data to store as a dictionary.
        vault_mount_point (str): The mount point for the KV store.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Writing the secret data to Vault at the specified path
        vault_client.secrets.kv.v2.create_or_update_secret(
            path=secret_path,
            secret=secret_data,
            mount_point=vault_mount_point
        )
        print("Secret updated successfully.")
        return True
    except Exception as e:
        print(f"Failed to update secret: {e}")
        return False

def generate_provider_creds(vault_client, provider, backend_path, role_name):
        """
        Generate credentials for a specified provider 
        """
        if provider == Providers.AWS:
            backend_path = backend_path
            role_name = role_name
            creds_path = f"{backend_path}/creds/{role_name}"
            return vault_client.read(creds_path)

        raise ValueError("Unknown provider")



def generate_new_secret_id(vault_client, role_name, vault_path, env_var_name):
    new_secret_response = vault_client.auth.approle.generate_secret_id(
        role_name=role_name,
        mount_point=f'approle/{vault_path}'
    )

    return { env_var_name : new_secret_response['data']['secret_id'] }