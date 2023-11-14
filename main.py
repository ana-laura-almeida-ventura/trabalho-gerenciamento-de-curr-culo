# pip install mysql-connector-python pillow reportlab
import tkinter as tk
from biblioteca import Gerenciamento

if __name__ == "__main__":
    root = tk.Tk()
    app = Gerenciamento(root)
    app.update_table()
    root.mainloop()
