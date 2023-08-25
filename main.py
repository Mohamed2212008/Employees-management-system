import tkinter as tk
from tkinter import ttk
import data as db

root = tk.Tk()
root.title("Employee management system")
root.geometry("800x500")
root.resizable(False, False)

main_font = ("Arial", 18)
entry_width = 15

# name
name_label = tk.Label(root, text = "Name: ", font = main_font)
name_label.place(x = 20, y = 20)
name_entry = tk.Entry(root, font = main_font, width = entry_width)
name_entry.place(x = 110, y = 20)

# age
age_label = tk.Label(root, text = "Age: ", font = main_font)
age_label.place(x = 20, y = 70)
age_entry = tk.Entry(root, font = main_font, width = entry_width)
age_entry.place(x = 110, y = 70)

# gender
gender_label = tk.Label(root, text = "Gender: ", font = main_font)
gender_label.place(x = 20, y = 120)
gender_combo = ttk.Combobox(root, values = ['Male', 'Female'], font = main_font, width = entry_width)
gender_combo.set('Male')
gender_combo.place(x = 110, y = 120)

# role
role_label = tk.Label(root, text = "Role: ", font = main_font)
role_label.place(x = 20, y = 170)
role_entry = tk.Entry(root, font = main_font, width = entry_width)
role_entry.place(x = 110, y = 170)

def send_data():
    db.insert_employees(db.id(),name_entry.get(),age_entry.get(), gender_combo.get(), role_entry.get())
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    gender_combo.set('Male')
    role_entry.delete(0, 'end')
    print_data()

def get_id():
    selected_item = tv.focus()
    values = tv.item(selected_item)
    id = values.get('values')[0]
    return id

def edit():
    id = get_id()
    row = db.get_row(id)
    print(row)
    db.delete_from_db(id)
    print_data()
    name_entry.insert(0,row[1])
    age_entry.insert(1,row[2])
    gender_combo.set(row[3])
    role_entry.insert(4,row[4])

def delete():
    id = get_id()
    db.delete_from_db(id)
    print_data()

def print_file():
    data = db.get_data()
    f = open('employees.txt', 'w')
    for item in data:
        for i in range(5):
            f.write(str(item[i]) + " ")
        f.write('\n')

def clr_all():
    db.clr_data()
    print_data()

# options
add_btn = tk.Button(root, font = main_font, text = "Add Employee", width = 13, bg = '#eee', command = send_data)
add_btn.place(x = 20, y = 250)

edit_btn = tk.Button(root, font = main_font, text = "Edit Employee", width = 13, bg = '#eee', command = edit)
edit_btn.place(x = 20, y = 300)

delete_btn = tk.Button(root, font = main_font, text = 'Delete Employee', width = 13, bg = '#eee', command = delete)
delete_btn.place(x = 20, y = 350)

print_in_file = tk.Button(root, font = main_font, text = 'Print In A File', width = 13, bg = '#eee', command = print_file)
print_in_file.place(x = 20, y = 400)

clr_btn = tk.Button(root, font = main_font, text = 'Clear All', width = 13, bg = '#eee', command = clr_all )
clr_btn.place(x = 20, y = 450)

# tree view
tv = ttk.Treeview(root, height = 23)
tv['columns'] = ('id', 'name', 'age', 'gender','Role')
tv.column('#0', width=0, stretch= False)
tv.column('id', width=89, anchor = 'center', stretch = False)
tv.column('name', width=89, anchor = 'center', stretch = False)
tv.column('age', width=89, anchor = 'center', stretch = False)
tv.column('gender', width=89, anchor = 'center', stretch = False)
tv.column('Role', width=89, anchor = 'center', stretch = False)

tv.heading('#0', text = '', anchor = 'center')
tv.heading('id', text = 'id', anchor = 'center')
tv.heading('name', text = 'name', anchor = 'center')
tv.heading('age', text = 'age', anchor = 'center')
tv.heading('gender', text = 'gender', anchor = 'center')
tv.heading('Role', text = 'role', anchor = 'center')

def print_data():
    for item in tv.get_children():
        tv.delete(item)
    data = db.get_data()
    for counter, i in enumerate(data):
        tv.insert('', 'end', iid = (counter), values = i)

tv.place(x = 350, y = 0)

print_data()

root.mainloop()