import string, secrets
from getpass import getpass
from colorama import Fore, Style

def prompt(answer):
    """Prompts and checks yes no check"""
    while True:
        check = input(Style.RESET_ALL + answer).lower()
        if check not in {"yes", "y", "no", "n"}:
            print(Fore.RED + f"{check} is not a valid response! Yes or no is expected")
        elif check == "yes" or check == "y":
            return True
        elif check == "no" or check == "n":
            return False

def pwinput():
    """Inputs and confirms custom password"""
    while True:
        Password = getpass(Style.RESET_ALL + "Enter your password:")
        PasswordCheck = str(Password)
        PasswordConfirm = getpass("Confirm your password:")
        if PasswordConfirm != (PasswordCheck):
            print(Fore.RED + "PASSWORD DOES NOT MATCH! PLEASE TRY AGAIN!")
            continue
        if PasswordConfirm == (PasswordCheck):
            print(Fore.GREEN + "Password has been added!")
            print(Style.RESET_ALL)
            return PasswordConfirm

def secretgen(length):
    """Generates password from length param"""
    chars = string.ascii_letters + "!@#$%^&*()" + string.digits
    password = "".join(secrets.choice(chars) for i in range(length))
    return password