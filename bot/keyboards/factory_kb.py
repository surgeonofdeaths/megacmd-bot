from aiogram.filters.callback_data import CallbackData


class NavigationCallbackFactory(CallbackData, prefix="nav"):
    is_file: bool
    action: str  # dir, file, go_back
