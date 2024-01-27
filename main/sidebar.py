from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from database import loadDatabase, getClientid
#from CTkScrollableDropdown import *

import ttkbootstrap as tkb

class clientWindow:
    def __init__(self, master):
        self.master = master
        master.title("IMS 2024")

        # Sidebar Frame
        self.sidebarFrame = SidebarFrame(master)
        self.sidebarFrame.pack_propagate(0)
        #self.sidebar_frame.pack(fill="y", anchor="w", side="left")





class SidebarFrame(tkb.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=176, height=650)
        self.pack_propagate(0)

        # Logo
        self.logoLabel = tkb.Label(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png")
        self.ordersButton = self.create_button("Procedures", "package_icon.png")
        self.ordersListButton = self.create_button("Pharmacy", "list_icon.png")
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png")
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))





        #image = im = Image.open("/path/to/your/image.ext")
    def create_button(self, text, image_filename, pady=(16, 0)):
        img_data = Image.open(f"main/{image_filename}")
        img = ImageTk.PhotoImage(img_data)
        return tkb.Button(master=self, image=img, text=text,bootstyle="success").pack(anchor="center", ipady=5, pady=pady)

    @property
    def logoImg(self):
        logoImgData=Image.open("main/logo.png")
        img = ImageTk.PhotoImage(logoImgData, size=(77.68, 85.42))
        return img
    

if __name__ == "__main__":
    root = tk.Tk()
    obj = clientWindow(root)
    root.mainloop()