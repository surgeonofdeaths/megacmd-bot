from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command="login",
            description="Login to your mega account",
        ),
        BotCommand(
            command="info",
            description="What can this bot do?",
        ),
        BotCommand(
            command="navigate",
            description="Navigate through your folder structure",
        ),
    ]
    await bot.set_my_commands(main_menu_commands)
