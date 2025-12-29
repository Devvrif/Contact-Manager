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

    
def main():
    """ Main program loop """
    while True:
        print("\n=== CONTACT MANAGER")
        print("1. Add Contact")
        print("2. Show All")
        print("3. Search")
        print("4. Exit")

        choice = input("\nChoose (1-4): ")

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
            print("Goodbye!")
            break
                
        else:
            print("Invalid choice!")

#Run the program
if __name__ == "__main__":
    main()




