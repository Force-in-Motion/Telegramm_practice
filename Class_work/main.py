import asyncio # Библиотека, требуемая для работы с асинхронным кодом
import random

from aiogram import Bot, Dispatcher, types # Библиотека, требуемая для создания асинхронного бота и ее составные части, требуемые для этого
from aiogram import F # Модуль специальных фильтров, который будет реагировать на любой полученный текст
from aiogram.filters.command import Command # Импорт фильтра, требуемого диспетчеру для обработки полученной из чата команды и выбора подходящего обработчика (хэндлера )
from config import TOKEN # Токен выдает бот фазер при создании бота в телеграмм, он идентифицирует бот в телеге и если его потерять то доступ к боту получить будет невозможно, если узнать токен чужого бота, то этого бота можно будет угнать


bot = Bot(token=TOKEN) # Создание объекта бота, передача ему токена

dp = Dispatcher() # Создание объекта диспетчера, он нужен чтобы получать сообщения в чате, обрабатывать их, подбирать соответствующий полученной команде обработчик при помощи фильтра и вызывать его

@dp.message(Command('start'))# Чтобы у Диспетчера появилось знание о наличии какого либо обработчика его нужно зарегистрировать при помощи такого декоратора, внутри декоратора передается фильтр, при помощи которого диспетчер ищет совпадения между введенными командами и хендлерами
async def start_handler(message: types.Message) -> None: # Функция - обработчик, которая будет вызвана если команда в фильтре идентична команде, которую ввел пользователь, ее вызовет диспетчер если в фильтре определит это совпадение
    await message.answer('Я получил команду /start')


@dp.message(Command('number'))
async def random_handler(message: types.Message) -> None:
    random_number = random.randint(1,100)
    await message.reply(f'Случайное число {random_number}')


@dp.message(F.text)
async def text_handler(message: types.Message) -> None: # F обработчик пишется всегда последним, поскольку он срабатывает на любой текст, если его поставить первым или в середине то он один будет обрабатывать все полученные команды и до других обработчиков команды доходить не будут
    await message.answer(message.text) # Вернет пользователю в чат то же самое сообщение, которое написал пользователь


async def main():
    await dp.start_polling(bot) # Бесконечный опрос команд, пришедших в чат боту


asyncio.run(main())