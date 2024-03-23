"""Menu Module for PWGEN"""
from pathlib import Path
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from account import load, Master
from logo import print_logo
from colorama import Style
from pwgen import generate

def exitmenu():
    """Resets CLI style when existing"""
    print(Style.RESET_ALL + "Resetting Style")

def mainmenu():
    """Function for main menu"""
    # Creates a generic master account if one is not found
    try:
        account = load()
    except OSError:
        account = Master("admin@url.com.au","password")

    # Creates folders if none exist
    Path("saved-accounts").mkdir(parents=True, exist_ok=True)
    Path("csv-export").mkdir(parents=True, exist_ok=True)

    menu = ConsoleMenu(
        print_logo,
        epilogue_text="Tip: Type number to select menu item",
        show_exit_option=False)

    function_item = FunctionItem("Password generator", generate.many_secrets)
    function_item_1 = FunctionItem("Add password", account.addpw)
    function_item_2 = FunctionItem("Show list of passwords", account.showpw)
    function_item_3 = FunctionItem("Save account", account.save)
    function_item_4 = FunctionItem("Export account", account.export_acc)
    function_item_5 = FunctionItem("Exit", exitmenu, should_exit=True)

    # Adding item menu
    menu.append_item(function_item)
    menu.append_item(function_item_1)
    menu.append_item(function_item_2)
    menu.append_item(function_item_3)
    menu.append_item(function_item_4)
    menu.append_item(function_item_5)
    menu.show()
