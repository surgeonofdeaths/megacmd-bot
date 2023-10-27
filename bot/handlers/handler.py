from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from loguru import logger

from bot.services import megacmd

router = Router()


@router.message()
async def test(message: Message):
    logger.info(f"The user entered {message.text}")
    await message.answer(
        f"list all files in {megacmd.mega_pwd()}\n{megacmd.mega_ls()}",
    )


@router.message(Command(commands=['ls']))
async def list_all_files(message: Message):
    ...
