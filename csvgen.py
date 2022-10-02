import uuid
from colorama import Fore, Style, Back
from pwgen import yes_no_prompt, pwinput, secretgen

def csvgen():
    """Asks params for csv_or_gen"""
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
            if csv_answer:
                csvcreate(length_pass, count_pass)
            else:
                print(Fore.GREEN + f"Here are your randomly generated {length_pass} character password(s):")
                for i in range(count_pass):
                    print (Style.RESET_ALL+ secretgen(length_pass))
            input("Press any key to go back to the menu")
            break

def csvcreate(length_pass = 0, count_pass = 0, Basefilename="csv-export\passwords", account_list =[]):
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