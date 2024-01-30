import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("300x300")

img = Image.open("main_ttk/logo.png") 
res_img = img.resize((77, 85), Image.ANTIALIAS)
con_img = ImageTk.PhotoImage(res_img)

frame = ttk.Frame(root,height=300, width=300)
frame.pack()
#frame.configure(height=300, width=300)

ttk.Label(frame, image=con_img).pack()

s = ttk.Style()
s.configure('success.TButton',         relief=[('pressed', 'groove'),
                ('!pressed', 'ridge')])


s = ttk.Style()
s.configure('Wild.TButton',
    background='black',
    foreground='white',
    highlightthickness='20',
    font=('Helvetica', 18, 'bold'))
s.map('Wild.TButton',
    foreground=[('disabled', 'yellow'),
                ('pressed', 'red'),
                ('active', 'blue')],
    background=[('disabled', 'magenta'),
                ('pressed', '!focus', 'cyan'),
                ('active', 'green')],
    highlightcolor=[('focus', 'green'),
                    ('!focus', 'red')],
    relief=[('pressed', 'groove'),
            ('!pressed', 'ridge')])


confirmDetailsButton = ttk.Button(master=frame, text="Register",
                                #font=("Calibri", 15), 
                                style="Wild.TButton", 
                                #height=20,  
                               ).pack()

root.mainloop()