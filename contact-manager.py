# contact_manager.py

contacts = []

def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email":email})
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")

def search_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            print(f"Contact found: {contact['name']}: {contact['phone']}")
            return
    print(f"Contact '{name}' not found.")

def delete_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone,email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()