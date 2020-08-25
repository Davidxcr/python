
global listStudents
listStudents = ["David", "Femi"]

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
    elif userInput == 3:
        searchStudent = input("Enter a student name to search: ")
        if searchStudent in listStudents:
            print("Record found of Student {}".format(searchStudent))
        else:
            print("No recored found of student {}".format(searchStudent))

    elif userInput == 4:
        removeStudent = input("Enter student name to remove: ")
        if removeStudent in listStudents:
            listStudents.remove(removeStudent)
            print("Student {} successfully removed".format(removeStudent))
            for students in listStudents:
                print("{}".format(students))
        else:
            print("No record found of this student {}".format(removeStudent))
    
    elif userInput < 1 or userInput > 4:
        print("Please enter a valid option")
    
manageStudent()

def runAgain():
    again = input("Do you want to run the program again Y/N: ")
    if runAgain.lower == 'y':
        manageStudent()
        runAgain()
    else:
        quit
    
runAgain()