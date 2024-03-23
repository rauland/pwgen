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

        # register the validation callback
        digit_func = self.root.register(validate_number)
        # alpha_func = self.root.register(validate_alpha)

        # Components
        self.l1 = ttk.Label(self.root, text="Password Generator", bootstyle="primary")
        self.l1.pack(pady=10)

        self.l2 = ttk.Label(self.root, text="Enter the password length", bootstyle="info")
        self.l2.pack(pady=10)
        self.e1 = ttk.Spinbox(
            self.root,
            bootstyle="info",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0, to=100)

        self.e1.pack(pady=10)
        self.l3 = ttk.Label(self.root, text="How many passwords?", bootstyle="info")
        self.l3.pack(pady=10)
        self.c1 = ttk.Spinbox(
            self.root,
            bootstyle="primary",
            validate="focus",
            validatecommand=(digit_func, '%P'),
            from_=0, to=100)

        self.c1.pack(pady=10)
        self.b1 = ttk.Button(
            self.root, text="Submit", bootstyle="primary",
            command=lambda: output_set(self.e1.get(),self.c1.get(),self.l4))
        self.b1.pack(padx=5, pady=10)

        self.l4 = ttk.Label(self.root, text="Output goes here...", bootstyle="info")
        self.l4.pack(pady=10)

    def run(self):
        """Run the GUI"""
        self.root.mainloop()

def validate_number(x) -> bool:
    """Validates that the input is a number"""
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False

def validate_alpha(x) -> bool:
    """Validates that the input is alpha"""
    if x.isdigit():
        return False
    elif x == "":
        return True
    else:
        return True

def output_set(length,count,output):
    """Get output for GUI"""
    output_list = generate.many_secrets(int(length),int(count),False,True)
    label_text = '\n'.join(output_list)
    output.config(text=label_text)

if __name__ == "__main__":
    app = App()
    app.run()
