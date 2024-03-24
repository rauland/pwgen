"""Common PWGEN Module"""
import string
import secrets
from getpass import getpass
from colorama import Fore, Style
from export import create

class Validate:
    """Input Class"""
    def prompt(self, answer):
        """Prompts and checks yes no check"""
        while True:
            check = input(Style.RESET_ALL + answer).lower()
            if check not in {"yes", "y", "no", "n"}:
                print(Fore.RED + f"{check} is not a valid response! Yes or no is expected")
            elif check == "yes" or check == "y":
                return True
            elif check == "no" or check == "n":
                return False

    def length_check(self, question, max_length):
        """Checks length of string based off max_length value"""
        while True:
            try:
                answer = int(input(Style.RESET_ALL+question))
                if answer > max_length:
                    raise ValueError(f"{answer} is too long, it must be less than {max_length}")
            except ValueError:
                print(Fore.RED + f"ERROR: {ValueError} PLEASE TRY AGAIN!")
                continue
            return answer

    def input(self):
        """Inputs and confirms custom password"""
        while True:
            password = getpass(Style.RESET_ALL + "Enter your password:")
            password_check = str(password)
            password_confirm = getpass("Confirm your password:")
            if password_confirm != (password_check ):
                print(Fore.RED + "PASSWORD DOES NOT MATCH! PLEASE TRY AGAIN!")
                continue
            if password_confirm == (password_check ):
                print(Fore.GREEN + "Password has been added!")
                print(Style.RESET_ALL)
                return password_confirm

class Generate:
    """Generate Secrets"""
    def secret(self, length):
        """Generates password from length param"""
        chars = string.ascii_letters + "!@#$%^&*()" + string.digits
        password = "".join(secrets.choice(chars) for i in range(length))
        return password

    def many_secrets(self,length=None,count=None,answer=None,gui=None):
        """Asks params for create"""
        if length is None:
            length = validate.length_check("How many characters do you "
                                           "want the password to be?: ", 50)
        if count is None:
            count = validate.length_check("How many passwords do you want "
                                          "to generate?: ", 99)
        if answer is None:
            answer = validate.prompt("Do you want to create a .csv file?: (Y / N) ")
        if answer:
            account_list = list(generate.secret(length)for _ in range(count))
            create(account_list, True)
        else:
            print(Fore.GREEN + f"Here are your randomly generated {length} character password(s):")
            for _ in range(count):
                print (Style.RESET_ALL+ generate.secret(length))
        if gui:
            return list(generate.secret(length)for _ in range(count))
        else:
            input(Style.RESET_ALL + "Press enter to go back to the main menu")


validate = Validate()
generate = Generate()
