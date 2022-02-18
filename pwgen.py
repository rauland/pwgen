import string
import secrets
import csv
import uuid
from colorama import Fore, Style, Back

print("Type -help for a list of commands!")

def helpcommand():
    print(Back.GREEN + Fore.BLACK + "List of commands:" + Style.RESET_ALL)
    print(Style.RESET_ALL + "-help (List of Commands)")
    print("-pwgen (Password Generator)")

while True:
    startinput = input(Style.RESET_ALL+ "\nWhat would you like to do?:")
    if startinput == "-help":
        helpcommand()
        continue
    elif startinput == "-pwgen":
        break
    else:
        print(Fore.RED + f"{startinput} is not a valid command, type -help for a list of valid commands")
        continue

chars = string.ascii_letters + "!@#$%^&*()" + string.digits
Basefilename = "passwords"
CSVfiletag = ".csv"
Secondfilename = str(uuid.uuid4())
filename = f"{Basefilename}-{Secondfilename}{CSVfiletag}"

def csvERROR():
    if csv_answer.isdigit():
        raise Exception(Fore.RED + "Answer not yes/no")
    if csv_answer not in {"yes", "y", "no", "n"}:
        raise Exception(Fore.RED + "Answer not yes/no")

while True:
    try:
        length = input(Style.RESET_ALL + "How many characters do you want your password to be?: ")
        count = input("How many passwords do you want to generate?: ")
        csvinput = input("Do you want to create a .csv file?: (Y / N) ")
        count_pass = int(count)
        count_pass_list = list(count)
        length_pass = int(length)
        csv_answer = str(csvinput).lower()
        csvERROR()
    except Exception as e:
        print(Fore.RED + f"ERROR: {e} PLEASE TRY AGAIN!")
        continue
    else: 
        break

def Passwordgen():
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

def csvcreate():
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
    print(f"{filename} has been created!")
    (exit)

def csvorgen():
    if csv_answer == "y" or csv_answer == "yes":
        csvcreate()
    elif csv_answer == "n" or csv_answer == "no":
        print(Fore.GREEN + f"Here is your randomly generated {length} character password(s):")
        for i in range(count_pass):
            print (Style.RESET_ALL+ Passwordgen())
            (exit)

password_list = list(Passwordgen()for i in range(count_pass))

csvorgen()