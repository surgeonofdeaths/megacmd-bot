from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb(*buttons: list[str]):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons)
    return kb_builder.as_markup()
