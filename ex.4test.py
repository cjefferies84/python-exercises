def get_phrase(choice):
    while choice != "3":
        phrase = raw_input("Enter a phrase: \t\n")
        if choice == "1":
            # write file phrase to file
            with open('sleepyTurtles.txt', 'w') as f:
                f.write(phrase)

            print("You entered:\t\n")
            with open('sleepyTurtles.txt', 'r') as f:
                for line in f:
                    print line
            menu()

        elif choice == "2":
            print("You entered:\t\n")
            print phrase
            menu()

    if choice == "3":
        print "You have selected to quit the program, good day"
        quit()


def menu():

    # user chooses a number from list
    print "*********************************\t\n"
    print"Exercise 4 - MENU\t\n"
    print"1. Write input to a file\t\n"
    print"2. Write output to a file\t\n"
    print"3. Quit\t\n"
    print"*********************************\t\n"

    print"*********************************\t\n"

    choice = raw_input("Enter menu choice: [1 - 3]\t\n")
    get_phrase(choice)

menu()

# get file choice from user















