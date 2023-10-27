import subprocess

print(subprocess.check_output(['mega-ls']).decode())
# [print(x) for x in subprocess.check_output(['ls', '-l']).split('\n')]
