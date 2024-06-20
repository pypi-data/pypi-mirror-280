import subprocess
import os
from prefect import get_run_logger
logger = get_run_logger()

def run_standalone_script(package_name, package_run, package_exec):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # script_path = os.path.join(script_dir, package_name.replace('.', os.sep))
    target_dir = os.path.join(script_dir, os.pardir, os.pardir, *package_name.split('.'))

    # Change the current working directory to the script directory
    full_command = f"{package_run} {os.path.join(target_dir, package_exec)}"

    # Execute the command
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            logger.info(result.stdout)
        if result.stderr:
            logger.error(result.stderr)
        # logger.info(f"Output: {result.stdout}")
        result.check_returncode()
    except subprocess.CalledProcessError as e:
        # All logs should have already been handled above, now just raise an exception
        logger.error("The subprocess encountered an error: %s", e)
        raise Exception("Subprocess failed with exit code {}".format(e.returncode))