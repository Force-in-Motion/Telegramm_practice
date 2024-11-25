
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
    result = meals.get_recipe("Завтрак")
    await callback.message.answer(result if not (result is None) else 'Вы еще не добавили ни одного рецепта в категорию "Завтрак"')
    await callback.answer()


@router.callback_query(F.data == "Обед")
async def dinner_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Обед"
    :return: None
    """
    result = meals.get_recipe("Обед")
    await callback.message.answer(result if not (result is None) else 'Вы еще не добавили ни одного рецепта в категорию "Обед"')
    await callback.answer()


@router.callback_query(F.data == "Ужин")
async def evening_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Ужин"
    :return: None
    """
    result = meals.get_recipe("Ужин")
    await callback.message.answer(result if not (result is None) else 'Вы еще не добавили ни одного рецепта в категорию "Ужин"')
    await callback.answer()


@router.callback_query(F.data == "Десерт")
async def dessert_callback_handler(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по кнопке "Десерт"
    :return: None
    """
    result = meals.get_recipe("Десерт")
    await callback.message.answer(result if not (result is None) else 'Вы еще не добавили ни одного рецепта в категорию "Десерт"')
    await callback.answer()



