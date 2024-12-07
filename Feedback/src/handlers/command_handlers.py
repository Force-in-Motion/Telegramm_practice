from Feedback.service.service import DataService as ds

from aiogram.filters import Command
from Feedback.src.keyboards.keyboards import KeyBoards
from aiogram import Router, types
from aiogram import F


router = Router()


@router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    """
    Обрабатывает команду 'start'
    Отправляет стартовое, приветственное сообщение с описанием функционала и возможными командами
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :return: None
    """
    mess = ('Вас приветствует отдел качества обслуживания\n'
           '/feedback и текст сообщения чтобы оставить отзыв \n'
           '/show для того чтобы просмотреть ваши отзывы\n'
            '/csv для выгрузки всех отзывов в csv файл'
            'Либо нажмите соответствующие кнопки на клавиатуре')

    await message.answer(mess, reply_markup=KeyBoards.create_reply_keyboard())


@router.message(F.text.lower() == 'показать отзывы')
@router.message(Command('show'))
async def show_handler(message: types.Message) -> None:
    """
    Обрабатывает команду 'show'
    Выводит в чат бота все отзывы пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :return: None
    """
    id_user = str(message.chat.id)

    user_reviews = ds.get_review()

    if id_user not in user_reviews:
        await message.answer('Вы пока не добавили отзывы')

    await message.answer(''.join(user_reviews.get(id_user)))


@router.message(F.text.lower() == 'сохранить в csv')
@router.message(Command('csv'))
async def csv_handler(message: types.Message) -> None:
    """
    Обрабатывает команду пользователя запись в файл
    :param message:
    :return:
    """
    data = ds.get_review()

    id_user = str(message.chat.id)

    user_reviews = ''.join(data.get(id_user))

    ds.write_csv(user_reviews)

    await message.answer('Отзывы успешно записаны в csv файл')


@router.message(F.text)
async def other_text_handler(message: types.Message) -> None:
    """
    Обрабатывает любой текст, который не зарезервирован командами бота и просит пользователя ввести возможную команду
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :return: None
    """
    await message.answer('Введите команду из предложенных')