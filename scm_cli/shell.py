import subprocess

def run(command):
    p = subprocess.Popen(command.split())
    p.wait()
