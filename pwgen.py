import string
import secrets
import csv
import uuid

while True:
    try:
        chars = string.ascii_letters + "!@#$%^&*()" + string.digits
        length = input("How many characters do you want your password to be?: ")
        count = input("How many passwords do you want to generate?: ")
        csvinput = (input("Do you want to create a .csv file?: (Y / N) "))
        count_pass = int(count)
        count_pass_list = list(count)
        length_pass = int(length)
        csv_answer = str(csvinput).lower()
        Basefilename = "passwords"
        Secondfilename = str(uuid.uuid4())
        CSVfiletag = ".csv"
        filename = f"{Basefilename}-{Secondfilename}{CSVfiletag}"
    except Exception as e:
        print("ERROR: (INVALID INPUT/S) PLEASE TRY AGAIN!")
        continue
    else: 
        break

def Passwordgen():
    password = "".join(secrets.choice(chars) for i in range(length_pass))
    return password

def csvcreate():
    with open(filename, "w") as f:
        for row in password_list:
            for x in row:
                f.write(str(x))
            f.write
    print(f"{filename} has been created!")
    (exit)

def csvorgen():
    if csv_answer == "y" or csv_answer == "yes":
        csvcreate()
    elif csv_answer == "n" or csv_answer == "no":
        for i in range(count_pass):
            print (Passwordgen())
            (exit)

password_list = list(Passwordgen()for i in range(count_pass))

csvorgen()