import logging
from enum import Enum
from os import path

import yaml

CONFIG = path.join(path.dirname(path.abspath(__file__)), "../config/download_config.yaml")
logger = logging.getLogger(__name__)


def get_url(key: str) -> str:
    """
    Retrieves the URL corresponding to the given key from the configuration file.

    :param key: The key to retrieve the URL for.
    :type key: str
    :return: The URL corresponding to the given key.
    :rtype: str
    """
    with open(CONFIG, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config[key]["url"]
