from pickle import TRUE
import string
import secrets
import csv
from tkinter import FALSE
import uuid
import os
from colorama import Fore, Style, Back
from getpass import getpass

# Clears console, command on windows is 'cls', unix is 'clear'
os.system('cls' if os.name == 'nt' else 'clear')

# This prints the logo of PWgen, after the console clear. Hard-coded but eh.
print(Fore.GREEN + """\n      
      :::::::::     :::       :::       ::::::::       ::::::::::       ::::    ::: 
     :+:    :+:    :+:       :+:      :+:    :+:      :+:              :+:+:   :+:  
    +:+    +:+    +:+       +:+      +:+             +:+              :+:+:+  +:+   
   +#++:++#+     +#+  +:+  +#+      :#:             +#++:++#         +#+ +:+ +#+    
  +#+           +#+ +#+#+ +#+      +#+   +#+#      +#+              +#+  +#+#+#     
 #+#            #+#+# #+#+#       #+#    #+#      #+#              #+#   #+#+#      
###             ###   ###         ########       ##########       ###    ####      
\n""")

print(Style.RESET_ALL + "Type -help for a list of commands!")

def helpcommand():
    print(Back.GREEN + Fore.BLACK + "List of commands:" + Style.RESET_ALL)
    print(Style.RESET_ALL + "-help (List of Commands)")
    print("-pwgen (Password Generator)")
    print("-add (Add a password to password manager)")
    print("-exit (exits)")

# TODO: Do we need '-' before a menu item, for example -help. Why not use help?
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
#  addpw()
def addpw():
    while True:
        URL = input("What is the URL?:")
        Username = input("What is the username?:")
        PasswordGen = pw_prompt(f"Do you want to generate a random password for {URL} (Y/N):")
        if PasswordGen:
            print("placeholder")
            break
        else:
            pwinput()
            if not pw_prompt("Do you want to add another password?"):
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
            break

def pw_prompt(question):
    while True:
            pwanswer = input(Style.RESET_ALL + question)
            if pwanswer not in {"yes", "y", "no", "n"}:
                print(Fore.RED + f"{pwanswer} is not a valid response! Answer not yes/no")
            elif pwanswer == "yes" or pwanswer == "y":
                return TRUE
            elif pwanswer == "no" or pwanswer == "n":
                return FALSE

# TODO: Code sitting outside of a function
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

# TODO: Pass length_pass as a over write-able parameter
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

# TODO: Pass csv_answer as a parameter
def csvorgen():
    if csv_answer == "y" or csv_answer == "yes":
        csvcreate()
    elif csv_answer == "n" or csv_answer == "no":
        print(Fore.GREEN + f"Here are your randomly generated {length} character password(s):")
        for i in range(count_pass):
            print (Style.RESET_ALL+ Passwordgen())
            (exit)

main()
