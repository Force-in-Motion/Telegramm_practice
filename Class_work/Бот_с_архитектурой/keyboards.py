from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_reply_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="1")
    builder.button(text="2")
    builder.button(text="3")

    builder.adjust(2)
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Введите число"
    )


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text="Да", callback_data="yes")
    builder.button(text="Нет", callback_data="no")
    builder.button(text="Иное", callback_data="other")

    builder.adjust(2)
    return builder.as_markup()
