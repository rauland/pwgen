"""Account"""
from pathlib import Path
import pickle
import export
from validate import validate
from pwgen import generate

def load():
    """Loads existing account on first load"""
    # Creates folders if none exist
    Path("saved-accounts").mkdir(parents=True, exist_ok=True)
    Path("csv-export").mkdir(parents=True, exist_ok=True)
    # Creates a generic master account if one is not found
    try:
        savefile = r'saved-accounts\savefile.data'
        f = open(savefile, 'rb')
        account = pickle.load(f)
        f.close()
        return account
    except OSError:
        return Master("admin@url.com.au","password")

class Account:
    """Base Account"""
    def __init__(self, username, password, url='', email=''):
        self.username = username
        self.password = password
        self.url = url
        self.email = email

class Master(Account):
    """Extension of Account"""
    def __init__(self, email, password):
        super().__init__(self, email, password)
        self.ref = generate.secret(8)
        self.accounts = []

    def addpw(self):
        """Creates password object, returns as list"""
        while True:
            url = input("What is the URL?:")
            username = input("What is the username?:")
            password = validate.prompt(
                f"Do you want to generate a random password for {url} (Y/N):")
            if password:
                length = validate.length_check(
                    "How many characters do you want your password to be?: ", 50)
                pw = generate.secret(length=length)
                print(pw)
            else:
                pw = validate.input()
            self.accounts += [Account(username, pw, url)]
            if not validate.prompt("Do you want to add another password? Y/n:"):
                input("Press enter to go back to the main menu")
                break

    def showpw(self):
        """Shows passwords, accepts account_list as param, default is [] if no param passed"""
        if self.accounts == []:
            print("No passwords have been added yet")
            input("Press enter to go back to the main menu.")
            return ()
        for acc in self.accounts:
            print(f'URL: {acc.url}')
            print(f'Username: {acc.username}')
            print(f'Password: {acc.password}')
            print('')
        input("Press enter to go back to the main menu")

    def save(self,confirm = False):
        """Save Function"""
        savefile = r'saved-accounts\savefile.data'
        f = open(savefile, 'wb')
        pickle.dump(self, f)
        print("Account successfully saved, press enter to go back to menu")
        if not confirm:
            input()
        f.close()

    def export_acc(self):
        """Export Account as Object"""
        input("Account successfully exported, press enter to go back to menu")
        export.create(account_list=self.accounts,
                      basefilename=f"csv-export\Saved-ref-{self.ref}")
