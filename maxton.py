#!/usr/bin/env python3
import os
import time
import subprocess

# Color codes
g = '\033[1;92m'  # green
c = '\033[1;96m'  # cyan
y = '\033[1;93m'  # yellow
r = '\033[1;91m'  # red
b = '\033[1;94m'  # blue
n = '\033[0m'     # reset

# Banner Function
def show_banner():
    os.system('clear')
    print(f"""{y}███╗   ███╗ █████╗ ██╗  ██╗████████╗ ██████╗ ███╗   ██╗
{r}████╗ ████║██╔══██╗╚██╗██╔╝╚══██╔══╝██╔═══██╗████╗  ██║
{g}██╔████╔██║███████║ ╚███╔╝    ██║   ██║   ██║██╔██╗ ██║
{c}██║╚██╔╝██║██╔══██║ ██╔██╗    ██║   ██║   ██║██║╚██╗██║
{b}██║ ╚═╝ ██║██║  ██║██╔╝ ██╗   ██║   ╚██████╔╝██║ ╚████║
{b}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝{n}""")
    print()
    print(f"{g}        Anonymous Cyber Shield")
    print(f"{c}        Created By {g}Robert Maxton{n}\n")

# Telegram Open
def open_telegram():
    os.system("xdg-open https://t.me/maxtonxbot_bot")
    time.sleep(3)

# Termux Full Setup
def termux_full_setup():
    os.system('clear')
    print(f"{y}Starting Full Setup... Please wait{n}")
    time.sleep(1)

    commands = [
        "pkg update -y && pkg upgrade -y",
        "pkg install -y git python zsh curl ruby figlet termux-api ncurses-utils jq exa",
        "pip install lolcat"
    ]

    for cmd in commands:
        subprocess.call(cmd, shell=True)

    print(f"{g}All packages installed successfully!{n}")
    time.sleep(2)

# Banner Setup
def banner_setup():
    maxton_path = os.path.expanduser("~/maxton.sh")
    if os.path.exists(maxton_path):
        subprocess.call(f"bash {maxton_path}", shell=True)
    else:
        print(f"{r}[×] maxton.sh not found in your HOME directory.{n}")
        time.sleep(2)

# Menu Loop
def main_menu():
    while True:
        show_banner()
        print(f"{r}[1]{g} Termux Full Setup")
        print(f"{r}[2]{g} Termux Banner Setup")
        print(f"{r}[0]{g} Exit\n")
        choice = input(f"{c}Select an option: {n}")

        if choice == '1':
            termux_full_setup()
        elif choice == '2':
            banner_setup()
        elif choice == '0':
            print(f"{g}Exiting...{n}")
            break
        else:
            print(f"{r}Invalid choice! Try again...{n}")
            time.sleep(1)

# Script start
if __name__ == "__main__":
    open_telegram()
    main_menu()
