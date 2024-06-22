from typing import Any, Dict, Optional

from .client import WecoAI


def build(task_description: str, api_key: str = None) -> tuple[str, str]:
    """Builds a specialized function given a task description.

    Parameters
    ----------
    task_description : str
        A description of the task for which the function is being built.
    api_key : str
        The API key for the WecoAI service. If not provided, the API key must be set using the environment variable - WECO_API_KEY.

    Returns
    -------
    tuple[str, str]
        A tuple containing the name and description of the function.
    """
    client = WecoAI(api_key=api_key)
    response = client.build(task_description=task_description)
    return response


def query(fn_name: str, fn_input: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Queries a function with the given function ID and input.

    Parameters
    ----------
    fn_name : str
        The name of the function to query.
    fn_input : str
        The input to the function.
    api_key : str
        The API key for the WecoAI service. If not provided, the API key must be set using the environment variable - WECO_API_KEY.

    Returns
    -------
    dict
        A dictionary containing the output of the function, the number of input tokens, the number of output tokens,
        and the latency in milliseconds.
    """
    client = WecoAI(api_key=api_key)
    response = client.query(fn_name=fn_name, fn_input=fn_input)
    return response
