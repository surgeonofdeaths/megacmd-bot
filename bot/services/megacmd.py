import subprocess


def _execute(command: str) -> str:
    return subprocess.check_output([command]).decode()


def mega_ls() -> str:
    return _execute(command='mega-ls')


def mega_cd() -> str:
    return _execute(command='mega-cd')


def mega_pwd() -> str:
    return _execute(command='mega-pwd')
