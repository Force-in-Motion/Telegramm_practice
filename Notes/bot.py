import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

from Notes.model.model import Notes
from service.receiving import ServiceData
from aiogram import F


bot = Bot(token=ServiceData.read_token())

dp = Dispatcher()

notes =  Notes()


@dp.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    mess = ('Бот помогает пользователю составить план дня,\n'
            ' добавляя задачи с указанием времени. \n'
            '/add <время> <описание> - добавляет задачу .\n'
            '/show - показывает список задач на день.\n'
            '/del <время> - удаляет задачу по времени .\n'
            '/clear - очищает весь план дня. \n'
            '/save - сохраняет заметки  после добавления в список')
    await message.answer(mess)


@dp.message(Command('add'))
async def add_task_handler(message: types.Message, command: CommandObject) -> None:
    if not (command.args is None):
        notes.create_note(command.args)
        await message.answer(f'Заметка {command.args} успешно добавлена')
    else:
        await message.answer('Введите время и текст заметки')


@dp.message(Command('del'))
async def remove_handler(message: types.Message, command: CommandObject) -> None:
    removed = notes.remove_note(command.args)
    await message.answer(f'Заметка {command.args} успешно удалена' if removed else 'Заметка с указанным временем не найдена')


@dp.message(Command('clear'))
async def cler_handler(message: types.Message) -> None:
    clear = notes.clear_notes()
    await message.answer('Все заметки удалены' if clear else 'Список заметок пуст, удалять нечего')


@dp.message(Command('show'))
async def show_handler(message: types.Message) -> None:
    show = notes.show_notes()
    await message.answer(show if show else 'Вы пока не добавили заметки')


@dp.message(Command('save'))
async def save_handler(message: types.Message) -> None:
    save = notes.save()
    await message.answer('Заметки успешно сохранены' if save else 'Список заметок пуст, сохранять нечего')


@dp.message(F.text)
async def other_text_handler(message: types.Message) -> None:
    await message.reply('Не верно введена команда')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
