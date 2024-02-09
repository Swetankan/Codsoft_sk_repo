'''               Important !!! 

To run this code please install the following packages:- 
pip install tk
'''
#task 4  Contact Book by Swetankan Kumar Sinha (Batch-A28)

# Importing module
from tkinter import *
from tkinter import messagebox as msgb
import csv

# Creating root
contact_root = Tk()
contact_root.title("CONTACT BOOK")
contact_root.geometry("550x340+450+150")
contact_root.config(bg='#162622')
contact_root.resizable(False, False)

contacts = {}
# Defining functions
def save_contact():
    name = entry_name.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone_number:
        msgb.showerror('Error', '(*) fields are mandatory!')
        return

    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }

    contacts[name] = contact
    clear_fields()
    msgb.showinfo('Success', 'Contact saved successfully !')

def search_contact():
    name = entry_search_name.get()

    if not name:
        msgb.showerror('Error', 'Please enter a name to search.')
        return

    results = [contact for contact in contacts.values() if name.lower() in contact["name"].lower()]

    if not results:
        msgb.showerror('Error', 'No contact found !')
        return
    elif len(results) > 1:
        matches = ', '.join([contact["name"] for contact in results])
        msgb.showinfo('Multiple Matches Found', f'{len(results)} matches found for {name}. The matches are:\n{matches}.\nPlease refine your search.')
        return
    elif entry_name.get() and entry_phone_number.get() and entry_email.get() and entry_address.get():
        msgb.showerror('Error', 'Contact details are already displayed.')
        return
    for contact in results:
        entry_name.insert(0, contact["name"])
        entry_phone_number.insert(0, contact["phone_number"])
        entry_email.insert(0, contact["email"])
        entry_address.insert(0, contact["address"])



def update_contact():
    name = entry_name.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone_number:
        msgb.showerror('Error', 'Name and number fields are required')
        return

    contacts[name] = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }

    with open('contacts_list.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone Number", "Email", "Address"])
        for contact in contacts.values():
            writer.writerow([contact["name"], contact["phone_number"], contact["email"], contact["address"]])

    clear_fields()
    msgb.showinfo('Success', 'Contact updated successfully')




def clear_fields():
    entry_name.delete(0, END)
    entry_phone_number.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)

def reset_search():
    entry_search_name.delete(0, END)

def on_closing():
    with open('contacts_list.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone Number", "Email", "Address"])
        for contact in contacts.values():
            writer.writerow([contact["name"], contact["phone_number"], contact["email"], contact["address"]])
    contact_root.destroy()


def load_contacts():
    try:
        with open('contacts_list.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, phone_number, email, address = row
                contacts[name] = {
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                    "address": address
                }
    except FileNotFoundError:
        pass     

contact_root.protocol("WM_DELETE_WINDOW", on_closing)

# Creating Labels
Label(contact_root,  font=('Candra', 18,'bold'),  text="Contact Book",fg='#faea05',bg='#162622').place(x=200,y=13)
Label(contact_root, font="FZShuti  8 bold",fg="#faea05", bg='#162622',text="#Developed by Swetankan").place(x=390,y=322)
Label(contact_root,  font=('Candra', 12),  text="Enter Name", fg='white',  bg='#162622').place(x=10,y=75)
Label(contact_root,  font=('Candra', 12),  text="*", fg='red',  bg='#162622').place(x=100,y=75)
Label(contact_root,  font=('Candra', 12),  text="Enter Phone Number", fg='white',  bg='#162622').place(x=10,y=100)
Label(contact_root,  font=('Candra', 12),  text="*", fg='red',  bg='#162622').place(x=162,y=100)
Label(contact_root,  font=('Candra', 12),  text="Enter Email", fg='white',  bg='#162622').place(x=10,y=125)
Label(contact_root,  font=('Candra', 12),  text="Enter Address", fg='white',  bg='#162622').place(x=10,y=150)
Label(contact_root,  font=('Candra', 12),  text="Search by Name", fg='white',  bg='#162622').place(x=10,y=240)

# Creating Entry
entry_name = Entry(contact_root,  font=('Candra', 12),fg="Black",bg="White")
entry_name.place(x=190,y=75,width=340, height=20)
entry_phone_number = Entry(contact_root,  font=('Candra', 12),fg="Black",bg="White")
entry_phone_number.place(x=190,y=100,width=340, height=20)
entry_email = Entry(contact_root,  font=('Candra', 12),fg="Black",bg="White")
entry_email.place(x=190,y=125,width=340, height=20)
entry_address =Entry(contact_root,  font=('Candra', 12),fg="Black",bg="White")
entry_address.place(x=190,y=150,width=340, height=20)
entry_search_name = Entry(contact_root,  font=('Candra', 12),fg="Black",bg="White")
entry_search_name.place(x=190,y=240,width=340, height=20)

# Creating Buttons
Button(contact_root, font=('Candra', 13,), text="Save", bg='#4feaff', fg="Black", command=save_contact).place(x=10,y=190,width=60, height=30)
Button(contact_root, font=('Candra', 13,), text="Clear", bg='#4feaff', fg="Black", command=clear_fields).place(x=80,y=190,width=75, height=30)
Button(contact_root, font=('Candra', 13,), text="Search", bg='#4feaff', fg="Black", command=search_contact).place(x=10,y=280,width=75, height=30)
Button(contact_root, font=('Candra', 13,), text="Reset", bg='#4feaff', fg="Black", command=reset_search).place(x=100,y=280,width=75, height=30)
Button(contact_root, font=('Candra', 13,), text="Update", bg='#4feaff', fg="Black", command=update_contact).place(x=165,y=190,width=75, height=30)
load_contacts()
contact_root.mainloop()
