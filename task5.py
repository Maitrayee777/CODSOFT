# Task5 Contact Book
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for name, contact_info in self.contacts.items():
                print(f"Name: {name}\tPhone: {contact_info['Phone Number']}")

    def search_contact(self, query):
        search_results = [(name, contact_info) for name, contact_info in self.contacts.items()
                          if query.lower() in name.lower() or query in contact_info['Phone Number']]
        if not search_results:
            print("No matching contacts found.")
        else:
            print("Search Results:")
            for name, contact_info in search_results:
                print(f"Name: {name}\tPhone: {contact_info['Phone Number']}")

    def update_contact(self, name, field, new_value):
        if name in self.contacts:
            if field in self.contacts[name]:
                self.contacts[name][field] = new_value
                print(f"Contact '{name}' updated successfully!")
            else:
                print("Invalid field.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            field = input("Enter field to update (Phone Number, Email, Address): ").title()
            new_value = input(f"Enter new value for {field}: ")
            contact_manager.update_contact(name, field, new_value)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()