from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.filters import Command
from loguru import logger

from bot.services import megacmd, other
from bot.keyboards.cd_ls import get_kb
from bot.keyboards.factory_kb import NavigationCallbackFactory

router = Router()


@router.message(Command(commands=["ls"]))
async def process_ls_entities(message: Message):
    buttons = [
        InlineKeyboardButton(
            text=other.form_title(title, is_file=is_file),
            callback_data=NavigationCallbackFactory(
                title=title,
                is_file=is_file,
                action=other.define_action_button(is_file=is_file),
            ).pack(),
        )
        for title, is_file in other.decide_file_or_dir(megacmd.mega_ls())
    ]
    buttons.insert(
        0,
        InlineKeyboardButton(
            text="⬅️ Go back",
            callback_data=NavigationCallbackFactory(
                title="go_back", is_file=False, action="go_back"
            ).pack(),
        ),
    )
    print(buttons)

    kb = get_kb(*buttons)

    await message.answer(
        text="Navigate through Mega using buttons",
        reply_markup=kb,
    )


@router.callback_query(
    NavigationCallbackFactory.filter(F.action == "dir")
)
async def process_directory(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    await query.answer("dir")


@router.callback_query(
    NavigationCallbackFactory.filter(F.action == "file")
)
async def process_file(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    await query.answer("file")


@router.callback_query(
    NavigationCallbackFactory.filter(F.action == "go_back")
)
async def process_go_back(
    query: CallbackQuery, callback_data: NavigationCallbackFactory
):
    megacmd.mega_cd('..')
    # await query.answer("go back")
    # await query.answer(
    #     text="Navigate through Mega using buttons",
    #     reply_markup=query,
    # )
    await query.message.edit_reply_markup()


@router.message()
async def process_wrong_text(message: Message):
    logger.info(f"User entered something else: {message.text}")
    await message.answer("You should enter something else")
