import asyncio

from aiogram import Bot, Dispatcher
from service.receiving import ServiceData
from handlers import handlers



async def main():
    bot = Bot(token=ServiceData.read_token())

    dp = Dispatcher()

    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
