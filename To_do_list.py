'''               Important !!! 

To run this code please install the following packages:- 

pip install customtkinter
pip install tk
'''
#task 3  To do list by Swetankan Kumar Sinha (Batch-A28)

# Importing module
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox as msgb

# Creating root
list_root = Tk()

list_root.title("TO DO LIST")
list_root.geometry("385x560+550+150")
list_root.config(bg='#1F2833')
list_root.resizable(False, False)

def task_add():
    task = task_input.get()
    if task.strip():
        tasks_list.insert(0, task)
        task_input.delete(0, END)
        save_tasks()
    else:
        msgb.showerror('Error', 'Task cannot be empty or blankspaces! \n \nPlease enter a task to add')

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        msgb.showerror('Error', 'Choose a task to delete. ')
def mark_as_done():
    selected = tasks_list.curselection()
    if selected:
        task = tasks_list.get(selected[0])
        tasks_list.delete(selected[0])
        tasks_list.insert(selected[0], "✔️ " + task)
        tasks_list.itemconfig(selected, fg="green")
        msgb.showinfo('Success', 'Task marked as done!')
    else:
        msgb.showerror('Error', 'Choose a task to mark as done.')
    
def remove_all_tasks():
    if msgb.askyesno('Confirmation','Are you sure?'):
        tasks_list.delete(0,END)
        msgb.showinfo('Success', 'All tasks removed successfully!')
        save_tasks()

def save_tasks():
    with open("tasks_list_file.txt", "w") as f:
        tasks = tasks_list.get(0, END)
        for task in tasks:
            f.write(task +"\n")

def task_loder():
    try:
        with open("tasks_list_file.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0, task.strip())
    except FileNotFoundError:
       open("tasks_list_file.txt", "w").close()

# Labels
Label(list_root, font="FZShuti  8 bold",fg="yellow", bg='#1F2833',text="#Developed by Swetankan").place(x=225,y=540)
ctk.CTkLabel(list_root,  font=('Candra', 32,'bold'),  text=" To-Do List ",   text_color='#1F2833',bg_color='#FFF03C').place(x=105,y=15)
ctk.CTkLabel(list_root,  font=('Candra', 18,'bold'),  text=" Enter a task ", text_color='white',  bg_color='#1F2833', height=10,width=10).place(x=10,y=90)

# Entry display
task_input = Entry(list_root,  font=('Candra', 15 ),fg="black",bg="White",border=4)
task_input.place(width=366, height=35,x=10,y=118)

# List Box display
tasks_list = Listbox(list_root,font=('Candra', 20,),height=9,width=24,border=4 )
tasks_list.place(x=10,y=193)

# Buttons display
ctk.CTkButton(list_root, font=('Candra', 15,'bold'),  text="Add Task",         text_color='black', bg_color='#1F2833', fg_color="white", hover_color="#00F0FF",   cursor='hand2',corner_radius=20,height=20,width=10,command=task_add).place(x=150,y=160)
ctk.CTkButton(list_root, font=('Candra', 15,),        text="Remove Task",      text_color='black', bg_color='#1F2833', fg_color="white", hover_color="#E66B04",   cursor='hand2',corner_radius=20,height=20,width=10,command=remove_task).place(x=8,y=513)
ctk.CTkButton(list_root, font=('Candra', 15,),        text="Mark as Done",     text_color='black', bg_color='#1F2833', fg_color="white", hover_color="dark green",cursor='hand2',corner_radius=20,height=20,width=10,command=mark_as_done).place(x=127,y=513)
ctk.CTkButton(list_root, font=('Candra', 15,),        text="Remove all tasks", text_color='black', bg_color='#1F2833', fg_color="white", hover_color="#FF0202",   cursor='hand2',corner_radius=20,height=20,width=10,command=remove_all_tasks).place(x=245,y=513)

task_loder()
list_root.mainloop()
