from consolemenu import *
from consolemenu.items import *
import csvgen
from account import *
from logo import *
from pathlib import Path

def mainmenu():
    """Function for main menu"""

    # Creates a generic master account if one is not found
    try:
        account = load()
    except OSError as e:
        account = Master("admin@url.com.au","password")    

    # Creates folders if none exist
    Path("saved-accounts").mkdir(parents=True, exist_ok=True)
    Path("csv-export").mkdir(parents=True, exist_ok=True)

    menu = ConsoleMenu(print_logo)
    function_item = FunctionItem("Password generator", csvgen.generate) # Menu for password generator
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