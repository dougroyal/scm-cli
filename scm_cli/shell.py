import subprocess

def run(command):
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    output, error = p.communicate()

    if error:
        print(error)
        raise(Excepiton, error)

    return output
