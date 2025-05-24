import os

while True:
    choice = int(input("1. Add Contact \n2. View all Contacts \n3. Delete all Contacts \n4. Exit\n"))

    if choice == 1:
        name = input("Enter Name : ")
        number = input("Enter Number : ")  

        with open("contact.txt", "a") as f:
            f.write(f"{name} : {number}\n")

        print("Contact Saved Successfully!\n")

    elif choice == 2:
        try:
            with open("contact.txt", "r") as f:
                print("\nContacts List:")
                print(f.read())
                print("\n")
        except FileNotFoundError:
            print("No Contacts Found\n")

    elif choice == 3:
        try:
            os.remove("contact.txt")
            print("All Contacts Deleted Successfully!\n")
        except FileNotFoundError:
            print("No Contact File Found to Delete.\n")

    elif choice == 4:
        print("Good Bye!")  
        break

    else:
        print("Invalid Output\n")
