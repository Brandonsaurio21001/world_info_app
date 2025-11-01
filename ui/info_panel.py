import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class InfoPanel(tk.Frame):
    def __init__(self: parent):
        super().__init__(parent, bd=0, highlightthickness=0)
        self.configure(padx=10, pady=10)

        self.title = tk.label(self, text= "Selecciona o busca un país", font=("Arial", 16, "bold"))
        self.title.pack(anchor="w", pady=(0,8))
        self.flag_label = tk.Label(self)
        self.flag_label.pack(anchor="w", pady=(0,8))

        self.info_text = tk.Label(self, text="", justify="left", font=("Arial", 12))
        self.info_text.pack(anchor="w")
        
