import json, requests
from csv_pm_llm_parsing import constants
from typing import Optional, Dict, Any
import traceback


def openai_inquiry(prompt: str, openai_api_url: Optional[str] = None, openai_api_key: Optional[str] = None,
                   openai_model: Optional[str] = None) -> str:
    """
    Sends the prompt to the OpenAI's APIs, obtaining the response

    Parameters
    ------------------
    prompt
        Prompt
    openai_api_url
        OpenAI API url
    openai_api_key
        OpenAI API key
    openai_model
        OpenAI model

    Returns
    -----------------
    response
        Response from the APIs
    """
    if openai_api_url is None:
        openai_api_url = constants.OPENAI_API_URL

    if openai_api_key is None:
        openai_api_key = constants.OPENAI_API_KEY

    if openai_model is None:
        openai_model = constants.OPENAI_MODEL

    if openai_api_key is None or not openai_api_key:
        raise Exception(
            "Please provide the 'openai_api_key' parameter to the method or set the OPENAI_API_KEY environment variable!")

    if openai_model is None or not openai_model:
        raise Exception(
            "Please provide the 'openai_model' parameter to the method or set the OPENAI_MODEL environment variable!")

    if openai_api_url.endswith("/"):
        openai_api_url = openai_api_url[:-1]

    complete_url = openai_api_url + "/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": openai_model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(complete_url, headers=headers, json=payload).json()

    if "error" in response:
        # raise an exception when the request fails, with the provided message
        raise Exception(response["error"]["message"])

    return response["choices"][0]["message"]["content"]


def get_json(response: str) -> Dict[str, Any]:
    """
    Gets the last JSON dictionary contained in the response from the APIs

    Parameters
    ---------------
    response
        Response from the APIs

    Returns
    ---------------
    json_dict
        Last JSON dict
    """
    try:
        json_str = "{" + response.split("{")[-1].split("}")[0].strip() + "}"
        return json.loads(json_str)
    except:
        traceback.print_exc()
        return None
