from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from loguru import logger

from config.config import config
from handlers import handler
from keyboards.main_menu import set_main_menu
from misc import redis
from middlewares.db import DbSessionMiddleware
from db.database import sessionmaker

import asyncio


async def main():
    logger.add(
        sink=config.logging.sink,
        format=config.logging.format,
        level=config.logging.level,
        rotation=config.logging.rotation,
        compression=config.logging.compression,
        serialize=config.logging.serialize,
    )
    logger.info("Starting bot")

    bot: Bot = Bot(token=config.bot.token, parse_mode=config.bot.parse_mode)
    dp: Dispatcher = Dispatcher(storage=RedisStorage(redis))

    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))

    dp.include_router(handler.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
