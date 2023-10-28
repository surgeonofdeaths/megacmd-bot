def is_file(title: str) -> bool:
    return "." in title


def decide_file_or_dir(ls_data: list[str]) -> list[set[str, bool]]:
    ls_data = [
        (x, True) if is_file(x) else (x, False) for x in ls_data
    ]
    return ls_data


def form_title(title: str, is_file: bool = True) -> str:
    # TODO: recognize formats and choose according emojis
    emoji = "🗒" if is_file else "🗂"
    return emoji + "  " + title


def define_action_button(is_file: bool = True) -> str:
    if is_file:
        return "file"
    return "dir"
