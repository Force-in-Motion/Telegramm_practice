import copy
from Culinary_assistant.service.receiving import ServiceData as sd



class Recipe:

    def __init__(self):
        """
        Создает обьект класса, подгружает данные из файлов
        """
        self.__current_data = sd.get_data()
        self.__old_data = copy.deepcopy(self.__current_data)
        self.__category = sd.read_category()


    def create_recipe(self, command: str) -> bool:
        """
        Создает новый рецепт и добавляет его во временную память бота
        :param command: Принимает данные, необходимые для создания рецепта
        :return: bool
        """
        lst_str = command.split()

        category = lst_str[0].title()
        key = lst_str[1].title()
        value = ' '.join(lst_str[2:]).capitalize()

        if category not in self.__category:
            return False

        if key in self.__current_data[category]:
            return False

        if self.__current_data[category] == {}:
            self.__current_data[category] = {key: value}
            return True

        self.__current_data[category][key] = value

        return True


    def get_recipe(self, name) -> str or bool:
        """
        Возвращает рецепт, запрошенный пользователем по названию
        :param name: Принимает название рецепта
        :return: str or bool
        """
        for categories, recipes  in self.__current_data.items():
            if name.title() in recipes :
                return f'Содержание рецепта : \n {recipes [name.title()]}'

        return False


    def del_recipe(self, name) -> bool:
        """
        Удаляет рецепт по названию, полученному от пользователя
        :param name: Принимает название рецепта
        :return: bool
        """
        for categories, recipes  in self.__current_data.items():
            if name.title() in recipes :
                del recipes[name.title()]
                return True

        return False


    def save(self) -> bool:
        """
        Сохраняет данные в файле, если были внесены изменения
        :return: bool
        """
        if self.__current_data != self.__old_data:
            sd.write_data(self.__current_data)
            self.__old_data = copy.deepcopy(self.__current_data)
            return True

        return False


    @property
    def current_data(self):
        return self.__current_data




class Meals:

    def __init__(self):
        self.__recipe = Recipe()
        self.__category = sd.read_category()


    def get_breakfast_recipe(self) -> str:
        """
        Обрабатывает колбэк запрос, полученный от нажатия соответствующей кнопки
        :return: str
        """
        rec = f'Рецепты в категории "Завтрак" :\n'

        for name, recipe in self.__recipe.current_data["Завтрак"].items():
            rec += f'{name} : {recipe}\n'

        return rec


    def get_dinner_recipe(self) -> str:
        """
        Обрабатывает колбэк запрос, полученный от нажатия соответствующей кнопки
        :return: str
        """
        rec = f'Рецепты в категории "Обед" :\n'

        for name, recipe in self.__recipe.current_data["Обед"].items():
            rec += f'{name} : {recipe}\n'

        return rec



    def get_evening_recipe(self) -> str:
        """
        Обрабатывает колбэк запрос, полученный от нажатия соответствующей кнопки
        :return: str
        """
        rec = f'Рецепты в категории "Ужин" :\n'

        for name, recipe in self.__recipe.current_data["Ужин"].items():
            rec += f'{name} : {recipe}\n'

        return rec



    def get_dessert_recipe(self) -> str:
        """
        Обрабатывает колбэк запрос, полученный от нажатия соответствующей кнопки
        :return: str
        """
        rec = f'Рецепты в категории "Десерт" :\n'

        for name, recipe in self.__recipe.current_data["Десерт"].items():
            rec += f'{name} : {recipe}\n'

        return rec
