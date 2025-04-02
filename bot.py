import logging
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import route
from config import token


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)

# Диспетчер
dp = Dispatcher()


async def main():
    dp.include_router(route)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
