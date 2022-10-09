import colorama
from colorama import Fore
COLORNAME = 'RED'
color = getattr(Fore, COLORNAME)
print(color + 'Hello')