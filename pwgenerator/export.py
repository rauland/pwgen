"""Export Module"""
import uuid
from colorama import Fore

def create(account_list=None, passwords_only=False,basefilename=r"csv-export\passwords"):
    """Creates CSV file"""
    if account_list is None:
        account_list = []
    filename = f"{basefilename}-{str(uuid.uuid4())}.csv"
    if passwords_only:
        with open(filename, "w", encoding="utf-8") as f:
            for row in account_list:
                for x in row:
                    f.write(str(x))
                f.write('\n')
        print(Fore.GREEN + f"{filename} has been created!")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            for acc in account_list:
                for x in f'URL: {acc.url}\nUsername: {acc.username}\nPassword: {acc.password}\n':
                    f.write(str(x))
                f.write('\n')
        print(Fore.GREEN + f"{filename} has been created!")
