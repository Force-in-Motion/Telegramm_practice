import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()

def get_inline_keyboard():
    inline_kb_builder = InlineKeyboardBuilder()

    # Через метод button, то же самое что и сверху
    inline_kb_builder.button(text="Да", callback_data="yes")
    inline_kb_builder.button(text="Нет", callback_data="no")

    inline_kb_builder.adjust(2)
    return inline_kb_builder.as_markup()


@dp.callback_query(F.data == "yes")
async def yes_callback_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вы согласились")
    await callback.answer()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb_markup = get_inline_keyboard()
    await message.answer(
        "Клавиатура нужна, брат?",
        reply_markup=kb_markup
    )

dp.message.register(start_handler, Command("start"))


@dp.message(F.text.lower() == "да")
async def yes_handler(message: types.Message):
    await message.answer("Хорошо")


@dp.message(F.text.lower() == "нет")
async def no_handler(message: types.Message):
    await message.answer("Жаль")


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
