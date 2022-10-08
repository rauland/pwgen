import uuid
from colorama import Fore, Style
from pwgen import prompt, secretgen

def lencheck(question, max):
    """Checks length of string based off max value"""
    while True:
        try:
            answer = int(input(Style.RESET_ALL+question))
            if answer > max:
                raise Exception(f"{answer} is too many, it must be less than {max}")
        except Exception or UnboundLocalError as e:
            print(Fore.RED + f"ERROR: {e} PLEASE TRY AGAIN!")
            continue
        return answer

def generator():
    """Asks params for create"""
    length = lencheck("How many characters do you want your password to be?: ", 50)
    count = lencheck("How many passwords do you want to generate?: ", 99)
    answer = prompt("Do you want to create a .csv file?: (Y / N) ")
    if answer:
        create(length, count)
    else:
        print(Fore.GREEN + f"Here are your randomly generated {length} character password(s):")
        for c in range(count):
            print (Style.RESET_ALL+ secretgen(length))
    input("Press enter to go back to the main menu")

def create(length_pass = 0, count_pass = 0, Basefilename="csv-export\passwords", account_list =[]):
    """Creates CSV file"""
    filename = f"{Basefilename}-{str(uuid.uuid4())}.csv"
    if account_list == []:
        account_list = list(secretgen(length_pass)for i in range(count_pass))
        with open(filename, "w") as f:
            for row in account_list:
                for x in row:
                    f.write(str(x))
                f.write('\n')
        print(Fore.GREEN + f"{filename} has been created!")
    else:
        with open(filename, "w") as f:
            for acc in account_list:
                for x in 'URL: ',acc.url,'\nUsername: ',acc.username,'\nPassword: ',acc.password,'\n':
                    f.write(str(x))
                f.write('\n')
        print(Fore.GREEN + f"{filename} has been created!")
