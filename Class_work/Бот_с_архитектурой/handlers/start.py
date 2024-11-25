from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from aiogram import F

from keyboards import get_reply_keyboard, get_inline_keyboard


router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Вы запустили бота с хорошей архитектурой",
        reply_markup=get_inline_keyboard()
        )

@router.callback_query(F.data == "yes")
async def yes_callback_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вы нажали на inline-кнопку \"Да\"")
    await callback.answer()


@router.callback_query(F.data == "no")
async def no_callback_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вы нажали на inline-кнопку \"Нет\"")
    await callback.answer()


@router.callback_query(F.data == "other")
async def other_callback_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вы нажали на inline-кнопку \"Иное\"")
    await callback.answer()
