import subprocess


def _execute(*commands) -> str:
    return subprocess.check_output(list(commands)).decode()


def mega_ls(*parameters) -> list[str]:
    proccessed_data = _execute("mega-ls", *parameters)
    return proccessed_data.strip().split("\n")


def mega_cd(*parameters) -> str:
    return _execute("mega-cd", *parameters)


def mega_pwd() -> str:
    return _execute("mega-pwd")
