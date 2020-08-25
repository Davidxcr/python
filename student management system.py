global listStudents
listStudents = ["David Oluwafemi", "Femi Olatunji"]

def manageStudent():

    x = "#" * 30
    y = "=" * 28

    print("""
    
    Enter 1: To view Student's List
    Enter 2: To Add New Student
    Enter 3: To Search Student
    Enter 4 : To Remove or Delete Student

        """)

    try:
        userInput = int(input("Please select an option from the list above: "))

    except ValueError:
        exit("That's not a number")

    else:
        print("\n")

    
    if userInput == 1:
        print("List Students\n")
        for students in listStudents:
            print("{}".format(students))

    elif userInput == 2:
        newStudent = input("Please enter a new student full name: ")
        if newStudent in listStudents:
            print("\nThis student {} already exists in the Database".format(newStudent))

        else:
            listStudents.append(newStudent)
            print("New student {} added successfully\n".format(newStudent))
            for students in listStudents:
                print("{}".format(students))
