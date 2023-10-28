from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def get_kb(*buttons: list[str]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons)
    return kb_builder.as_markup()
