import time
import random
    
def generate_number():
    return 42

def print_number(number, dummy_param, env_var_name):
    print(f"The generated number is: {number} and the dummy_value is: {dummy_param}")
    return number, dummy_param, env_var_name

def delay(seconds):
    time.sleep(seconds)


def random_boolean():
    return random.choice([True, False])

def merge_bools(inp_dict):
    list_bools = [v for k,v in inp_dict.items()]
    return any(list_bools)

def print_result(task_name, result):
    print(f'=========== {task_name} RESULT =================')
    print(result)
