from tkinter import *
from tkinter import ttk


# Move Row Up
def up(my_tree):
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down(my_tree):
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one(my_tree):
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove Many records
def remove_many(my_tree):
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Remove all records
def remove_all(my_tree):
	for record in my_tree.get_children():
		my_tree.delete(record)

# Clear entry boxes
def clear_entries(Details):
	# Clear entry boxes
	Details[0].delete(0, END)
	Details[1].delete(0, END)
	Details[2].delete(0, END)
	Details[3].delete(0, END)
	Details[4].delete(0, END)
	Details[5].delete(0, END)
	Details[6].delete(0, END)


# Select Record
def select_record(my_tree,Details):
	# Clear entry boxes
	Details[0].delete(0, END)
	Details[1].delete(0, END)
	Details[2].delete(0, END)
	Details[3].delete(0, END)
	Details[4].delete(0, END)
	Details[5].delete(0, END)
	Details[6].delete(0, END)

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	Details[0].insert(0, values[0])
	Details[1].insert(0, values[1])
	Details[2].insert(0, values[2])
	Details[3].insert(0, values[3])
	Details[4].insert(0, values[4])
	Details[5].insert(0, values[5])
	Details[6].insert(0, values[6])

# Update record
def update_record(my_tree,Details):
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	select_record(my_tree,Details)
	my_tree.item(selected, text="", values=(Details[0].get(), Details[1].get(), Details[2].get(), Details[3].get(), Details[4].get(), Details[5].get(), Details[6].get()))

	# Clear entry boxes
	Details[0].delete(0, END)
	Details[1].delete(0, END)
	Details[2].delete(0, END)
	Details[3].delete(0, END)
	Details[4].delete(0, END)
	Details[5].delete(0, END)
	Details[6].delete(0, END)