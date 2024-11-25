import json
import os


class ServiceData:

    @staticmethod
    def check_folder() -> None:
        """
        Проверяет наличие папки, если нет- создает
        :return:
        """
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


    @staticmethod
    def check_file() -> bool:
        """
        Проверяет наличие файла
        :return: bool
        """
        if os.path.isfile(dir_path + r'\Recipe.json'):
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
        """
        Считывает токен из файла и возвращает его
        """
        with open(ServiceData.get_token_path(), 'r', encoding='utf-8')as f:
            data = json.load(f)
            token = data["TOKEN"]
            return token


    @staticmethod
    def read_data() -> dict:
        """
        Считывает данные из файла и возвращает их
        """
        with open(dir_path + r'\Recipe.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def read_category() -> list:
        """
        Считывает и возвращает из файла фаблон структуры данных для хранения рецептов
        """
        with open(ServiceData.get_token_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
            data_recipe = data["data_recipe"]
            return data_recipe


    @staticmethod
    def write_data(*args) -> None:
        """
        Записывает в файл полученные данные
        :return: None
        """
        with open(dir_path + r'\Recipe.json', 'w', encoding='utf-8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)



    @staticmethod
    def get_data() -> dict:
        """
        Подготавливает данные для работы, осуществляет проверки
        :return: dict
        """
        ServiceData.check_folder()
        data = ServiceData.read_data() if ServiceData.check_file() else ServiceData.read_category()
        return data






dir_path = os.environ.get('LOCALAPPDATA') + r'\Culinary assistant'