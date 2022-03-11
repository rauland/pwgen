import string, secrets, uuid, pwd
from logo import print_logo, clear_console, help_command
from colorama import Fore, Style, Back
from getpass import getpass

def main():
    print(Fore.GREEN)
    clear_console()
    print_logo()
    print(Style.RESET_ALL + "Type -help for a list of commands!")
    # This creates a empty password list
    password_list = []
    while True:
        startinput = input(Style.RESET_ALL+ "\nWhat would you like to do?:") #TODO Add rstrip() function to inputs
        if startinput == "-help":
            help_command()
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

def addpw(password_list =[]):
    """Creates password object, returns as list"""
    while True:
        url = input("What is the URL?:")
        username = input("What is the username?:")
        passwordgen = yes_no_prompt(f"Do you want to generate a random password for {url} (Y/N):")
        if passwordgen:
            pw = Passwordgen(length_pass=16)
            print(pw)
        else: 
            pw = pwinput()
        password_list += [pwd.Password(url,username,pw)]
        if not yes_no_prompt("Do you want to add another password? Y/n:"):
            break
    return password_list

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

def showpw(password_list = []):
    """Shows passwords, accepts password_list as param, default is [] if not param passed"""
    if password_list == []:
        print("No passwords have been added yet")
        return()
    for pwd in password_list:
        print(f'URL: {pwd.url}')
        print(f'Username: {pwd.username}')
        print(f'Password: {pwd.pw}')
        print(f'')

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

def pwgen_input():
    """Asks params for csvorgen"""
    while True:
        try:
            length_pass = int(input(Style.RESET_ALL + "How many characters do you want your password to be?: "))
            if length_pass > 50:
                raise Exception(f"{length_pass} is too long, it must be lower than 50")
            count_pass = int(input("How many passwords do you want to generate?: "))
            if count_pass > 99:
                raise Exception(f"{count_pass} is too many, it must be lower than 99")
            csv_answer = yes_no_prompt("Do you want to create a .csv file?: (Y / N) ")
        except Exception as e:
            print(Fore.RED + f"ERROR: {e} PLEASE TRY AGAIN!")
            continue
        else: 
            csvorgen(csv_answer, length_pass, count_pass)
            break

def Passwordgen(length_pass):
    """Generates password from length param"""
    chars = string.ascii_letters + "!@#$%^&*()" + string.digits
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

def csvcreate(Basefilename, length_pass, count_pass):
    """Creates CSV file"""
    filename = f"{Basefilename}-{str(uuid.uuid4())}.csv"
    password_list = list(Passwordgen(length_pass)for i in range(count_pass))
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
    print(Fore.GREEN + f"{filename} has been created!")

def csvorgen(csv_answer, length_pass, count_pass):
    """Accepts csv_answer, calls csvcreate or prints requested list based on answer"""
    if csv_answer:
        csvcreate("passwords", length_pass, count_pass),
    else:
        print(Fore.GREEN + f"Here are your randomly generated {length_pass} character password(s):")
        for i in range(count_pass):
            print (Style.RESET_ALL+ Passwordgen(length_pass))

main()
