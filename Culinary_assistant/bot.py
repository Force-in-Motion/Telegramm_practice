import asyncio

from aiogram import Bot, Dispatcher
from service.receiving import ServiceData as sd
from handlers import commandHandlers, callbackHandlers


async def main() -> None:
    bot = Bot(token=sd.read_token())

    dp = Dispatcher()

    dp.include_routers(commandHandlers.router, callbackHandlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())