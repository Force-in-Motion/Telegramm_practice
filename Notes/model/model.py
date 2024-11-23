from Notes.service.receiving import ServiceData as sd

class Notes:

    def __init__(self):
        """
        Создает временную область памяти, хранящую заметки в виде словаря,
        Если есть сохраненные заметки, то выгружает их из файла, иначе создает пустой словарь
        """
        self.__notes = sd.get_notes()
        self.__old_notes = self.__notes.copy()


    def create_note(self, data) -> None:
        """
        Создает новую заметку , Принимает данные в виде строки, преобразует в список чтобы разбить строку на время и заметку,
        затем сохраняет в словарь, где первый элемент списка (время) будет ключем, а текст заметки значением
        :param data: Принимает данные в виде строки
        :return: None
        """
        data = data.split()
        key = data[0]
        del data[0]
        self.__notes[key] = ' '.join(data)


    def remove_note(self, data) -> bool:
        """
        Удаляет заметку по ключу если такой имеется в словаре и возвращает True иначе вернет False
        :param data: Принимает ключ словаря
        :return: bool
        """
        if not data in self.__notes:
            return False

        del self.__notes[data]
        return True


    def clear_notes(self) -> bool:
        """
        Удаляет все данные словаря если он не None и возвращает True иначе вернет False
        :return: bool
        """
        if not self.__notes is None:
            self.__notes.clear()
            return True

        return False


    def show_notes(self) -> str:
        """
        Преобразует ключ - значение словаря в кортежи и сортирует по первому элементу (времени),
        затем создает пустую строку, в которую при обходе циклом по сортированному словарю записываются в виде строки ключ - значение
        :return: Возвращает строку
        """
        sorted_notes = dict(sorted(self.__notes.items()), key=lambda x: x[0])
        response_mess = ''
        for key, value in sorted_notes.items():
            response_mess += f'{key}, {value}\n'

        return response_mess


    def save(self):
        """
        Сохраняет данные в файл если область временной памяти (словарь) не None и возвращает True иначе False
        :return: bool
        """
        if self.__notes != self.__old_notes:
            sd.write_notes(self.__notes)
            return True

        return False



