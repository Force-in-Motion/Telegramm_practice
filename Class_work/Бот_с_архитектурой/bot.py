import asyncio

from aiogram import Bot, Dispatcher
from handlers import start, date


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router, date.router)

    # Для удаления всех сообщений, которые пришли боту,
    # но он на них не ответил
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
