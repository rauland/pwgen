from etc import yes_no_prompt, pwinput, passwordgen

class Account:
  def __init__(self,username, password, url ='',email=''):
    self.username = username
    self.password = password
    self.url = url
    self.email = email

class Master:
  def __init__(self, email, password):
    Account.__init__(self, email, password)
    self.accounts = []

  def addpw(self):
    """Creates password object, returns as list"""
    while True:
        url = input("What is the URL?:")
        username = input("What is the username?:")
        password = yes_no_prompt(f"Do you want to generate a random password for {url} (Y/N):")
        if password:
            pw = passwordgen(length_pass=16)
            print(pw)
        else: 
            pw = pwinput()
        self.accounts += [Account(username,pw,url=url)]
        if not yes_no_prompt("Do you want to add another password? Y/n:"):
            break
    #return self.accounts

  def showpw(self):
    """Shows passwords, accepts account_list as param, default is [] if not param passed"""
    if self.accounts == []:
        print("No passwords have been added yet")
        return()
    for acc in self.accounts:
        print(f'URL: {acc.url}')
        print(f'Username: {acc.username}')
        print(f'Password: {acc.password}')
        print(f'')
