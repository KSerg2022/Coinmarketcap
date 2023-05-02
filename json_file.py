""""""
import json
import shutil


from settings import base_dir, time_stamp

filename_to_load_data_from_file = base_dir / 'json_files' / 'readable_data.json'


def wright_to_json(data: dict):
    """Writing to file human-readable data."""
    filename = base_dir / 'json_files' / f'data_{time_stamp}.json'
    with open(filename, 'w') as file_json:
        json.dump(data, file_json, indent=4)

    shutil.copy(filename, filename_to_load_data_from_file)
    return True


def load_data_from_file() -> dict:
    with open(filename_to_load_data_from_file, 'r') as file_json:
        loaded_data = json.load(file_json)
    return loaded_data
