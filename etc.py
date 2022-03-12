from getpass import getpass
from colorama import Fore, Style, Back
import string, secrets, uuid

def yes_no_prompt(strprompt):
    """Prompts and checks yes no answer"""
    while True:
            pwanswer = input(Style.RESET_ALL + strprompt).lower()
            if pwanswer not in {"yes", "y", "no", "n"}:
                print(Fore.RED + f"{pwanswer} is not a valid response! Yes or no is expected")
            elif pwanswer == "yes" or pwanswer == "y":
                return True
            elif pwanswer == "no" or pwanswer == "n":
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

def passwordgen(length_pass):
    """Generates password from length param"""
    chars = string.ascii_letters + "!@#$%^&*()" + string.digits
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password