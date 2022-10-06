from consolemenu import *
from consolemenu.items import *
import csvgen
from account import *
from pathlib import Path
from logo import print_logo

def exitmenu():
    exit()

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

    menu = ConsoleMenu(print_logo, show_exit_option=False)
    function_item = FunctionItem("Password generator", csvgen.generate) # Menu item for password generator
    function_item_1 = FunctionItem("Add password", account.addpw) #Menu item for adding password
    function_item_2 = FunctionItem("Show list of passwords", account.showpw) #Menu item for showing list of passwords
    function_item_3 = FunctionItem("Save account", account.save) #Menu item for saving account
    function_item_4 = FunctionItem("Export account", account.export_acc) #menu item for exporting account
    function_item_5 = FunctionItem("Exit", exitmenu) #exit program function

    # Adding item menu
    menu.append_item(function_item)
    menu.append_item(function_item_1)
    menu.append_item(function_item_2)
    menu.append_item(function_item_3)
    menu.append_item(function_item_4)
    menu.append_item(function_item_5)
    menu.show()

mainmenu()