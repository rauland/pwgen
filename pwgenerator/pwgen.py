"""Common PWGEN Module"""
import string
import secrets
from colorama import Fore, Style
from export import create
from validate import validate

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

generate = Generate()
