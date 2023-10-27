from aiogram import Bot, Dispatcher
from loguru import logger

from bot.config.config import config
from bot.handlers import handler
from bot.keyboards.main_menu import set_main_menu

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
    dp: Dispatcher = Dispatcher()

    dp.include_router(handler.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
