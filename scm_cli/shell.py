import subprocess

def run(command, capture=False):
    command = command if isinstance(command, list) else command.split()

    kwargs = {}
    if capture:
        kwargs['stderr'] = subprocess.STDOUT
        kwargs['stdout'] = subprocess.PIPE

    p = subprocess.Popen(command, **kwargs)

    output, error = p.communicate()

    if error:
        raise Exception(str(error))

    return output
