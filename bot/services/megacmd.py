import subprocess


def _execute(command: str, *parameters) -> str:
    commands = [[command]]
    for param in parameters:
        commands.append([param])
    return subprocess.check_output(*commands).decode()


def mega_ls() -> list[str]:
    proccessed_data = _execute(command='mega-ls').strip().split('\n')
    return proccessed_data


def mega_cd(dir: str, *parameters) -> str:
    return _execute(command='mega-cd', *parameters)


def mega_pwd() -> str:
    return _execute(command='mega-pwd')
