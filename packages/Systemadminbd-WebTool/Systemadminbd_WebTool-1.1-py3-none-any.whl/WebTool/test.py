# -*- coding: utf-8 -*-
import asyncio
import os
import rich
import time
import platform
import uuid
import hashlib
import webbrowser
import requests
from rich.console import Console
from rich.progress import Progress
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Importing functions from custom modules
from .proxyGrabber import main as pxg
from .domainGrabbere import main as dg
from .cms import main as cms
from .reverIpe import main as rev
from .WordpressExploit import main as exploit
from .spider import main as spider

# Constants and settings
BANNER = """
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝██║  ██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██╗██║  ██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝██████╔╝
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═════╝
"""
OPTIONS = {
    "1": ("Reverse IP", rev),
    "2": ("Domain grabber", dg),
    "3": ("Premium proxy Grabber", pxg),
    "4": ("Cms detector", cms),
    "5": ("Wordpress exploiter", exploit),
    "6": ("Download websites all files and folders [except some files]", spider)
}

# Foreground colors and styles
FR = Fore.RED
FG = Fore.GREEN
FY = Fore.YELLOW
FC = Fore.CYAN
FW = Fore.WHITE
SB = Style.BRIGHT

def get_centered(center, message):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(message)) // 2
    centered_message = f"{' ' * padding}{message}{' ' * padding}" if center else message
    os.system(f"echo \"{centered_message}\" | lolcat")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"echo \"\"\"{BANNER}\"\"\" | lolcat")
    get_centered(True, "Coded By Systemadminbd")

def print_text_slowly(text, speed=0.03):
    for char in text:
        print(FC + SB + char, end='', flush=True)
        time.sleep(speed)

def open_telegram():
    telegram_link = "https://t.me/systemadminbdbot"
    webbrowser.open(telegram_link)

async def main_menu():
    while True:
        clear()
        print(f"{SB + FC}Select an option:\n")
        for key, (description, _) in OPTIONS.items():
            print(f"{SB + FG}{key}. {description}")

        choice = input(f"{SB + FY}\nEnter the number of your choice: {Fore.RESET}")

        if choice in OPTIONS:
            print("\n\n")
            description, func = OPTIONS[choice]

            if choice in ["4", "5"]:  # 'cms' and 'exploit' are not asynchronous
                func()
            else:
                await func()
            break
        else:
            print(f"{SB + FR}Invalid choice, please try again.{Fore.RESET}")

def verify_hardware_id(hardware_id):
    try:
        api = requests.get("https://raw.githubusercontent.com/ABIRHOSSAIN10/Email-bombing/main/Key.txt").text
        return hardware_id in api
    except Exception:
        return None

def generate_hardware_id():
    system_info = platform.uname()
    unique_string = f"{system_info.node}{system_info.processor}{system_info.system}{platform.machine()}{platform.platform()}"
    return hashlib.sha256(unique_string.encode()).hexdigest()

async def print_option():
    console = Console()
    clear()
    pr = f"{SB + FC}Select an option:\n"
    os.system(f"echo \"{pr}\" | lolcat")
    for key, (description, _) in OPTIONS.items():
        os.system(f"echo \"{key}. {description}\" | lolcat")
    print("\n\n")
    get_centered(True, "You don't have enough permission to proceed")
    print("\n\n")
    with Progress() as progress:
        task = progress.add_task("[bold cyan]Verifying license key...", total=100)
        for _ in range(100):
            time.sleep(0.005)
            progress.update(task, advance=1)

async def main():
    hardware_id = generate_hardware_id()
    verification_result = verify_hardware_id(hardware_id)
    if verification_result:
        print(f"\n{FY}{SB}Verification Result Status: {FG}{SB}Verified")
        await main_menu()
    else:
        await print_option()
        print(f"\n{FY}{SB}Verification Result Status: {FR}{SB}Not Verified")
        print(f"\n{FG}{SB}Your License key is: {SB}{FW}{hardware_id}")
        print_text_slowly(f"\nPlease verify your License Key.\n")
        print_text_slowly("\nContact the author on Telegram to get verified. [https://t.me/systemadminbdbot]\n")
        open_telegram()

def async_main():
    asyncio.run(main())

if __name__ == "__main__":
    async_main()