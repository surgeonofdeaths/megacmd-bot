from misc import redis
from uuid import uuid4


def is_file(title: str) -> bool:
    return "." in title


def decide_file_or_dir(ls_data: list[str]) -> list[set[str, bool]]:
    ls_data = [(x, True) if is_file(x) else (x, False) for x in ls_data]
    return ls_data


def form_title(title: str, is_file: bool = True) -> str:
    # TODO: recognize formats and choose according emojis
    emoji = "🗒" if is_file else "🗂"
    return emoji + "  " + title


def define_action_button(is_file: bool = True) -> str:
    if is_file:
        return "file"
    return "dir"


def _generate_uuid(title: str) -> str:
    uuid = str(uuid4())
    return uuid


def check_title_length(title: str) -> bool:
    return len(title) >= 51


def generate_title_or_uuid(title: str) -> str:
    """
    returns title of a file or a dir if its length
    is valid for callback_data else returns uuid
    and caches the title
    """
    if len(title) >= 51:
        uuid = str(uuid4())
        redis.set(uuid, title)
        return uuid
    return title
