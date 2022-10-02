from consolemenu import *
from consolemenu.items import *
from csvgen import csvgen

def mainmenu():
    """Function for main menu"""
    menu = ConsoleMenu("PasswordGen", "A simple password manager made in python.")
    function_item = FunctionItem("Password Generator", csvgen) # Menu for password generator

    # Adding item menu
    menu.append_item(function_item) 
    menu.show()

mainmenu()