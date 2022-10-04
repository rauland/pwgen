from consolemenu import *
from consolemenu.items import *
from csvgen import csvgen
from account import *

def mainmenu():
    """Function for main menu"""

    # Creates a generic account if one is not found
    try:
        account = load()
    except OSError as e:
        account = Master("admin@url.com.au","password")

    menu = ConsoleMenu("PasswordGen", "A simple password manager made in python.")
    function_item = FunctionItem("Password generator", csvgen) # Menu for password generator
    function_item_1 = FunctionItem("Add password", account.addpw)
    function_item_2 = FunctionItem("Show list of passwords", account.showpw)
    function_item_3 = FunctionItem("Save account", account.save)
    function_item_4 = FunctionItem("Export account", account.export_acc)

    # Adding item menu
    menu.append_item(function_item)
    menu.append_item(function_item_1)
    menu.append_item(function_item_2)
    menu.append_item(function_item_3)
    menu.append_item(function_item_4)
    menu.show()

mainmenu()