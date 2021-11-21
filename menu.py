import ipdb
import os
import colorama
from colorama import Fore, Style

genConf = """
1. Redundancy
2. Vlans
3. TACACS and RADIUS
4. HTTP and SSH \n
"""

conf = """
50. Option
...
tbd
...\n\n
"""


def c_print(printMe):
    """
    Prints text centered on screen

    printMe : Text to be written, type str
    """
    print(f"\n{printMe.center(70,)}\n")


def main():
    os.system('clear')
    choice = int()
    print("\n")
    print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
    c_print("Welcome to " + Fore.BLUE + "The Menu" + Style.RESET_ALL)

    print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
    print("\n")
    print(Fore.YELLOW + Style.BRIGHT +
          "GENERATE CONFIGS" + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + genConf + Style.RESET_ALL)

#    print(Fore.YELLOW + Style.BRIGHT +
#          "CONFIGURE" + Style.RESET_ALL)
#    print(Fore.BLUE + Style.BRIGHT + conf + Style.RESET_ALL)

    choice = input("Please enter your choice (1 for now) : ")


if __name__ == "__main__":
    main()
