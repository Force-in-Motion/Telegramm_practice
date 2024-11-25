import asyncio

from Culinary_assistant.service.process import Processing
from Culinary_assistant.model.model import Recipe, Meals
from aiogram.filters.command import Command, CommandObject
from aiogram import Router, types
from aiogram import F


router = Router()

rec = Recipe()


@router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает команду
    :return: None
    """
    mess = ('Бот помогает пользователю выбрать рецепт по категории\n'
           'И предложить пошаговые инструкции для приготовления блюда\n'
           'Команды : \n'
           '/create "категория" "название" "описание" — создает рецепт из заданной категории с заданным описанием\n'
           '/get "название" — предоставляет рецепт выбранного блюда\n'
           '/del "название" — удаляет рецепт по названию.\n'
           '/save сохраняет изменения в файл, изменения в данных вступят в силу после перезагрузки бота')

    await message.answer(mess, reply_markup=Processing.create_inline_keyboard())


@router.message(Command('create'))
async def create_handler(message: types.Message, command: CommandObject) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает команду
    :return: None
    """
    if not (command.args is None):
        result = rec.create_recipe(command.args)
        await message.answer('Рецепт успешно добавлен' if result else 'Не верно указана категория или рецепт с таким названием уже существует')
    else:
        await message.answer('Укажите категорию, название и описание рецепта')


@router.message(Command('get'))
async def get_handler(message: types.Message, command: CommandObject) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает команду
    :return: None
    """
    if not (command.args is None):
        result = rec.get_recipe(command.args)
        await message.answer(result if result else 'Рецепт с таким названием отсутствует')
    else:
        await message.answer('Укажите название рецепта')


@router.message(Command('del'))
async def del_handler(message: types.Message, command: CommandObject) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает команду
    :return: None
    """
    if not (command.args is None):
        result = rec.del_recipe(command.args)
        await message.answer('Рецепт успешно удален' if result else 'Рецепт с таким названием отсутствует')
    else:
        await message.answer('Укажите название рецепта')


@router.message(Command('save'))
async def save_handler(message: types.Message) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает команду
    :return: None
    """
    await message.answer('Данные успешно сохранены' if rec.save() else 'Сохранять нечего, для начала добавьте рецепты')


@router.message(F.text)
async def other_text_handler(message: types.Message) -> None:
    """
    Обрабатывает полученный текст пользователя, который не соответствует ни одной команде
    :param message: Принимает текст
    :return: None
    """
    await message.answer('Введите команду из предложенных')
