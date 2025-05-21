import json
import os
from time import sleep

file_name = "addresses.json"

def load_address():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"contacts": []}  # Corrected "addresses" to "contacts"

def view_addresses(addresses):
    os.system("cls" if os.name == "nt" else "clear")
    
    if not addresses["contacts"]:
        print("No addresses found.")
        input("\nPress Enter to return to the menu...")
        return

    # Display indexed list of contacts
    for idx, entry in enumerate(addresses["contacts"], start=1):
        print(f"{idx}. {entry['name']}")

    # Let user select a contact by index
    while True:
        try:
            choice = int(input("\nEnter the number of the person you want to see details of: ").strip())
            
            if 1 <= choice <= len(addresses["contacts"]):
                selected_contact = addresses["contacts"][choice - 1]
                print("\n\033[1;32mContact Details:\033[0m")
                print(f"Name: {selected_contact['name']}")
                print(f"Phone: {selected_contact['phone']}")
                print(f"Email: {selected_contact['email']}")
                print(f"Address: {selected_contact['address']}")
                print(f"Notes: {selected_contact['notes']}")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Enter a valid number.")

    input("\nPress Enter to return to the menu...")    
    os.system("cls" if os.name == "nt" else "clear")

def main():
    addresses = load_address()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1;32mAddress Book\033[0m\n")
        print("1. View Addresses\n2. Exit\n")
        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            view_addresses(addresses)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again")
            sleep(1)

main()