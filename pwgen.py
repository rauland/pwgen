import string
import secrets
import csv
import uuid
import os
import pwobj
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
    print("-show (Show list of passwords)")
    print("-exit (exits)")

def main():
    password_list = []
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
            password_list = addpw(password_list)
        elif startinput =="-show":
            showpw(password_list)
        else:
            print(Fore.RED + f"{startinput} is not a valid command, type -help for a list of valid commands")
            continue

# Creates password object, returns as list 
def addpw(password_list =[]):
    while True:
        url = input("What is the URL?:")
        username = input("What is the username?:")
        passwordgen = yes_no_prompt(f"Do you want to generate a random password for {url} (Y/N):")
        if passwordgen:
            pw = Passwordgen(length_pass=16)
            print(pw)
        else: 
            pw = pwinput()
        password_list = password_list + [pwobj.Password(url,username,pw)]
        if not yes_no_prompt("Do you want to add another password?"):
            break
    return password_list

# Inputs and confirms custom password
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
            return PasswordConfirm

# Shows passwords, accepts password_list as param, default is [] if not param passed
def showpw(password_list = []):
    if password_list == []:
        print("No passwords have been added yet")
        return()
    for i in range(len(password_list)):
        print(password_list[i].url)
        print(password_list[i].username)
        print(password_list[i].pw)

# Prompts and checks yes no answer
def yes_no_prompt(strprompt):
    while True:
            pwanswer = input(Style.RESET_ALL + strprompt).lower()
            if pwanswer not in {"yes", "y", "no", "n"}:
                print(Fore.RED + f"{pwanswer} is not a valid response! Yes/No expected")
            elif pwanswer == "yes" or pwanswer == "y":
                return True
            elif pwanswer == "no" or pwanswer == "n":
                return False

def pwgen_input():
    while True:
        try:
            length_pass = int(input(Style.RESET_ALL + "How many characters do you want your password to be?: "))
            count_pass = int(input("How many passwords do you want to generate?: "))
            csv_answer = yes_no_prompt("Do you want to create a .csv file?: (Y / N) ")
        except Exception as e:
            print(Fore.RED + f"ERROR: {e} PLEASE TRY AGAIN!")
            continue
        else: 
            csvorgen(csv_answer, length_pass, count_pass)
            break

def Passwordgen(length_pass):
    chars = string.ascii_letters + "!@#$%^&*()" + string.digits
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

def csvcreate(Basefilename, length_pass, count_pass):
    filename = f"{Basefilename}-{str(uuid.uuid4())}.csv"
    password_list = list(Passwordgen(length_pass)for i in range(count_pass))
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
    print(Fore.GREEN + f"{filename} has been created!")

def csvorgen(csv_answer, length_pass, count_pass):
    if csv_answer:
        csvcreate("passwords", length_pass, count_pass),
    else:
        print(Fore.GREEN + f"Here are your randomly generated {length_pass} character password(s):")
        # TODO: I in range not used
        for i in range(count_pass):
            print (Style.RESET_ALL+ Passwordgen(length_pass))

main()
