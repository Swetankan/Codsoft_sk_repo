import tkinter as tk
from tkinter import messagebox

def create_contact_book():
    contacts = {}

    def save_contact():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        phone_number = entry_phone_number.get()
        email = entry_email.get()
        address = entry_address.get()

        if not first_name or not last_name or not phone_number:
            messagebox.showerror("Error", "All fields are required")
            return

        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }

        contact_id = max(contacts.keys()) + 1 if contacts else 0
        contacts[contact_id] = contact

        clear_fields()

    def search_contact():
        last_name = entry_search_last_name.get()

        if not last_name:
            messagebox.showerror("Error", "Please enter a last name to search")
            return

        results = [contact for contact in contacts.values() if contact["last_name"].lower() == last_name.lower()]

        if not results:
            messagebox.showerror("Error", "No contacts found")
            return

        display_results(results)

    def display_results(results):
        clear_results()

        for i, contact in enumerate(results, 1):
            label = tk.Label(frame_results, text=f"{i}. {contact['first_name']} {contact['last_name']} - {contact['phone_number']}")
            label.pack()

    def clear_fields():
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_phone_number.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

    def clear_results():
        for widget in frame_results.winfo_children():
            widget.destroy()

    root = tk.Tk()

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    label_first_name = tk.Label(frame_top, text="Enter First Name(*)")
    label_first_name.grid(row=0, column=0, padx=10)
    entry_first_name = tk.Entry(frame_top)
    entry_first_name.grid(row=0, column=1, padx=10)

    label_last_name = tk.Label(frame_top, text="Enter Last Name(*)")
    label_last_name.grid(row=1, column=0, padx=10)
    entry_last_name = tk.Entry(frame_top)
    entry_last_name.grid(row=1, column=1, padx=10)

    label_phone_number = tk.Label(frame_top, text="Enter Phone Number(*)")
    label_phone_number.grid(row=2, column=0, padx=10)
    entry_phone_number = tk.Entry(frame_top)
    entry_phone_number.grid(row=2, column=1, padx=10)

    label_email = tk.Label(frame_top, text="Enter Email")
    label_email.grid(row=3, column=0, padx=10)
    entry_email = tk.Entry(frame_top)
    entry_email.grid(row=3, column=1, padx=10)

    label_address = tk.Label(frame_top, text="Enter Address")
    label_address.grid(row=4, column=0, padx=10)
    entry_address = tk.Entry(frame_top)
    entry_address.grid(row=4, column=1, padx=10)

    button_save = tk.Button(frame_top, text="Save Contact", command=save_contact)
    button_save.grid(row=5, column=0, columnspan=2, pady=10)

    label_search_last_name = tk.Label(frame_top, text="Search by Last Name")
    label_search_last_name.grid(row=6, column=0, padx=10)
    entry_search_last_name = tk.Entry(frame_top)
    entry_search_last_name.grid(row=6, column=1, padx=10)

    button_search = tk.Button(frame_top, text="Search Contact", command=search_contact)
    button_search.grid(row=7, column=0, columnspan=2, pady=10)

    frame_results = tk.Frame(root)
    frame_results.pack(pady=10)

    root.mainloop()

create_contact_book()
