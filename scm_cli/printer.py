# This is, designed to only work on my terminal, which has a black background.
# Planning on covering to a curses app to be able to control the look and feel.
import os

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
# Colorama options
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


def notify_starting_search():
    print(os.linesep + Style.BRIGHT + "hold on, I'll see if I can find that for you ..." + Back.RESET + os.linesep)


def display_options(repos):
    print(os.linesep + Style.BRIGHT + "Ok, here's what I got:")

    for index, repo in enumerate(repos):
        print((str(index+1) + '.').rjust(4) + ' ' + Style.BRIGHT + repo['name'] + Style.RESET_ALL + Fore.BLUE + ' (' + repo['host'] + ')')

    print('')
