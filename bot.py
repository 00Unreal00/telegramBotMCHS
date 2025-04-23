import logging
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import route as route1
from app.on_site_medical_aid import route as route2
from app.questions import route2 as route3
from app.training import route as route4
from app.emergency_services import route as route5
from app.about import route as route6
from app.go_back import route as route7
from config import token


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)

# Диспетчер
dp = Dispatcher()


async def main():
    dp.include_router(route1)
    dp.include_router(route2)
    dp.include_router(route3)
    dp.include_router(route4)
    dp.include_router(route5)
    dp.include_router(route6)
    dp.include_router(route7)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
