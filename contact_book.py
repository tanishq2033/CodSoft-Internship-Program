contacts = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully.\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
        print("-" * 30)


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        info = contacts[name]
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}\n")
    else:
        print("Contact not found.\n")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        contacts[name]["phone"] = input("New phone: ")
        contacts[name]["email"] = input("New email: ")
        contacts[name]["address"] = input("New address: ")
        print("Contact updated successfully.\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")


while True:
    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Try again.")