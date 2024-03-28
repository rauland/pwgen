"""GUI Module for PWGEN"""
import ttkbootstrap as ttk
# from ttkbootstrap.constants import BOTH, YES
from account import load, Account
from pwgen import generate

class App():
    """APP GUI Class"""
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("PWGEN")
        self.root.geometry("640x480")
        # Create Menubar
        menubar = Menubar(self.root)
        self.root.config(menu=menubar)
        # Layout
        tabs = ttk.Frame(self.root, width=64)
        tabs.grid(row=0, column=0)
        tabs.pack(side="left",fill="y")

        button1 = ttk.Button(tabs, text="Gen",
                            command=lambda: self.show_frame("PwgenForm"),bootstyle="secondary", width=6)
        button2 = ttk.Button(tabs, text="Add",
                            command=lambda: self.show_frame("AddForm"),bootstyle="secondary", width=6)
        button3 = ttk.Button(tabs, text="Show",
                            command=lambda: self.show_frame("ShowList"),bootstyle="secondary", width=6)
        button4 = ttk.Button(tabs, text="Save",
                            command=save,bootstyle="secondary", width=6)
        button5 = ttk.Button(tabs, text="Export",
                            command=lambda: self.show_frame("PwgenForm"),bootstyle="secondary", width=6)
        side_butpad={'ipady': 8, 'padx': 1, 'pady': 1}
        button1.pack(side_butpad)
        button2.pack(side_butpad)
        button3.pack(side_butpad)
        button4.pack(side_butpad)
        button5.pack(side_butpad)

        seperator = ttk.Frame(self.root, bootstyle="secondary", width=1, borderwidth=1, relief="sunken")
        seperator.pack(side="left", fill="y")

        # Container
        container = ttk.Frame(self.root, padding=10)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Select Frames
        self.frames = {}
        for F in (PwgenForm, AddForm, ShowList):
            page_name = F.__name__
            frame = F(master=container,controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PwgenForm")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        """Run the GUI"""
        self.root.mainloop()

class Menubar(ttk.Menu):
    """menubar GUI class"""
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        filemenu = ttk.Menu(self, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        self.add_cascade(label="File", menu=filemenu)

class PwgenForm(ttk.Frame):
    """pwgen GUI form"""
    def __init__(self, master, *args, controller=None, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.controller = controller
        # Set border properties
        # self.configure(borderwidth=2,relief="solid")

        # register the validation callback
        digit_func = self.register(validate.number)
        # alpha_func = self.register(validate.alpha)

        self.l1 = ttk.Label(self, text="Password Generator", font=("Helvetica", 16))
        self.l1.pack(pady=10)

        self.l2 = ttk.Label(self, text="Enter the password length", font=("Helvetica", 10))
        self.l2.pack(pady=10)
        self.e1 = ttk.Spinbox(self,
            bootstyle="primary",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0,
            to=100)

        self.e1.pack(pady=10)
        self.l3 = ttk.Label(self,
            text="How many passwords?",
            font=("Helvetica", 10))

        self.l3.pack(pady=10)
        self.c1 = ttk.Spinbox(self,
            bootstyle="primary",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0,
            to=100)
        self.c1.pack(pady=10)

        self.b1 = ttk.Button(self,
            text="Submit",
            bootstyle="primary",
            command=lambda: generate_set(self.e1.get(),self.c1.get(),self.l4))
        self.b1.pack(padx=5, pady=10)

        self.l4 = ttk.Text(self)
        self.l4.insert(1.0, "Output goes here...")
        self.l4.configure(state="disabled", width=72)
        self.l4.pack(side="left", fill="both", expand=True)

        # Scrollbar attached to the l4 text widget
        self.scrollbar = ttk.Scrollbar(self.l4 , command=self.l4.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.l4.config(yscrollcommand=self.scrollbar.set)

        # button1 = ttk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        # button2 = ttk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button1.pack()
        # button2.pack()

class AddForm(ttk.Frame):
    """Add Form Frame"""
    def __init__(self, master, controller=None):
        ttk.Frame.__init__(self, master)
        self.controller = controller

        self.l1 = ttk.Label(self, text="Add Account", font=("Helvetica", 16))
        self.l1.pack(pady=12)

        self.l2 = ttk.Label(self, text="URL:", font=("Helvetica", 10))
        self.l2.pack(pady=6)
        self.e2 = ttk.Entry(self)
        self.e2.pack(pady=6)

        self.l3 = ttk.Label(self, text="Username:", font=("Helvetica", 10))
        self.l3.pack(pady=6)
        self.e3 = ttk.Entry(self)
        self.e3.pack(pady=6)

        self.l4 = ttk.Label(self, text="Password:", font=("Helvetica", 10))
        self.l4.pack(pady=6)
        self.e4 = ttk.Entry(self)
        self.e4.pack(pady=6)

        self.b1 = ttk.Button(self,
        text="Submit",
        bootstyle="primary",
        command=lambda: add(self.e2.get(),self.e3.get(),self.e4.get()))
        self.b1.pack(padx=5, pady=10)

class ShowList(ttk.Frame):
    """Show List Frame"""
    def __init__(self, master, controller=None):
        ttk.Frame.__init__(self, master)
        self.controller = controller

        self.l1 = ttk.Label(self, text="Saved Accounts", font=("Helvetica", 16))
        self.l1.pack(pady=12)

        self.l4 = ttk.Text(self)
        # self.l4.insert(1.0, "Output goes here...")
        # self.l4.configure(state="disabled", width=72)

        show(self.l4)

class Validate():
    """GUI Field Validation"""
    def number(self, x) -> bool:
        """Validates that the input is a number"""
        if x.isdigit():
            if int(x) <= 100:
                return True
            else: return False
        elif x == "":
            return True
        else:
            return False
    def alpha(self, x) -> bool:
        """Validates that the input is alpha"""
        if x.isdigit():
            return False
        elif x == "":
            return True
        else:
            return True

validate = Validate()

def generate_set(length, count, text):
    """Sets output for GUI"""
    if validate.number(length) and validate.number(count):
        output = generate.many_secrets(int(length),int(count),False,True)
        output = '\n'.join(output)
    else:
        output = "Error: No Characters or Length or Amount over 100"
    text.configure(state="normal")
    text.delete(1.0, "end")
    text.insert(1.0, output)
    text.configure(state="disabled")

def show(label):
    if account.accounts == []:
        label.insert(1.0, "No passwords have been added yet")
    else:
        output = ""
        for acc in account.accounts:
            output += f'URL: {acc.url}\n'
            output += f'Username: {acc.username}\n'
            output += f'Password: {acc.password}\n'
            output += '\n'
        label.insert(1.0, output)

    label.configure(state="disabled", width=72)
    label.pack(side="left", fill="both", expand=True)

def add(url,user,pw):
    account.accounts += [Account(user, pw, url)]

def save():
    account.save(True)

if __name__ == "__main__":
    account = load()
    app = App()
    app.run()
