"""GUI Module for PWGEN"""
import ttkbootstrap as ttk
# from ttkbootstrap.constants import BOTH, YES
from pwgen import generate

class App():
    """APP GUI Class"""
    def __init__(self):
        self.root = ttk.Window(themename="morph")

        self.root.title("PWGEN")
        self.root.geometry("600x480")

        # Components
        self.form = PwgenForm(self.root, padding=10)
        self.form.pack()

    def run(self):
        """Run the GUI"""
        self.root.mainloop()

class PwgenForm(ttk.Frame):
    """pwgen GUI form"""
    def __init__(self, master,  *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Set border properties
        # self.configure(borderwidth=2,relief="solid")

        # register the validation callback
        digit_func = self.register(validate.number)
        # alpha_func = self.register(validate.alpha)

        self.l1 = ttk.Label(self, text="Password Generator", bootstyle="primary", font=("Helvetica", 16))
        self.l1.pack(pady=10)

        self.l2 = ttk.Label(self, text="Enter the password length", bootstyle="primary", font=("Helvetica", 10))
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
            bootstyle="primary",
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
            command=lambda: generated_output(self.e1.get(),self.c1.get(),self.l4))
        self.b1.pack(padx=5, pady=10)

        self.l4 = ttk.Text(self)
        # self.l4 = ttk.Text(self, text="Output goes here...", bootstyle="info")
        self.l4.insert(1.0, "Output goes here...")
        self.l4.configure(state="disabled")
        self.l4.pack()

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

def generated_output(length, count, text):
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

if __name__ == "__main__":
    app = App()
    app.run()
