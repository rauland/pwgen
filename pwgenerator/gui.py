"""GUI Module for PWGEN"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import LEFT

class App():
    """APP GUI Class"""
    def __init__(self):
        self.root = ttk.Window(themename="cosmo")

        self.root.title("PWGEN")
        self.b1 = ttk.Button(self.root, text="Submit", bootstyle="success")
        self.b1.pack(side=LEFT, padx=5, pady=10)

        self.b2 = ttk.Button(self.root, text="Submit", bootstyle="info-outline")
        self.b2.pack(side=LEFT, padx=5, pady=10)


    def run(self):
        """Run the GUI"""
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
