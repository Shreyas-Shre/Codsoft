import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Book")

        self.contacts = self.load_contacts()

        self.create_widgets()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                data = f.read()
                if data:
                    return json.loads(data)
                else:
                    return []
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f, indent=4)

    def create_widgets(self):
        self.contact_list = tk.Listbox(self)
        self.contact_list.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        scrollbar.config(command=self.contact_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_list.config(yscrollcommand=scrollbar.set)

        self.refresh_contact_list()

        self.add_button = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.TOP, padx=10, pady=5)

        self.delete_button = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.TOP, padx=10, pady=5)

        self.update_button = tk.Button(self, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.TOP, padx=10, pady=5)

        self.search_label = tk.Label(self, text="Search:")
        self.search_label.pack(side=tk.TOP, padx=10, pady=5)

        self.search_entry = tk.Entry(self)
        self.search_entry.pack(side=tk.TOP, padx=10, pady=5)

        self.search_button = tk.Button(self, text="Search", command=self.search_contact)
        self.search_button.pack(side=tk.TOP, padx=10, pady=5)

    def refresh_contact_list(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter name:")
        phone = simpledialog.askstring("Phone", "Enter phone number:")
        email = simpledialog.askstring("Email", "Enter email address:")
        address = simpledialog.askstring("Address", "Enter address:")

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.save_contacts()
            self.refresh_contact_list()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def delete_contact(self):
        selected_index = self.contact_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.save_contacts()
            self.refresh_contact_list()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def update_contact(self):
        selected_index = self.contact_list.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            name = simpledialog.askstring("Name", "Enter name:", initialvalue=contact["name"])
            phone = simpledialog.askstring("Phone", "Enter phone number:", initialvalue=contact["phone"])
            email = simpledialog.askstring("Email", "Enter email address:", initialvalue=contact["email"])
            address = simpledialog.askstring("Address", "Enter address:", initialvalue=contact["address"])

            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
                self.save_contacts()
                self.refresh_contact_list()
            else:
                messagebox.showerror("Error", "Name and Phone are required fields.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def search_contact(self):
        keyword = self.search_entry.get().lower()
        results = []
        for contact in self.contacts:
            if keyword in contact['name'].lower() or keyword in contact['phone']:
                results.append(f"{contact['name']} - {contact['phone']}")

        self.contact_list.delete(0, tk.END)
        for result in results:
            self.contact_list.insert(tk.END, result)

if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
