import uuid
from colorama import Fore, Style, Back
from pwgen import yes_no_prompt, pwinput, passwordgen

def csvgen():
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

def csvorgen(csv_answer, length_pass, count_pass):
    """Accepts csv_answer, calls csvcreate or prints requested list based on answer"""
    if csv_answer:
        csvcreate("passwords", length_pass, count_pass),
    else:
        print(Fore.GREEN + f"Here are your randomly generated {length_pass} character password(s):")
        for i in range(count_pass):
            print (Style.RESET_ALL+ passwordgen(length_pass))

def csvcreate(Basefilename, length_pass, count_pass):
    """Creates CSV file"""
    filename = f"csv-export\{Basefilename}-{str(uuid.uuid4())}.csv"
    account_list = list(passwordgen(length_pass)for i in range(count_pass))
    with open(filename, "w") as f:
        for row in account_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
    print(Fore.GREEN + f"{filename} has been created!")

