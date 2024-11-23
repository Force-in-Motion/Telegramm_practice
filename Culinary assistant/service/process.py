from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

class Processing:

    @staticmethod
    def create_keyboard_and_started_mess():
        buttons = ["Завтрак", "Обед", "Ужин", "Десерт"]

        kb_builder = ReplyKeyboardBuilder()

        for i in buttons:
            kb_builder.add(types.KeyboardButton(text=i))

        kb_builder.adjust(2)

        kb_markup = kb_builder.as_markup()

        return kb_markup