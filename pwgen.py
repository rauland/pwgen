import string
import secrets
import csv
import uuid

while True:
    try:
        chars = string.ascii_letters + "!@#$%^&*()" + string.digits
        length = input("How many characters do you want your password to be?: ")
        count = input("How many passwords do you want to generate?: ")
        count_pass = int(count)
        count_pass_list = list(count)
        length_pass = int(length)
        break
    except ValueError:
        print("ERROR: (INVALID INPUT) USE INTERGERS ONLY! PLEASE TRY AGAIN!")

def Passwordgen():
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

password_list = list(Passwordgen()for i in range(count_pass))


csv = input("Do you want to create a .csv file?: (Y / N) ")
csv_answer = str(csv).lower()
if csv_answer == "y" or csv_answer == "yes":
    Basefilename = "passwords"
    Secondfilename = str(uuid.uuid4())
    CSVfiletag = ".csv"
    filename = f"{Basefilename}-{Secondfilename}{CSVfiletag}"
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write('\n')
        print(f"{filename} has been created!")
elif csv_answer == "n" or csv_answer == "no":
    for i in range(count_pass):
        print (Passwordgen())
else:
    print ("ERROR: (INVALID INPUT) YES/NO ONLY! PLEASE TRY AGAIN!")
    (exit)