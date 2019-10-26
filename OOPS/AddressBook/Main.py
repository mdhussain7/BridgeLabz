from OOPS.AddressBook import AddressBook                                        # imorting sys module

if __name__ ==  '__main__':
    try:
        while True:
            address = AddressBook.AddressBook()                                # Assigning the object to address class
            op = int(input("Press \n 1. To Existing User 2. To New User 3. To Quit \n"))
            if op == 1:
                address.open() # opening the file
                choice = int(input(' Press \n 1. To Add new contact \n 2. To Delete\n 3. To Update address book\n'
                                   ' 4. To Print Book \n 5. To Sort by zipcode \n 6. To Sort by Name \n'
                                   ' 7. To Quit \n '))  # Asks user for input
                if choice == 1:
                    address.add()
                    print(" Data Added Successfully ")  # if user input is 1 the add a data
                elif choice == 2:
                    address.remove()
                    print(" Data Removed Successfully ")  # if user input is 2 then delete a data
                elif choice == 3:
                    address.update()
                    print(" Data Updated Successfully ")  # user input is 3 to update the data
                elif choice == 4:
                    address.display()
                    print(" Data is Currently Displaying ")  # user input is 4 to print the AddressBook
                elif choice == 5:
                    address.sort()
                    print(" Data is in Sortyed Manner ")  # user input is 5 to sort by zipcode
                elif choice == 6:
                    address.sortName()
                    print(" Data is Sorted By Name ")  # if user input is 6 to sort by name
                elif choice == 7:
                    print(" Bye User ")
                    exit()
            elif op == 2:
                address.create()                                       # creating the json file
                address.add()
            elif op == 3:
                exit()
    except KeyboardInterrupt:
        print("\nForce Quit ")
        print(" Bye ")
    except ValueError:
        print("Invalid Option")
