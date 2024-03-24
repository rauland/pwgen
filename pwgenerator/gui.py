"""GUI Module for PWGEN"""
import ttkbootstrap as ttk
# from ttkbootstrap.constants import BOTH, YES
from pwgen import generate

class App():
    """APP GUI Class"""
    def __init__(self):
        self.root = ttk.Window(themename="cosmo")

        self.root.title("PWGEN")
        self.root.geometry("600x480")

        # Components
        self.form = PwgenForm(self.root)
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

        self.l2 = ttk.Label(self, text="Enter the password length", bootstyle="info", font=("Helvetica", 10))
        self.l2.pack(pady=10)
        self.e1 = ttk.Spinbox(
            self,
            bootstyle="info",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0, to=100)

        self.e1.pack(pady=10)
        self.l3 = ttk.Label(self, text="How many passwords?", bootstyle="info", font=("Helvetica", 10))
        self.l3.pack(pady=10)
        self.c1 = ttk.Spinbox(
            self,
            bootstyle="primary",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0, to=100)

        self.c1.pack(pady=10)
        self.b1 = ttk.Button(
            self, text="Submit", bootstyle="primary",
            command=lambda: generated_output(self.e1.get(),self.c1.get(),self.l4))
        self.b1.pack(padx=5, pady=10)

        self.l4 = ttk.Label(self, text="Output goes here...", bootstyle="info")
        self.l4.pack(pady=10)

class Validate():
    """GUI Field Validation"""
    def number(self, x) -> bool:
        """Validates that the input is a number"""
        if x.isdigit():
            return True
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

def generated_output(length,count,output):
    """Sets output for GUI"""
    output_list = generate.many_secrets(int(length),int(count),False,True)
    label_text = '\n'.join(output_list)
    output.config(text=label_text)

validate = Validate()

if __name__ == "__main__":
    app = App()
    app.run()
