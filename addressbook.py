import json
import os
from time import sleep

file_name = "addresses.json"

def load_contacts():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"contacts": []}  # Corrected "addresses" to "contacts"

def view_contacts(contacts):
    os.system("cls" if os.name == "nt" else "clear")
    
    if not contacts["contacts"]:
        print("No contacts found.")
        input("\nPress Enter to return to the menu...")
        return  # Exit function if no contacts exist

    # Display indexed list of contacts
    print(f"\033[1;32mAll Contacts:\033[0m ({len(contacts['contacts'])})\n")
    for idx, entry in enumerate(contacts["contacts"], start=1):
        print(f"{idx}. {entry['name']}")

    # Let user select a contact or go back
    while True:
        choice = input("\nEnter the number of the person you want to see details of, or 'b' to go back: ").strip()

        if choice.lower() == 'b':
            print("Returning to the main menu...")
            return  # Exit function

        try:
            choice = int(choice)
            if 1 <= choice <= len(contacts["contacts"]):
                selected_contact = contacts["contacts"][choice - 1]
                print("\n\033[1;32mContact Details:\033[0m\n")
                print(f"Name: {selected_contact['name']}")
                print(f"Phone: {selected_contact['phone']}")
                print(f"Email: {selected_contact['email']}")
                print(f"Address: {selected_contact['address']}")
                print(f"Notes: {selected_contact['notes']}")
                input("\nPress Enter to return to the menu...")
                return  # Exit after showing details
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            
            print("Enter a valid number or 'b' to go back.")

def add_contacts(contacts):
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;32m💰 Add a new contact 💳\033[0m\n")
    
    name_input = input("Enter Name: ").strip()
    address_input = input("Enter Address: ").strip()
    phone_input = input("Enter phone #: ").strip()
    email_input = input("Enter email address: ").strip()
    note_input = input("Enter notes: ").strip()

    new_contact = {
        "name": name_input,
        "address": address_input,
        "phone": phone_input if phone_input else "",
        "email": email_input,
        "notes": note_input if note_input else ""
    }

    contacts["contacts"].append(new_contact)

    try:
        with open(file_name, "w") as file:
            json.dump(contacts, file, indent=4)
        print("\nNew Contact added successfully!")
    except:
        print("Failed to save the contact.")

    input("\nPress Enter to return to the menu...")
    os.system("cls" if os.name == "nt" else "clear")

def delete_contacts(contacts):
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;32mDelete a contact\033[0m")

    if not contacts["contacts"]:
        print("No contacts to delete.")
        input("\nPress Enter to return to the menu...")
        os.system("cls" if os.name == "nt" else "clear")
        return
    
    print("\nSelect a contact to delete:\n")
    for idx, entry in enumerate(contacts["contacts"], start=1):
        print(f"{idx}. {entry['name']}")

    while True:
        try:
            choice = input("\nEnter the number of the contact to delete (or 'b' to go back): ").strip()
            if choice.lower() == "b":
                print("Returning to main menu...")
                os.system("cls" if os.name == "nt" else "clear")
                return

            contact_index = int(choice) - 1
            if 0 <= contact_index < len(contacts):
                del contacts["contacts"][contact_index]  # Remove the correct bill from the original list

                with open(file_name, "w") as file:
                    json.dump(contacts, file, indent=4)

                print("\nContact deleted successfully!")
                break
            else:
                print("Invalid selection. Please choose a valid contact number.")
        except ValueError:
            print("Enter a valid number.")

    input("\nPress Enter to return to the menu...")
    os.system("cls" if os.name == "nt" else "clear")

def search_contacts(addresses):
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;32m🔍 Search Contacts\033[0m\n")

    search_term = input("Enter a name, phone, email, or address to search: ").strip().lower()

    matching_contacts = [
        contact for contact in addresses["contacts"]
        if search_term in contact["name"].lower() 
        or search_term in contact["phone"].lower()
        or search_term in contact["email"].lower()
        or search_term in contact["address"].lower()
    ]

    if not matching_contacts:
        print("\nNo contacts found matching your search.")
        input("\nPress Enter to return to the menu...")
        return

    print("\n\033[1;34mMatching Contacts:\033[0m\n")
    for idx, contact in enumerate(matching_contacts, start=1):
        print(f"{idx}. {contact['name']}")

    # Let user select a contact or go back
    while True:
        choice = input("\nEnter the number of the person you want to see details of, or 'b' to go back: ").strip()

        if choice.lower() == 'b':
            print("Returning to the main menu...")
            return  

        try:
            choice = int(choice)
            if 1 <= choice <= len(matching_contacts):
                selected_contact = matching_contacts[choice - 1]
                print("\n\033[1;32mContact Details:\033[0m")
                print(f"Name: {selected_contact['name']}")
                print(f"Phone: {selected_contact['phone']}" if selected_contact['phone'] else "Phone: (Not Provided)")
                print(f"Email: {selected_contact['email']}")
                print(f"Address: {selected_contact['address']}")
                print(f"Notes: {selected_contact['notes']}" if selected_contact['notes'] else "Notes: (No additional info)")
                input("\nPress Enter to return to the menu...")
                return  
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Enter a valid number or 'b' to go back.")

def main():
    contacts = load_contacts()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1;32mAddress Book\033[0m\n")
        print("1. View contacts\n2. Add Contact\n3. Delete Contact\n4. Search Contact\nq. Exit\n")
        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice =="2":
            add_contacts(contacts)
        elif choice =="3":
            delete_contacts(contacts)
        elif choice =="4":
            search_contacts(contacts)
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again")
            sleep(1)

main()