""""""
import json
import shutil


from settings import time_stamp, data_dir

filename_to_load_cmc_data_from_file = data_dir / 'json_files' / 'cmc_readable_data.json'
filename_to_load_exchangers_data_from_file = data_dir / 'json_files' / 'exchangers_readable_data.json'


class JsonFile:

    def wright_to_json_cmc_data(self, data: list[dict] | dict[dict]):
        """Writing to file human-readable data."""
        filename = data_dir / 'json_files' / f'cmc_data_{time_stamp}.json'
        self.wright_to_json(data, filename)
        shutil.copy(filename, filename_to_load_cmc_data_from_file)

    def wright_to_json_exchangers_data(self, data: list[dict] | dict[dict]):
        """Writing to file human-readable data."""
        filename = data_dir / 'json_files' / f'exchangers_data_{time_stamp}.json'
        self.wright_to_json(data, filename)
        shutil.copy(filename, filename_to_load_exchangers_data_from_file)

    @staticmethod
    def wright_to_json(data: list[dict] | dict[dict], filename):
        """Writing to file human-readable data."""
        with open(filename, 'w') as file_json:
            json.dump(data, file_json, indent=4)

    @staticmethod
    def load_cmc_data_from_file() -> dict:
        with open(filename_to_load_cmc_data_from_file, 'r') as file_json:
            loaded_data = json.load(file_json)
        return loaded_data

    @staticmethod
    def load_exchangers_data_from_file() -> dict:
        with open(filename_to_load_exchangers_data_from_file, 'r') as file_json:
            loaded_data = json.load(file_json)
        return loaded_data

