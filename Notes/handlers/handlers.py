import asyncio

from aiogram import types, Router
from aiogram import F
from aiogram.filters.command import Command, CommandObject
from Notes.model.model import Notes

router = Router()

notes = Notes()


@router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    mess = ('Бот помогает пользователю составить план дня,\n'
            ' добавляя задачи с указанием времени. \n'
            '/add <время> <описание> - добавляет задачу .\n'
            '/show - показывает список задач на день.\n'
            '/del <время> - удаляет задачу по времени .\n'
            '/clear - очищает весь план дня. \n'
            '/save - сохраняет заметки  после добавления в список')
    await message.answer(mess)


@router.message(Command('add'))
async def add_task_handler(message: types.Message, command: CommandObject) -> None:
    if not (command.args is None):
        notes.create_note(command.args)
        await message.answer(f'Заметка "{command.args}" успешно добавлена')
    else:
        await message.answer('Введите время и текст заметки')


@router.message(Command('del'))
async def remove_handler(message: types.Message, command: CommandObject) -> None:
    removed = notes.remove_note(command.args)
    await message.answer(f'Заметка "{command.args}" успешно удалена' if removed else 'Заметка с указанным временем не найдена')


@router.message(Command('clear'))
async def cler_handler(message: types.Message) -> None:
    clear = notes.clear_notes()
    await message.answer('Все заметки удалены' if clear else 'Список заметок пуст, удалять нечего')


@router.message(Command('show'))
async def show_handler(message: types.Message) -> None:
    show = notes.show_notes()
    await message.answer(show if show else 'Вы пока не добавили заметки')


@router.message(Command('save'))
async def save_handler(message: types.Message) -> None:
    save = notes.save()
    await message.answer('Заметки успешно сохранены' if save else 'Список заметок пуст, сохранять нечего')


@router.message(F.text)
async def other_text_handler(message: types.Message) -> None:
    await message.reply('Не верно введена команда')