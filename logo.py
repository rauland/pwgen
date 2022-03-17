import os
from colorama import Fore, Style, Back

def print_logo(colour = Fore.GREEN):
    logo = colour + """\n      
      :::::::::     :::       :::       ::::::::       ::::::::::       ::::    ::: 
     :+:    :+:    :+:       :+:      :+:    :+:      :+:              :+:+:   :+:  
    +:+    +:+    +:+       +:+      +:+             +:+              :+:+:+  +:+   
   +#++:++#+     +#+  +:+  +#+      :#:             +#++:++#         +#+ +:+ +#+    
  +#+           +#+ +#+#+ +#+      +#+   +#+#      +#+              +#+  +#+#+#     
 #+#            #+#+# #+#+#       #+#    #+#      #+#              #+#   #+#+#      
###             ###   ###         ########       ##########       ###    ####      
\n"""
    print(logo)
    Style.RESET_ALL

def clear_console():
    """Clears console, command on windows is 'cls', unix is 'clear'"""
    os.system('cls' if os.name == 'nt' else 'clear')    

def help_command():
    print(Back.GREEN + Fore.BLACK + "List of commands:" + Style.RESET_ALL)
    print(Style.RESET_ALL + "-help (List of Commands)")
    print("-pwgen (Password Generator)")
    print("-add (Add a password to password manager)")
    print("-show (Show list of passwords)")
    print("-save (Saves account)")
    print("-export (Export passwords to CSV)")
    print("-exit (exits)")