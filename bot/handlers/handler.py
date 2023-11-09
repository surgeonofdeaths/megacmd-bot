from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from loguru import logger

from services import megacmd, keyboard, other
from keyboards.factory_kb import NavigationCallbackFactory
from lexicon.lexicon import LEXICON, LEXICON_COMMANDS
from misc import redis

router = Router()


@router.message(Command(commands=["navigate"]))
async def process_navigate_command(message: Message):
    buttons = await keyboard.form_nav_buttons()
    kb = keyboard.build_inline_kb(*buttons)

    await message.answer(
        text=LEXICON_COMMANDS["/navigate"],
        reply_markup=kb,
    )


@router.callback_query(NavigationCallbackFactory.filter(F.action == "dir"))
async def process_dir_action(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    # TODO: toggle dir selection mode which allows
    # to compress directory to rar/zip format
    megacmd.mega_cd(callback_data.title)
    buttons = await keyboard.form_nav_buttons()
    kb = keyboard.build_inline_kb(*buttons)
    filename = await other.get_filename(callback_data)

    await query.answer(filename)
    await query.message.edit_reply_markup(
        reply_markup=kb,
    )


@router.callback_query(NavigationCallbackFactory.filter(F.action == "file"))
async def process_file_action(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    filename = await other.get_filename(callback_data)
    await query.answer(filename)


@router.callback_query(NavigationCallbackFactory.filter(F.action == "go_back"))
async def process_go_back_action(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    megacmd.mega_cd("..")
    buttons = await keyboard.form_nav_buttons()
    kb = keyboard.build_inline_kb(*buttons)
    await query.message.edit_reply_markup(
        reply_markup=kb,
    )


@router.message()
async def process_wrong_text(message: Message):
    logger.info(f"User entered something else: {message.text}")
    await message.answer(LEXICON["user_misspell"])
