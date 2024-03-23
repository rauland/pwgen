"""Export Module"""
import uuid
from colorama import Fore, Style
from pwgen import validate, generate

def generator():
    """Asks params for create"""
    length = validate.length_check("How many characters do you want your password to be?: ", 50)
    count = validate.length_check("How many passwords do you want to generate?: ", 99)
    answer = validate.prompt("Do you want to create a .csv file?: (Y / N) ")
    if answer:
        create(length, count)
    else:
        print(Fore.GREEN + f"Here are your randomly generated {length} character password(s):")
        for _ in range(count):
            print (Style.RESET_ALL+ generate.secret(length))
    input(Style.RESET_ALL + "Press enter to go back to the main menu")

def create(length = 0, count = 0, basefilename=r"csv-export\passwords", account_list=None):
    """Creates CSV file"""
    if account_list is None:
        account_list = []
    filename = f"{basefilename}-{str(uuid.uuid4())}.csv"
    if account_list == []:
        account_list = list(generate.secret(length)for i in range(count))
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
