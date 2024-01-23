import tkinter as tk
import ttkbootstrap as tkb

def update_second_entry(*args):
    # Get the value from the first entry widget
    first_entry_value = entry1.get()
    
    # Update the second entry widget with the first three letters
    entry2.config(state=tk.NORMAL)  # Enable the second entry widget
    entry2.delete(0, tk.END)        # Clear existing content
    entry2.insert(0, first_entry_value[:3])  # Insert the first three letters
    entry2.config(state=tk.DISABLED)  # Disable the second entry widget

# Create the main Tkinter window
root = tk.Tk()
root.title("Entry Widget Example")

# Create the first entry widget
entry1 = tkb.Entry(root)
entry1.grid(row=0, column=0, padx=10, pady=10)
entry1.insert(0, "Type here")
entry1.bind("<KeyRelease>", update_second_entry)

# Create the second entry widget (disabled initially)
entry2 = tkb.Entry(root, state=tk.DISABLED)
entry2.grid(row=1, column=0, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
