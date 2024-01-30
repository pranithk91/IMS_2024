from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from database import loadDatabase, getClientid
from new_client import ClientMainViewFrame
from new_sale import MainViewFrame

import ttkbootstrap as tkb

class clientWindow:
    def __init__(self, master):
        self.master = master
        master.title("IMS 2024")

        # Sidebar Frame
        self.sidebarFrame = SidebarFrame(master)
        self.sidebarFrame.pack_propagate(0)
        #self.sidebar_frame.pack(fill="y", anchor="w", side="left")


class MedicineApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master, background="#2A8C55", width=176, height=650)
        self.pack_propagate(0)
        self.grid(column=0, row=0)
        #self.pack(fill="y", anchor="w", side="left")

        # Logo
        self.logoLabel = CTkLabel(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png", command=self.client_frame)
        #self.ordersButton = self.create_button("Orders", "package_icon.png")
        self.ordersListButton = self.create_button("Orders", "list_icon.png", command=self.main_frame)
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png") 
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))

        #self.frames = {}
        
        self.main_view = MainViewFrame(master)
        

    def main_frame(self):

        self.main_view   = MainViewFrame(self.master)
        self.main_view.tkraise()

    def client_frame(self):

        self.main_view = ClientMainViewFrame(self.master)
        self.main_view.tkraise()


    def create_button(self, text, image_filename, pady=(16, 0), command = None):
        img_data = Image.open(f"main/{image_filename}")
        img = CTkImage(dark_image=img_data, light_image=img_data)
        return CTkButton(master=self, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14),
                         hover_color="#207244", anchor="w",command = command).pack(anchor="center", ipady=5, pady=pady )

    # Main View Frame
    



    @property
    def logoImg(self):
        return CTkImage(dark_image=Image.open("main/logo.png"),
                        light_image=Image.open("main/logo.png"), size=(77.68, 85.42))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pranith Pharmacy')
        self.geometry('856x650')
        #self.resizable(False, False)


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
    app = App()
    MedicineApp(app)
    app.mainloop()
