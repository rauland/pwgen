import string
import secrets
import csv
import uuid
from colorama import Fore, Style, Back
from getpass import getpass

print("Type -help for a list of commands!")

def helpcommand():
    print(Back.GREEN + Fore.BLACK + "List of commands:" + Style.RESET_ALL)
    print(Style.RESET_ALL + "-help (List of Commands)")
    print("-pwgen (Password Generator)")
    print("-add (Add a password to password manager)")
    print("-exit (exits)")

def main():
    while True:
        startinput = input(Style.RESET_ALL+ "\nWhat would you like to do?:")
        if startinput == "-help":
            helpcommand()
            continue
        elif startinput == "-pwgen":
            pwgen_input()
        elif startinput == "-exit":
            exit()
        elif startinput == "-add":
            addpw()
        else:
            print(Fore.RED + f"{startinput} is not a valid command, type -help for a list of valid commands")
            continue

def addpw():
    while True:
        URL = input("What is the URL?:")
        Username = input("What is the username?:")
        PasswordGen = input(f"Do you want to generate a random password for {URL} (Y/N):")
        PasswordGenAnsw = str(PasswordGen).lower()
        if PasswordGenAnsw not in {"yes", "y", "no", "n"}:
            print(Fore.RED + f"{PasswordGenAnsw} is not a valid answer! Answer not yes/no")
        if PasswordGenAnsw == "yes" or PasswordGenAnsw == "y":
            print("placeholder")
            break
        if PasswordGenAnsw == "no" or PasswordGenAnsw == "n":
            pwinput()
            break

def pwinput():
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
            anothpw()

def anothpw():
    while True:
            AnotherPass = input(Style.RESET_ALL + "Do you want to add another password?")
            AnotherPassL = str(AnotherPass).lower()
            if AnotherPass not in {"yes", "y", "no", "n"}:
                print(Fore.RED + f"{AnotherPass} is not a valid response! Answer not yes/no")
            elif AnotherPass == "yes" or AnotherPass == "y":
                addpw()
            elif AnotherPass == "no" or AnotherPass == "n":
                main()


chars = string.ascii_letters + "!@#$%^&*()" + string.digits
Basefilename = "passwords"
CSVfiletag = ".csv"
Secondfilename = str(uuid.uuid4())
filename = f"{Basefilename}-{Secondfilename}{CSVfiletag}"


def pwgen_input():
    while True:
        try:
            global length, count, csvinput, csv_answer, length_pass, count_pass, count_pass_list
            length = input(Style.RESET_ALL + "How many characters do you want your password to be?: ")
            count = input("How many passwords do you want to generate?: ")
            csvinput = input("Do you want to create a .csv file?: (Y / N) ")
            count_pass = int(count)
            count_pass_list = list(count)
            length_pass = int(length)
            csv_answer = str(csvinput).lower()
            if csv_answer.isdigit():
                raise Exception(Fore.RED + "Answer not yes/no")
            if csv_answer not in {"yes", "y", "no", "n"}:
                raise Exception(Fore.RED + "Answer not yes/no")
        except Exception as e:
            print(Fore.RED + f"ERROR: {e} PLEASE TRY AGAIN!")
            continue
        else: 
            csvorgen()
            break

def Passwordgen():
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

def csvcreate():
    password_list = list(Passwordgen()for i in range(count_pass))
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
    print(Fore.GREEN + f"{filename} has been created!")
    (exit)

def csvorgen():
    if csv_answer == "y" or csv_answer == "yes":
        csvcreate()
    elif csv_answer == "n" or csv_answer == "no":
        print(Fore.GREEN + f"Here are your randomly generated {length} character password(s):")
        for i in range(count_pass):
            print (Style.RESET_ALL+ Passwordgen())
            (exit)

main()
