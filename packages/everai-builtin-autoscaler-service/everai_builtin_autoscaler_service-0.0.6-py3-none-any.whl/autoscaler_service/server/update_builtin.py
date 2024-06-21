import importlib
import logging
import subprocess
import sys
import everai_autoscaler.builtin


def update_builtin():
    result = subprocess.run("./update_builtin.sh", capture_output=True)
    match result.returncode:
        case 0:
            print('everai-builtin-autoscaler updated to new version')
            importlib.reload(everai_autoscaler.builtin)
        case _:
            ...

    if result.stdout and len(result.stdout) > 0:
        print(result.stdout)

    if result.stderr and len(result.stderr) > 0:
        print(result.stderr, file=sys.stderr)
