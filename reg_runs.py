import winreg
import json
import logging
from pprint import pprint as pp


def load_reg_paths(json_path) -> dict:
    try:
        with open(json_path, 'r') as f:
            reg_paths = json.load(f)
    except FileNotFoundError:
        logging.error(f"{f.name} not found")
    return reg_paths


def get_reg_values(key, subkey):
    reg_values = {}
    with winreg.OpenKey(key, subkey) as reg_key:
        for i in range(winreg.QueryInfoKey(reg_key)[1]):
            name, value, _ = winreg.EnumValue(reg_key, i)
            reg_values[name] = value

    return reg_values


def extract_hive_key(registry_path):
    hive = registry_path.split("\\")[0]
    subkey = "\\".join(registry_path.split("\\")[1:])
    try:
        key = getattr(winreg, hive)
    except AttributeError:
        logging.error(f"{hive} is not a valid hive")
        key = None
    return key, subkey


def main():
    paths = load_reg_paths("paths.json")
    registry_paths = paths["registry_paths"]
    for registry_path in registry_paths:
        reg_values = get_reg_values(*extract_hive_key(registry_path))
        pp(reg_values)


if __name__ == "__main__":
    main()
