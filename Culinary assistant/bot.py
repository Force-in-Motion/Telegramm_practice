import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from service.receiving import ServiceData as sd
from model.model import Recipe
from service.process import Processing

dp = Dispatcher()

bot = Bot(token=sd.read_token())

rec = Recipe()


@dp.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    kb_markup = Processing.create_keyboard_and_started_mess()

    mess = ('Бот помогает пользователю выбрать рецепт по категории\n'
           'И предложить пошаговые инструкции для приготовления блюда\n'
           'Команды : \n'
           '/create "категория" "название" "описание" — создает рецепт из заданной категории с заданным описанием\n'
           '/get "название" — предоставляет рецепт выбранного блюда\n'
           '/del "название" — удаляет рецепт по названию.')

    await message.answer(mess, reply_markup=kb_markup)


@dp.message(Command('create'))
async def create_handler(message: types.Message, command: CommandObject) -> None:
    if not (command.args is None):
        result = rec.create_recipe(command.args)
        await message.answer('Рецепт успешно добавлен' if result else 'Не удалось добавить рецепт')

    await message.answer('Укажите категорию, название и описание рецепта')


@dp.message(Command('get'))
async def get_handler(message: types.Message, command: CommandObject) -> None:
    if not (command.args is None):
        result = rec.get_recipe(command.args)
        await message.answer(result if result else 'Рецепт с таким названием отсутствует')

    await message.answer('Укажите название рецепта')


@dp.message(Command('del'))
async def del_handler(message: types.Message, command: CommandObject) -> None:
    if not (command.args is None):
        result = rec.del_recipe(command.args)
        await message.answer('Рецепт успешно удален' if result else 'Рецепт с таким названием отсутствует')

    await message.answer('Укажите название рецепта')


@dp.message(F.text)
async def other_text_handler(message: types.Message) -> None:
    await message.answer('Введите команду из предложенных')



async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())