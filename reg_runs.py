import winreg
import json
import logging
from pprint import pprint as pp
from typing import Dict, List, Union, Tuple

logger = logging.getLogger(__name__)


def load_reg_paths(json_path: str) -> Dict[str, List[str]]:
    try:
        with open(json_path, 'r') as f:
            reg_paths = json.load(f)
    except FileNotFoundError:
        logger.error(f"{json_path} not found")
        reg_paths = {}
    return reg_paths


def get_reg_values(key: int, subkey: str) -> Dict[str, Union[str, int]]:
    reg_values = {}
    try:
        with winreg.OpenKey(key, subkey) as reg_key:
            for i in range(winreg.QueryInfoKey(reg_key)[1]):
                name, value, _ = winreg.EnumValue(reg_key, i)
                reg_values[name] = value
    except PermissionError as pe:
        logger.error(f"Permission error: Unable to open registry key {subkey}: {pe}")
    except WindowsError as we:
        if we.errno == 2:
            logger.info(f"Windows error: Cannot open registry key {subkey}: {we.args[1]}")
        else:
            logger.error(f"Windows error: Unable to open registry key {subkey}: {we}")
    except Exception as e:
        logger.error(f"Error reading registry key {subkey}: {e}")
    return reg_values


def extract_hive_key(registry_path: str) -> Tuple[int, str]:
    hive, subkey = registry_path.split("\\", 1)
    try:
        key = getattr(winreg, hive)
    except AttributeError:
        logger.error(f"{hive} is not a valid registry hive")
        key = None
    return key, subkey


def reg_runs():
    paths = load_reg_paths("paths.json")
    registry_paths = paths.get("registry_paths", [])

    for registry_path in registry_paths:
        key, subkey = extract_hive_key(registry_path)
        if key is not None:
            reg_values = get_reg_values(key, subkey)
            if reg_values:
                yield reg_values


if __name__ == "__main__":
    main()
