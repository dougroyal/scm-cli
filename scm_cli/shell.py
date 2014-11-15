import subprocess

def run(command):
    command = command if isinstance(command, list) else command.split()

    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    output, error = p.communicate()

    if error:
        raise Exception(str(error))

    return output
