import json
import os

class ServiceData:

    @staticmethod
    def check_folder() -> None:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


    @staticmethod
    def check_file() -> bool:
        if os.path.isfile(dir_path + r'\Recipe'):
            return True

        return False


    @staticmethod
    def get_token_path() -> str:
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path_token = os.path.join(current_dir, '..', 'storage', 'config.json')

        return os.path.abspath(path_token)


    @staticmethod
    def read_token() -> str:
        with open(ServiceData.get_token_path(), 'r', encoding='utf-8')as f:
            data = json.load(f)
            token = data["TOKEN"]
            return token


    @staticmethod
    def read_data() -> dict:
        with open(dir_path + r'\Recipe', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_data(*args) -> None:
        with open(dir_path + r'\Recipe', 'r', encoding='utf-8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)









dir_path = os.environ.get('LOCALAPPDATA') + r'\Culinary assistant'