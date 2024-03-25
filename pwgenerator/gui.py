"""GUI Module for PWGEN"""
import ttkbootstrap as ttk
# from ttkbootstrap.constants import BOTH, YES
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
                            command=lambda: self.show_frame("PageOne"),bootstyle="secondary", width=6)
        button3 = ttk.Button(tabs, text="Show",
                            command=lambda: self.show_frame("PageTwo"),bootstyle="secondary", width=6)
        button4 = ttk.Button(tabs, text="Save",
                            command=lambda: self.show_frame("PageOne"),bootstyle="secondary", width=6)
        button5 = ttk.Button(tabs, text="Export",
                            command=lambda: self.show_frame("PageTwo"),bootstyle="secondary", width=6)
        button1.pack(side="top")
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

        seperator = ttk.Frame(self.root, bootstyle="secondary", width=1, borderwidth=1, relief="sunken")
        seperator.pack(side="left", fill="y")

        # Container
        container = ttk.Frame(self.root, padding=10)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Select Frames
        self.frames = {}
        for F in (PwgenForm, PageOne, PageTwo):
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

validate = Validate()

class PageOne(ttk.Frame):

    def __init__(self, master, controller=None):
        ttk.Frame.__init__(self, master)
        self.controller = controller
        label = ttk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PwgenForm"))
        button.pack()


class PageTwo(ttk.Frame):

    def __init__(self, master, controller=None):
        ttk.Frame.__init__(self, master)
        self.controller = controller
        label = ttk.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PwgenForm"))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.run()
