from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

class Processing:
    """
    Класс, содержащий вспомогательные, сервисные методы
    """
    @staticmethod
    def create_inline_keyboard():
        """
        Создает инлайн кнопки
        """
        buttons = ["Завтрак", "Обед", "Ужин", "Десерт"]

        builder = InlineKeyboardBuilder()

        for i in buttons:
            builder.button(text=i, callback_data=i)

        builder.adjust(2)

        return builder.as_markup()
