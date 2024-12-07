import asyncio
from aiogram import Bot, Dispatcher
from service.service import DataService as ds
from src.handlers import command_handlers
from src.handlers import state_handlers
from src.handlers import button_handlers




async def main():
    """
    Главная функция приложения, запускающая бесконечный опрос пользователя
    """
    bot = Bot(token=ds.get_token())

    dp = Dispatcher()

    dp.include_routers(state_handlers.router, button_handlers.router, command_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
