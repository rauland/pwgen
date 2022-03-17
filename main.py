from logo import print_logo, clear_console, help_command
from colorama import Fore, Style, Back
from account import Account, Master, load
from csvgen import csvgen

def main():
    clear_console()
    print_logo(Fore.RED)
    print(Style.RESET_ALL + "Type -help for a list of commands!")
    
    # Creates a generic account if one is not found
    try:
        account = load()
    except OSError as e:
        account = Master("admin@url.com.au","password")
        
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
            account.addpw()
        elif startinput =="-show":
            account.showpw()
        elif startinput =="-save":
            account.save()
        elif startinput =="-export":
            account.export_acc()    
        else:
            print(Fore.RED + f"{startinput} is not a valid command, type -help for a list of valid commands")
            continue
main()
