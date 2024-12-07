from Feedback.src.model.state import StateList

from aiogram.fsm.context import FSMContext
from Feedback.src.keyboards.keyboards import KeyBoards
from aiogram.filters import StateFilter
from aiogram import Router, types


router = Router()


@router.callback_query(StateFilter(StateList.grade), lambda callback: callback.data in KeyBoards.grade )
async def input_grade_btn_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает колбэк полученный после нажатии инлайн кнопки
    :param callback: Колбэк полученный после нажатии инлайн кнопки
    :param state: Состояние, находясь в котором бот реагирует на команду пользователя
    :return: None
    """
    await state.update_data(grade=callback.data)

    await state.set_state(StateList.comment)

    await callback.message.answer('Введите текст отзыва')

    await callback.answer()


