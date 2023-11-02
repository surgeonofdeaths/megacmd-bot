from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)

from bot.keyboards.factory_kb import NavigationCallbackFactory
from bot.lexicon.lexicon import LEXICON
from bot.services import megacmd, other

from subprocess import CalledProcessError


def build_inline_kb(*buttons: list[str]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons)
    kb_builder.adjust(4)
    return kb_builder.as_markup()


def form_nav_buttons() -> list[InlineKeyboardButton]:
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
    try:
        megacmd.mega_ls('..')
        buttons.insert(
            0,
            InlineKeyboardButton(
                text=LEXICON["go_back"],
                callback_data=NavigationCallbackFactory(
                    title="go_back", is_file=False, action="go_back"
                ).pack(),
            ),
        )
    except CalledProcessError:
        pass
    return buttons
