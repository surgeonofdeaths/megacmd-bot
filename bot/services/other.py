from keyboards.factory_kb import NavigationCallbackFactory

from misc import redis
from uuid import uuid4
from loguru import logger


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


async def _set_title(title, uuid) -> None:
    await redis.set(uuid, title)
    redis_get = await redis.get(uuid)
    logger.info("redis get: " + redis_get.decode("UTF-8"))


async def generate_uuid(title: str) -> str | None:
    if len(title) > 51:
        uuid = str(uuid4())
        await _set_title(title, uuid)
        return uuid


def generate_title(title: str) -> str | None:
    if len(title) <= 51:
        return title


async def get_filename(callback_data: NavigationCallbackFactory) -> str:
    if callback_data.title:
        name = callback_data.title
    else:
        name = await redis.get(callback_data.uuid)
    return name
