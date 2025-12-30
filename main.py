def add_contact(name, phone):
    """ Add a contact to the file """
    with open("contact.txt", "a") as f:
        f.write(f"{name}, {phone}\n")
    print(f"✅ Added: {name}")

def show_all_contacts():
    """Display all contacts"""
    try:
        with open("contact.txt", "r") as f:
            lines = f.readlines()

        if not lines:
            print("No contacts yet!")
            return 
        
        print("\n---All Contacts---")
        for line in lines:
            name, phone = line.strip().split(",")
            print(f"{name}: {phone}")

    except FileNotFoundError:
            print("No contacts yet!")

def search_contact(search_term):
    """ Search for a contact """
    try:
        with open("contact.txt", "r") as f:
            lines = f.readlines()

        found = False 
        for line in lines:
            name, phone = line.strip().split(",")
            if search_term.lower() in name.lower():
                print(f"Found {name} - {phone}")
                found = True 
        
        if not found:
            print(f"No match for: {search_term}")

    except FileNotFoundError:
        print("No contacts to search")

def delete_contact(search_term):
    """ Delete a contact """
    try:
        with open("contact.txt", "r") as f:
            lines = f.readlines()

        matches = []
        for i, line in enumerate(lines):
            name, phone = line.strip().split(", ")
            if search_term.lower() in name.lower():
                matches.append((i, name, phone))
        
        if not matches:
            print(f"No match found for the {search_term}")
        
        else: print("Matches Found: ")

        for idx, (line_index, name, phone) in enumerate(matches, 1):
            print(f"{idx}, {name}, {phone}")

        choice = input("Enter the number of the contact to be deleted (0 to cancel): ")

        if not choice.isdigit():
            print("Invalid input!")
            return
        choice = int(choice)

        if choice == 0:
            return
        
        elif choice < 1 or choice > len(matches):
            print("Invalid choice")
            return 
        
        line_index_to_delete = matches[choice - 1][0]
        name, phone = matches[choice - 1][1], matches[choice - 1][2]

        confirm = input(f"Are you sure to delete the selected contact permanently (y/n): )").lower().strip()
        if confirm != "y":
            print("Deletetion Cancelled")
            return 
        
        else:
            lines.pop(line_index_to_delete)
            print(f"{name}-{phone} has be deleted successfully!")

        with open("contact.txt", "w") as f:
            for line in lines:
                f.write(line)

    except FileNotFoundError:
        print("No contacts to found")

def main():
    """ Main program loop """
    while True:
        print("\n=== CONTACT MANAGER")
        print("1. Add Contact")
        print("2. Show All")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")

        choice = input("\nChoose (1-5): ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(name, phone)
            
        elif choice == "2":
            show_all_contacts()
            
        elif choice == "3":
            search_term = input("Search for: ")
            search_contact(search_term)

        elif choice == "4":
            search_term = input("Enter name to delete: ")
            delete_contact(search_term)

        elif choice == "5":
            print("Goodbye!")
            break
                
        else:
            print("Invalid choice!")

#Run the program
if __name__ == "__main__":
    main()




