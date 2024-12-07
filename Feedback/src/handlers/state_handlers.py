from Feedback.src.model.state import StateList
from Feedback.src.model.processing import ListReview
from Feedback.src.keyboards.keyboards import KeyBoards

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram import Router, types
from aiogram import F

router = Router()
list_review = ListReview()

@router.message(StateFilter(None), F.text.lower() == 'оставить отзыв')
@router.message(StateFilter(None), Command('feedback'))
async def input_name_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return:None
    """
    await message.answer('Введите название темы для отзыва')

    await state.set_state(StateList.name)


@router.message(StateFilter(StateList.name), F.text)
async def input_grade_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return: None
    """
    await state.update_data(name=message.text)

    await message.answer('Введите вашу оценку от 1 до 5 включительно', reply_markup=KeyBoards.create_inline_kb())

    await state.set_state(StateList.grade)


@router.message(StateFilter(StateList.grade), F.text.in_(KeyBoards.grade))
async def input_comment_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return: None
    """
    await state.update_data(grade=message.text)

    await state.set_state(StateList.comment)

    await message.answer('Введите текст отзыва')


@router.message(StateFilter(StateList.comment), F.text)
async def create_review_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return: None
    """
    await state.update_data(comment=message.text)

    review_data = await state.get_data()

    list_review.add_review(message.chat.id, review_data['name'], review_data['grade'], review_data['comment'])

    await message.answer('Ваш отзыв успешно добавлен')

    await state.clear()


@router.message(StateFilter(StateList.name, StateList.grade, StateList.comment))
async def input_error_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученную команду пользователя
    :param message: Принимает текст сообщения, которое пользователь пишет в чат
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return: None
    """

    await message.answer('Введите данные из предложенных!')