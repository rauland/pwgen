from cgi import test
from logo import print_logo, clear_console, help_command
from colorama import Fore, Style, Back
from account import Account, Master
from csvgen import csvgen

def main():
    print(Fore.GREEN)
    clear_console()
    print_logo()
    print(Style.RESET_ALL + "Type -help for a list of commands!")
    # This creates a empty password list
    test_account = Master("admin@url.com.au","password")
    while True:
        startinput = input(Style.RESET_ALL+ "\nWhat would you like to do?:") #TODO Add rstrip() function to inputs
        if startinput == "-help":
            help_command()
            continue
        elif startinput == "-pwgen":
            csvgen()
        elif startinput == "-exit":
            exit()
        elif startinput == "-add":          
            test_account.addpw()
        elif startinput =="-show":
            test_account.showpw()
        else:
            print(Fore.RED + f"{startinput} is not a valid command, type -help for a list of valid commands")
            continue
main()
