import os
from typing import Any, Dict

import requests


class WecoAI:
    def __init__(self, api_key: str = None) -> None:
        """Initializes the WecoAI client with the provided API key and base URL.

        Parameters
        ----------
        api_key : str
            The API key used for authentication. If not provided, the client will attempt to read it from the environment variable - WECO_API_KEY.
        base_url : str
            The base URL of the WecoAI API.

        Raises
        ------
        ValueError
            If the API key is not provided to the client, is not set as an environment variable or is not a string.
        """
        # Manage the API key
        if api_key is None or not isinstance(api_key, str):
            try:
                api_key = os.environ["WECO_API_KEY"]
            except KeyError:
                raise ValueError(
                    "WECO_API_KEY must be passed to client or set as an environment variable"
                )
        self.api_key = api_key

        # base URL
        self.base_url = "https://function-builder.vercel.app"

    def _headers(self) -> Dict[str, str]:
        """Constructs the headers for the API requests.

        Returns
        -------
        dict
            A dictionary containing the headers.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Makes a POST request to the specified endpoint with the provided data.

        Parameters
        ----------
        endpoint : str
            The API endpoint to which the request will be made.
        data : dict
            The data to be sent in the request body.

        Returns
        -------
        dict
            The response from the server as a dictionary.

        Raises
        ------
        requests.HTTPError
            If the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def build(self, task_description: str) -> tuple[str, str]:
        """Builds a specialized function given a task description.

        Parameters
        ----------
        task_description : str
            A description of the task for which the function is being built.

        Returns
        -------
        tuple[str, str]
            A tuple containing the name and description of the function.
        """
        endpoint = "build"
        data = {"request": task_description}
        response = self._post(endpoint, data)
        return response["name"], response["description"]

    def query(self, fn_name: str, fn_input: str) -> Dict[str, Any]:
        """Queries a function with the given function ID and input.

        Parameters
        ----------
        fn_name : str
            The name of the function to query.
        fn_input : str
            The input to the function.

        Returns
        -------
        dict
            A dictionary containing the output of the function, the number of input tokens, the number of output tokens,
            and the latency in milliseconds.
        """

        endpoint = "query"
        data = {
            "name": fn_name,
            "user_message": fn_input,
        }
        response = self._post(endpoint, data)
        result = {
            "output": response["response"],
            "in_tokens": response["num_input_tokens"],
            "out_tokens": response["num_output_tokens"],
            "latency_ms": response["latency_ms"],
        }
        return result
