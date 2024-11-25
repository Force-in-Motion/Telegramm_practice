
from Culinary_assistant.model.model import Meals, Recipe
from aiogram import Router, types
from aiogram import F


meals = Meals()

router = Router()

@router.callback_query(F.data == "Завтрак")
async def breakfast_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Завтрак"
    :return: None
    """
    await callback.message.answer(meals.get_breakfast_recipe())
    await callback.answer()


@router.callback_query(F.data == "Обед")
async def dinner_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Обед"
    :return: None
    """
    await callback.message.answer(meals.get_dinner_recipe())
    await callback.answer()


@router.callback_query(F.data == "Ужин")
async def evening_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Ужин"
    :return: None
    """
    await callback.message.answer(meals.get_evening_recipe())
    await callback.answer()


@router.callback_query(F.data == "Десерт")
async def dessert_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Десерт"
    :return: None
    """
    await callback.message.answer(meals.get_dessert_recipe())
    await callback.answer()



