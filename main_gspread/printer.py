import win32print
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import tkinter as tk

program_path = r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe'
#fileName = r'C:\Users\prani\OneDrive\Documents\IMS_2024\main_ttk\Invoices\{}.pdf'.format(entry.get())
def print_file():
    fileName = r'C:\Users\prani\OneDrive\Documents\IMS_2024\main_ttk\Invoices\{}.pdf'.format(entry.get())
    adobe=Application().start(r'{} "{}"'.format(program_path, fileName))
    time.sleep(3)

    send_keys('^p')
    time.sleep(3)

    wHandle = pywinauto.findwindows.find_windows(title = u'Print')[0]
    window = adobe.window(handle=wHandle)
    window.wait('ready',timeout=10)
    window.Print.click()
    entry.delete(0,END)
    #window[u'Pri&nter:comboBox'].select(0)
    #window[u'&Properties'].click()
    

app = tk.Tk()
app.title("Print File")

tk.Label(app, text="Enter file name:").pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=5)


tk.Button(app, text="Print File", command=print_file).pack(pady=20)

app.mainloop()
