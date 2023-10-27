import subprocess


def _execute(command: str) -> str:
    return subprocess.check_output([command]).decode()


def mega_ls() -> list[str]:
    proccessed_data = _execute(command='mega-ls').strip().split('\n')
    return proccessed_data


def mega_cd() -> str:
    return _execute(command='mega-cd')


def mega_pwd() -> str:
    return _execute(command='mega-pwd')
