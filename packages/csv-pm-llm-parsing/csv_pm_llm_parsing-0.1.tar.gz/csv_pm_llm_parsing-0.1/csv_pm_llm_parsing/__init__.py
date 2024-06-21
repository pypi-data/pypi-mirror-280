import pandas as pd
from csv_pm_llm_parsing import constants, meta
from typing import Optional, Union, Dict
import sys, traceback


def detect_timest_format(df: pd.DataFrame, timest_column: str = "time:timestamp", max_head_n: int = 10,
                         max_retry: int = constants.MAX_RETRY, openai_api_url: Optional[str] = None,
                         openai_api_key: Optional[str] = None,
                         openai_model: Optional[str] = None, return_timest_format: bool = False, debug: bool = False) -> Union[
    pd.DataFrame, Dict[str, str]]:
    """
    Automatically detects the format of the timestamp in the specified column using LLMs.
    The Pandas dataframe's column is then parsed using the given format.

    Parameters
    ---------------
    df
        Pandas dataframe
    timest_column
        Column to which we aim to apply the automatic timestamp format detection
    max_head_n
        Number of top values that should be provided to the LLM
    max_retry
        Maximum number of retries upon failure
    openai_api_url
        API URL (like https://api.openai.com/v1 or http://127.0.0.1:11434/v1 )
    openai_api_key
        API key
    openai_model
        OpenAI model
    return_timest_format
        (bool) Returns the timestamp format (instead of the transformed dataframe)
    debug
        (bool) Prints additional debug information

    Returns
    ----------------
    df
        Pandas dataframe (with the timestamp column parsed)
    """
    from csv_pm_llm_parsing import timest_parser
    return timest_parser.detect_timest_format(df, timest_column=timest_column, max_head_n=max_head_n,
                                              max_retry=max_retry, openai_api_url=openai_api_url,
                                              openai_api_key=openai_api_key, openai_model=openai_model,
                                              return_timest_format=return_timest_format, debug=debug)


def detect_sep_and_quote(file_path: str, input_encoding: str = "utf-8", read_bytes: int = 2048,
                         max_retry: int = constants.MAX_RETRY, openai_api_url: Optional[str] = None,
                         openai_api_key: Optional[str] = None,
                         openai_model: Optional[str] = None, return_detected_sep: bool = False, debug: bool = False) -> Union[
    pd.DataFrame, Dict[str, str]]:
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
    from csv_pm_llm_parsing import sep_detection
    return sep_detection.detect_sep_and_load(file_path, input_encoding=input_encoding, read_bytes=read_bytes,
                                             max_retry=max_retry, openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model,
                                             return_detected_sep=return_detected_sep, debug=debug)


def detect_caseid_activity_timestamp(df: pd.DataFrame, max_retry: int = constants.MAX_RETRY,
                                     openai_api_url: Optional[str] = None,
                                     openai_api_key: Optional[str] = None,
                                     openai_model: Optional[str] = None, return_suggestions: bool = False, debug: bool = False) -> Union[
    pd.DataFrame, Dict[str, str]]:
    """
    Detects automatically the columns to use as case identifier, activity, and timestamp in the provided dataframe.

    Parameters
    -----------------
    df
        Pandas dataframe
    max_retry
        Maximum number of retries upon failure
    openai_api_url
        API URL (like https://api.openai.com/v1 or http://127.0.0.1:11434/v1 )
    openai_api_key
        API key
    openai_model
        OpenAI model
    return_suggestions
        (bool) Return the suggestion (dictionary) instead of the dataframe
    debug
        (bool) Prints additional debug information

    Returns
    ----------------
    df
        Pandas dataframe with standard column names (i.e., in pm4py, 'case:concept:name' for the case ID, 'concept:name' for the activity, and 'time:timestamp' for the timestamp).
    """
    from csv_pm_llm_parsing import pm_columns_detection
    return pm_columns_detection.detect_caseid_activity_timestamp(df, max_retry=max_retry, openai_api_url=openai_api_url,
                                                                 openai_api_key=openai_api_key,
                                                                 openai_model=openai_model,
                                                                 return_suggestions=return_suggestions,
                                                                 debug=debug)


def __parse_bytes(file_path: str, n_bytes: int) -> str:
    """
    Parses the specific number of bytes from the file to retrieve the encoding
    (using the 'chardet' package)

    Parameters
    --------------
    file_path
        Path to the CSV file
    n_bytes
        Number of bytes to decide the encoding

    Returns
    --------------
    encoding
        Encoding
    """
    import chardet

    F = open(file_path, "rb")
    byte_content = F.read(n_bytes)
    F.close()

    result = chardet.detect(byte_content)
    encoding = result['encoding']

    F = open(file_path, "r", encoding=encoding)
    F.read()
    F.close()

    return encoding


def full_parse_csv_for_pm(file_path: str, openai_api_url: Optional[str] = None,
                          openai_api_key: Optional[str] = None,
                          openai_model: Optional[str] = None, debug: bool = False) -> pd.DataFrame:
    """
    Starting from the specified path, reads the CSV in a process-mining-ready format.

    Parameters
    ---------------
    file_path
        Path to the CSV file
    openai_api_url
        API URL (like https://api.openai.com/v1 or http://127.0.0.1:11434/v1 )
    openai_api_key
        API key
    openai_model
        OpenAI model
    debug
        (bool) Prints additional debug information

    Returns
    ---------------
    dataframe
        Pandas dataframe
    """
    try:
        encoding = __parse_bytes(file_path, 2048)
    except:
        encoding = __parse_bytes(file_path, sys.maxsize)

    if debug:
        print(encoding)

    for i in range(constants.MAX_RETRY):
        try:
            dataframe = detect_sep_and_quote(file_path, input_encoding=encoding, openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model, debug=debug, max_retry=1)

            dataframe = detect_caseid_activity_timestamp(dataframe, openai_api_url=openai_api_url,
                                                         openai_api_key=openai_api_key, openai_model=openai_model, debug=debug, max_retry=1)
            dataframe = dataframe.dropna(subset=["case:concept:name", "concept:name", "time:timestamp"])
            dataframe["case:concept:name"] = dataframe["case:concept:name"].astype(str)
            dataframe["concept:name"] = dataframe["concept:name"].astype(str)

            dataframe = detect_timest_format(dataframe, "time:timestamp", openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model, debug=debug, max_retry=2)

            dataframe["@@index"] = dataframe.index
            dataframe.sort_values(["case:concept:name", "time:timestamp", "@@index"])

            break
        except:
            traceback.print_exc()

    return dataframe
