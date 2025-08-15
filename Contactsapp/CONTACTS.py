import json
import os
import difflib
import re

filename = "contacts.json"
contacts = []

if os.path.exists(filename):
    try:
        with open(filename, "r") as json_file:
            contacts = json.load(json_file)
            print(f"Loaded {len(contacts)} contacts from {filename}")
    except json.JSONDecodeError:
        print(f"{filename} is empty or corrupted. Starting with empty contacts.")
else:
    print(f"No existing {filename} found. Starting fresh.")

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r"^\+?\d{8,15}$"
    return re.match(pattern, phone) is not None

def delete_contact(c):
    confirm = input("ARE YOU SURE YOU WANT TO DELETE THIS CONTACT? (y/n): ").lower()
    if confirm == "y":
        contacts.remove(c)
        print(f"{c['name']} has been deleted.")
    elif confirm == "n":
        print("Contact not deleted.")
    else:
        print("Please enter a valid input.")

def edit_contact(c):
    new_name = input(f"Enter new name (current: {c['name']}): ")
    new_phone = input(f"Enter new phone (current: {c['phone']}): ")
    while not is_valid_phone(new_phone):
        print("Please enter a valid phone number (8-15 digits, optional + at start).")
        new_phone = input(f"Enter new phone (current: {c['phone']}): ")
    new_email = input(f"Enter new email (current: {c['email']}): ")
    while not is_valid_email(new_email):
        print("Please enter a valid email address.")
        new_email = input(f"Enter new email (current: {c['email']}): ")
    if new_name:
        c["name"] = new_name
    if new_phone:
        c["phone"] = new_phone
    if new_email:
        c["email"] = new_email
    print("Contact updated successfully!")

while True:
    print("\n--- CONTACTS APP ---")
    print("1. View Contacts")
    print("2. Search Contacts")
    print("3. Add Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "3":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        while not is_valid_phone(phone):
            print("Please enter a valid phone number (8-15 digits, optional + at start).")
            phone = input("Enter phone: ")
        email = input("Enter email: ")
        while not is_valid_email(email):
            print("Please enter a valid email address.")
            email = input("Enter email: ")
        contact = {"name": name, "phone": phone, "email": email}
        if contact in contacts:
            print(f"{name} already exists in contacts. Failed to add.")
        else:
            contacts.append(contact)
            print(f"{name} added successfully.")
    elif choice == "1":
        if not contacts:
            print("No contacts yet.")
        else:
            print("\n--- ALL CONTACTS ---")
            for idx, c in enumerate(contacts, start=1):
                print(f"{idx}. NAME: {c['name']}, PHONE: {c['phone']}, EMAIL: {c['email']}")
    elif choice == "2":
        search_by = input("Do you want to search by name or number? ").lower()
        found = False
        if search_by == "name":
            search_name = input("Enter name of contact: ").lower()
            for c in contacts:
                if (search_name in c["name"].lower() or
                    difflib.SequenceMatcher(None, search_name, c["name"].lower()).ratio() > 0.6):
                    print(f"Closest Match/Match: NAME: {c['name']}, PHONE: {c['phone']}, EMAIL: {c['email']}")
                    edit_choice = input("Do you want to edit this contact? (y/n): ").lower()
                    if edit_choice == "y":
                        edit_contact(c)
                    found = True
            if not found:
                print("No contact found with that name.")
        elif search_by == "number":
            search_phone = input("Enter phone number of contact: ")
            for c in contacts:
                if search_phone in c["phone"]:
                    print(f"Found: NAME: {c['name']}, PHONE: {c['phone']}, EMAIL: {c['email']}")
                    edit_choice = input("Do you want to edit this contact? (y/n): ").lower()
                    if edit_choice == "y":
                        edit_contact(c)
                    found = True
            if not found:
                print("No contact found with that phone number.")
        else:
            print("Invalid search option. Choose 'name' or 'number'.")
    elif choice == "4":
        search_by = input("Do you want to search to delete the contact by name or number? ").lower()
        found = False
        if search_by == "name":
            search_name = input("Enter name of contact: ").lower()
            for c in contacts:
                if c["name"].lower() == search_name:
                    print(f"Found: NAME: {c['name']}, PHONE: {c['phone']}, EMAIL: {c['email']}")
                    delete_contact(c)
                    found = True
            if not found:
                print("No contact found with that name.")
        elif search_by == "number":
            search_phone = input("Enter phone number of contact: ")
            for c in contacts:
                if c["phone"] == search_phone:
                    print(f"Found: NAME: {c['name']}, PHONE: {c['phone']}, EMAIL: {c['email']}")
                    delete_contact(c)
                    found = True
            if not found:
                print("No contact found with that phone number.")
        else:
            print("Invalid search option. Choose 'name' or 'number'.")
    elif choice == "5":
        try:
            with open(filename, "w") as json_file:
                json.dump(contacts, json_file)
            print(f"Data successfully written to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
