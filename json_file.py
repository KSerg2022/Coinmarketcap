""""""
import json
import shutil


from settings import base_dir, time_stamp

filename_to_load_cmc_data_from_file = base_dir / 'json_files' / 'cmc_readable_data.json'
filename_to_load_exchangers_data_from_file = base_dir / 'json_files' / 'exchangers_readable_data.json'


def wright_to_json_cmc_data(data: list[dict] | dict[dict]):
    """Writing to file human-readable data."""
    filename = base_dir / 'json_files' / f'cmc_data_{time_stamp}.json'
    wright_to_json(data, filename)
    shutil.copy(filename, filename_to_load_cmc_data_from_file)


def wright_to_json_exchangers_data(data: list[dict] | dict[dict]):
    """Writing to file human-readable data."""
    filename = base_dir / 'json_files' / f'exchangers_data_{time_stamp}.json'
    wright_to_json(data, filename)
    shutil.copy(filename, filename_to_load_exchangers_data_from_file)


def wright_to_json(data: list[dict] | dict[dict], filename):
    """Writing to file human-readable data."""
    with open(filename, 'w') as file_json:
        json.dump(data, file_json, indent=4)


def load_cmc_data_from_file() -> dict:
    with open(filename_to_load_cmc_data_from_file, 'r') as file_json:
        loaded_data = json.load(file_json)
    return loaded_data


def load_exchangers_data_from_file() -> dict:
    with open(filename_to_load_exchangers_data_from_file, 'r') as file_json:
        loaded_data = json.load(file_json)
    return loaded_data

