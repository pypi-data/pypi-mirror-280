from csv_pm_llm_parsing import constants, util
import pandas as pd
from typing import Optional, Union, Dict
import traceback
import time


def detect_sep_and_load(file_path: str, input_encoding: str = "utf-8", read_bytes: int = 2048,
                        max_retry: int = constants.MAX_RETRY, openai_api_url: Optional[str] = None,
                        openai_api_key: Optional[str] = None,
                        openai_model: Optional[str] = None, return_detected_sep: bool = False, debug: bool = False) -> Union[pd.DataFrame, Dict[str, str]]:
    """
    Detects the separator and quotechar in the provided file using LLMs.

    Parameters
    ----------------
    file_path
        Path to the file
    input_encoding
        Encoding of the file (default: utf-8)
    read_bytes
        Number of bytes that should be initially considered
    max_retry
        Maximum number of retries upon failure
    openai_api_url
        API URL (like https://api.openai.com/v1 or http://127.0.0.1:11434/v1 )
    openai_api_key
        API key
    openai_model
        OpenAI model
    return_detected_sep
        (bool) Returns the detected separator and quotechar, instead of the Pandas dataframe
    debug
        (bool) Prints additional debug information

    Returns
    ----------------
    df
        Pandas dataframe
    """
    F = open(file_path, 'r', encoding=input_encoding)
    first_characters = F.read(read_bytes)
    F.close()

    prompt = "Given the following contents of a CSV file:\n\n"
    prompt += first_characters
    prompt += "\n\n"
    prompt += "Could you identify the separator and quote characters for the Pandas read_csv method?\n"
    prompt += "Please produce a JSON including two keys, 'sep' and 'quotechar'."
    dataframe = None
    for i in range(max_retry):
        try:
            format = util.get_json(util.openai_inquiry(prompt.encode('utf-8', errors='ignore').decode('utf-8'),
                                                       openai_api_url=openai_api_url, openai_api_key=openai_api_key,
                                                       openai_model=openai_model))
            format['sep']
            format['quotechar']

            if debug:
                print(format)
            if return_detected_sep:
                return format

            dataframe = pd.read_csv(file_path, encoding=input_encoding, sep=format['sep'],
                                    quotechar=format['quotechar'])
            break
        except Exception as e:
            traceback.print_exc()
            prompt += "\n\nI am getting the following error: " + str(e)
            time.sleep(constants.SLEEP_TIME)

    if dataframe is None:
        raise Exception("failed detection of separator and quotechar.")

    return dataframe
