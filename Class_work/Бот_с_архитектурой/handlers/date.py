import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram import types


WEEKDAYS = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]

router = Router()

@router.message(Command('weekday'))
async def weekday_handler(message: types.Message):
    weekday = datetime.datetime.today().weekday()
    await message.reply(f"Сегодня: {WEEKDAYS[weekday]}")
