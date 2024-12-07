from aiogram.fsm.state import StatesGroup, State


class StateList(StatesGroup):
    """
    Класс - хранилище возможных состояний бота
    """
    name = State()
    grade = State()
    comment = State()