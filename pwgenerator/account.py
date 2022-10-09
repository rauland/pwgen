from pwgen import prompt, pwinput, secretgen
import export
import pickle

def load():
  savefile = 'saved-accounts\savefile.data'
  f = open(savefile,'rb')
  account = pickle.load(f)
  f.close()
  return account

class Account:
  def __init__(self,username, password, url ='',email=''):
    self.username = username
    self.password = password
    self.url = url
    self.email = email

class Master:
  def __init__(self, email, password):
    self.ref = secretgen(8)
    Account.__init__(self, email, password)
    self.accounts = []

  def addpw(self):
    """Creates password object, returns as list"""
    while True:
        url = input("What is the URL?:")
        username = input("What is the username?:")
        password = prompt(f"Do you want to generate a random password for {url} (Y/N):")
        if password:
            pw = secretgen(length=16)
            print(pw)
        else: 
            pw = pwinput()
        self.accounts += [Account(username,pw,url)]
        if not prompt("Do you want to add another password? Y/n:"):
            input("Press enter to go back to the main menu")
            break

  def showpw(self):
    """Shows passwords, accepts account_list as param, default is [] if no param passed"""
    if self.accounts == []:
        print("No passwords have been added yet")
        input("Press enter to go back to the main menu.")
        return()
    for acc in self.accounts:
        print(f'URL: {acc.url}')
        print(f'Username: {acc.username}')
        print(f'Password: {acc.password}')
        print(f'')
    input("Press enter to go back to the main menu")

  def save(self):
    savefile = 'saved-accounts\savefile.data'
    f = open(savefile, 'wb')
    pickle.dump(self, f)
    input("Account successfully saved, press enter to go back to menu")
    f.close

  def export_acc(self):
    input("Account successfully exported, press enter to go back to menu")
    export.create(account_list = self.accounts,Basefilename=f"csv-export\Saved-ref-{self.ref}")