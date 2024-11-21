import json
import os

class ServiceData:

    @staticmethod
    def check_folder() -> None:
        """
        Проверяет наличие папки по указанному пути, если ее нет то создает
        :return: bool
        """
        if not os.path.isdir(path_dir):
            os.mkdir(path_dir)


    @staticmethod
    def check_file() -> bool:
        """
        Проверяет наличие файла по указанному пути
        :return: bool
        """
        if not os.path.isfile(path_dir + r'\data_notes'):
            return False
        else:
            return True


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
        """
        Считывает токен из файла
        :return: Токен в виде строки
        """
        with open(ServiceData.get_token_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
            token = data["TOKEN"]
            return token


    @staticmethod
    def read_notes() -> dict:
        """
        Считывает данные заметок из файла
        :return: dict
        """
        with open(path_dir + r'\data_notes', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_notes(*args) -> None:
        """
        Записывает данные в файл
        :param data: Принимает данные
        :return: None
        """
        with open(path_dir + r'\data_notes', 'w', encoding='utf-8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)


    @staticmethod
    def get_notes() -> dict:
        """
        Проверяет наличие папки, если ее нет то создает, затем проверяет наличие файла,
        если файл есть то считывает из него данные в виде словаря, иначе создает пустой словарь
        :return: dict
        """
        ServiceData.check_folder()
        notes = ServiceData.read_notes() if ServiceData.check_file() else {}
        return notes


path_dir = os.environ.get('LOCALAPPDATA') + r'\Notes Bot'

