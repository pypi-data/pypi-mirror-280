from prefect import task
import functools
import asyncio
from prefect.task_runners import ConcurrentTaskRunner, SequentialTaskRunner
# from prefect_dask.task_runners import DaskTaskRunner
from typing import Dict, List
import yaml
import importlib
import os
from kube_watch.models.workflow import WorkflowConfig, BatchFlowConfig, Task
from kube_watch.enums.workflow import ParameterType, TaskRunners, TaskInputsType
from kube_watch.modules.logic.merge import merge_logical_list

def load_workflow_config(yaml_file) -> WorkflowConfig:
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return WorkflowConfig(**data['workflow'])


def load_batch_config(yaml_file) -> BatchFlowConfig:
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return BatchFlowConfig(**data['batchFlows'])



# def execute_task(func, *args, name="default_task_name", **kwargs):
#     @task(name=name)
#     def func_task():
#         return func(*args, **kwargs)
#     return func_task


def func_task(name="default_task_name", task_input_type: TaskInputsType = TaskInputsType.ARG):
    if task_input_type == TaskInputsType.ARG:
        @task(name=name)
        def execute_task(func, *args, **kwargs):
            return func(*args, **kwargs)
        return execute_task
    if task_input_type == TaskInputsType.DICT:
        @task(name=name)
        def execute_task(func, dict_inp):
            return func(dict_inp)
        return execute_task
    raise ValueError(f'Unknow Task Input Type. It should either be {TaskInputsType.ARG} or {TaskInputsType.DICT} but {task_input_type} is provided.')


# @task
# def execute_task(func, *args, **kwargs):
#     return func(*args, **kwargs)



def get_task_function(module_name, task_name):
    # module = importlib.import_module(f"sparrow_watch.modules.{module_name}")
    # klass = getattr(module, class_name)
    # return getattr(klass, task_name)
    """
    Fetch a function directly from a specified module.
    
    Args:
        module_name (str): The name of the module to import the function from. e.g. providers.aws
        task_name (str): The name of the function to fetch from the module.
        
    Returns:
        function: The function object fetched from the module.
    """
    module = importlib.import_module(f"kube_watch.modules.{module_name}")
    return getattr(module, task_name)



def resolve_parameter_value(param):
    if param.type == ParameterType.FROM_ENV:
        return os.getenv(param.value, '')  # Default to empty string if env var is not set
    return param.value

def prepare_task_inputs(parameters):
    return {param.name: resolve_parameter_value(param) for param in parameters}


def prepare_task_inputs_from_dep(task_data: Task, task_inputs: Dict, tasks):
    for dep in task_data.dependency:
        par_task   = tasks[dep.taskName]
        par_res    = par_task.result()
        if dep.inputParamName != None:
            task_inputs.update({dep.inputParamName: par_res})

    return task_inputs


def resolve_conditional(task_data: Task, tasks):
    lst_bools = []
    for task_name in task_data.conditional.tasks:
        if task_name not in tasks:
            return False
        
        par_task   = tasks[task_name]
        lst_bools.append(par_task.result())
    return merge_logical_list(lst_bools, task_data.conditional.operation)
    



def submit_task(task_name, task_data, task_inputs, func):
    execute_task = func_task(name=task_name, task_input_type=task_data.inputsArgType)
    if task_data.inputsArgType == TaskInputsType.ARG:
        return execute_task.submit(func, **task_inputs)
    if task_data.inputsArgType == TaskInputsType.DICT:
        return execute_task.submit(func, dict_inp=task_inputs)
    raise ValueError("Unknown Input Arg Type.")



def resolve_runner(runner):
    if runner == TaskRunners.CONCURRENT:
        return ConcurrentTaskRunner
    if runner == TaskRunners.SEQUENTIAL:
        return SequentialTaskRunner
    if runner == TaskRunners.DASK:
        raise ValueError("Dask Not Implemented")
        # return DaskTaskRunner
    if runner == TaskRunners.RAY:
        raise ValueError("Ray Not Implemented")
        # return RayTaskRunner
    raise ValueError("Invalid task runner type")