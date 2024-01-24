import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(bg='#F0F0F0') 

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg='green', fg='white')
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, bg='blue', fg='white')
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, bg='brown', fg='white')
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, bg='grey', fg='white')
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg='red', fg='white')

        self.name_label.grid(row=0, column=0, sticky="E")
        self.name_entry.grid(row=0, column=1, padx=12, pady=10)

        self.phone_label.grid(row=1, column=0, sticky="E")
        self.phone_entry.grid(row=1, column=1, padx=12, pady=10)

        self.email_label.grid(row=2, column=0, sticky="E")
        self.email_entry.grid(row=2, column=1, padx=12, pady=10)

        self.address_label.grid(row=3, column=0, sticky="E")
        self.address_entry.grid(row=3, column=1, padx=12, pady=10)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=8)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=8)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=8)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=8)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=8)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Contact Book", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Contact Book", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact Book", f"Contacts:\n{contact_list}")
        else:
            messagebox.showinfo("Contact Book", "No contacts available.")

    def search_contact(self):
        search_term = self.name_entry.get().lower()
    
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term == contact['Name'].lower() or search_term == contact['Phone'].lower()]
            
            if found_contacts:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Contact Book", f"Search results:\n{contact_list}")
            else:
                messagebox.showinfo("Contact Book", "No matching contacts found.")
        else:
            messagebox.showwarning("Contact Book", "Please enter a search term.")

    def update_contact(self):
        search_term = self.name_entry.get().lower()
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term == contact['Name'].lower()]
            if found_contacts:
                contact = found_contacts[0]
                contact["Phone"] = self.phone_entry.get()
                contact["Email"] = self.email_entry.get()
                contact["Address"] = self.address_entry.get()
                messagebox.showinfo("Contact Book", "Contact updated successfully!")
                self.clear_entries()
            else:
                messagebox.showinfo("Contact Book", "No matching contacts found.")
        else:
            messagebox.showwarning("Contact Book", "Please enter a search term.")

    def delete_contact(self):
        search_term = self.name_entry.get().lower()
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term == contact['Name'].lower()]
            if found_contacts:
                contact = found_contacts[0]
                self.contacts.remove(contact)
                messagebox.showinfo("Contact Book", "Contact deleted successfully!")
                self.clear_entries()
            else:
                messagebox.showinfo("Contact Book", "No matching contacts found.")
        else:
            messagebox.showwarning("Contact Book", "Please enter a search term.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
