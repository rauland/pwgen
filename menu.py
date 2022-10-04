from consolemenu import *
from consolemenu.items import *
from csvgen import csvgen
from account import Account, Master, load

def mainmenu():
    """Function for main menu"""

    # Creates a generic account if one is not found
    try:
        account = load()
    except OSError as e:
        account = Master("admin@url.com.au","password")

    menu = ConsoleMenu("PasswordGen", "A simple password manager made in python.")
    function_item = FunctionItem("Password Generator", csvgen) # Menu for password generator
    function_item_1 = FunctionItem("Add Password", account.addpw)

    # Adding item menu
    menu.append_item(function_item)
    menu.append_item(function_item_1) 
    menu.show()

mainmenu()