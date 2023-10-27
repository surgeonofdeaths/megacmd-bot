from aiogram import Router
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.filters import Command
from loguru import logger

from bot.services import megacmd
from bot.keyboards.cd_ls import get_kb

router = Router()


@router.message(Command(commands=["ls"]))
async def list_all_files(message: Message):
    buttons = [
        InlineKeyboardButton(text=button, callback_data=button)
        for button in megacmd.mega_ls()
    ]
    kb = get_kb(*buttons)
    print(type(kb), kb)

    await message.answer(
        text="Navigate through Mega using buttons",
        reply_markup=kb,
    )


@router.message()
async def test(message: Message):
    logger.info(f"User entered something else: {message.text}")
    await message.answer("You should enter something else")
