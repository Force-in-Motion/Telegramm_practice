import json
import csv
import os


class DataService:

    @staticmethod
    def check_folder() -> None:
        """
        Проверяет наличие папки, если ее нет - создает
        :return: None
        """
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


    @staticmethod
    def check_file() -> bool:
        """
        Проверяет наличие файла
        :return: bool
        """
        if os.path.isfile(dir_path + r'\feedback.json'):
            return True

        return False


    @staticmethod
    def create_token_path():
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path_token = os.path.join(current_dir, '..', 'storage', 'token.json')
        return path_token


    @staticmethod
    def get_token():
        """
        Получает токен по указанному пути
        :return: Токен
        """
        with open(DataService.create_token_path(), 'r', encoding='utf=8') as f:
            data = json.load(f)
            token = data["TOKEN"]
            return token


    @staticmethod
    def read_review():
        """
        Считывает данные из файла
        :return: None
        """
        with open(dir_path + r'\feedback.json', 'r', encoding='utf=8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_review(*args) -> None:
        """
        Записывает данные в файл
        :param args: Принимает данные
        :return: None
        """
        with open(dir_path + r'\feedback.json', 'w', encoding='utf=8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)


    @staticmethod
    def write_csv(data) -> None:
        """
        Записывает данные в файл
        :param data: Принимает данные
        :return: None
        """
        with open(csv_path + r'\feedback.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)


    @staticmethod
    def get_review():
        """
        Получает данные из файла если они там есть или вопрвлащает пустой словарь
        :return: 
        """
        DataService.check_folder()
        return DataService.read_review() if DataService.check_file() else {}


dir_path = os.environ.get('LOCALAPPDATA')  + r'\Feedback data'
csv_path = os.path.expanduser('~') + r'\Documents'