from aiogram.filters.callback_data import CallbackData


class NavigationCallbackFactory(CallbackData, prefix="nav"):
    # TODO: Длина коллбека измеряется в байтах.
    # Русские символы занимают очень много.
    # Нужно класть данные в бд, присваивать им айди, а в коллбек уже
    # работать через этот айди, тогда будет ок все.
    title: str = ""
    uuid: str | None
    is_file: bool = True
    action: str  # dir, file
