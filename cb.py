import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone to search: ")

    found = False
    for c in contacts:
        if query.lower() in c["name"].lower() or query in c["phone"]:
            print("\n--- Contact Found ---")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            found = True

    if not found:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter name of contact to update: ")

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Leave blank to keep old value.")

            new_phone = input("New phone: ")
            new_email = input("New email: ")
            new_address = input("New address: ")

            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            if new_address:
                c["address"] = new_address

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name of contact to delete: ")

    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

contacts = load_contacts()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")
