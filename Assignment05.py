# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   David Goldberg, 5/15/2024, Attempt at Assignment 05
# ------------------------------------------------------------------------------------------ #


# Imports 
import json     # Importing the json



# Define the Data Constants
MENU: str = '''     
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict = []     # Dictionary that will hold keys and associated variables
students: list = []     # list that contains lists of the student's inputs

try:
    # read through file to input previous entries
    file = open(FILE_NAME, 'r')     # open the file in read mode
    students = json.load(file)      # load the previous dictionaries from the json file
    print("\n")
    print(students)
    print("\n")
    file.close()
except FileNotFoundError as e:      # Structured error handling if the file is not found      
    print(e)
    print('''
          This file does not exist or not previous data has been inputted
          ''')        # Should I also open the file
finally:
    print("\t"'This code will execute whether you have the file or not')        # will print this no matter the outcome

    # While loop that will loop while true
    while (True):

        # Present the menu of choices
        print(MENU)
        menu_choice = input("What would you like to do: ") # Will ask to choose from the menu

        # Input user data
        if menu_choice == "1": 
            try:
                student_first_name = input("Enter the student's first name: ")      # input first name
                student_last_name = input("Enter the student's last name: ")        # input last name
                if not student_first_name.isalpha() or not student_last_name.isalpha:       # check if the first name or last name has a non-alphabetic input
                    raise ValueError('''
                                     inputted names can only use letters
                                     ''')       # Will output a Value Error
            except ValueError as e:     # Structured error handling if the input is non-alphabetic
                print(e)
                print('''
                      enter a valid name that only uses the alphabet
                      ''')
                continue
            course_name = input("Please enter the name of the course: ")        # input course name
            student_data = {"first_name":student_first_name, "last_name":student_last_name, "course":course_name}       # create a dictionary with appropriate keys
            students.append(student_data)       # append each dictionary at a list
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")      # print a string to the user with their inputs
            print('''
                Saved!
                ''')
            

        # Present the current data
        elif menu_choice == "2":

             # Process the data to create and display a custom message
             print("-"*50)
             for entry in students:     # loop through each entry in the dictionary
                 print(f"Student {entry["first_name"]} {entry["last_name"]} is enrolled in {entry["course"]}")      # pull each key from the dictionary    
                 print("-"*50)
            

        # Save the data to a file
        elif menu_choice == "3":
            try:
                file = open(FILE_NAME, 'w')     # open a file to write to 
                json.dump(students, file)       # write the dictionary/dictionaries to the json file
                file.close()        # close the file
            except Exception as e:      # Structured error handling if any exceptions occur
                print(e, e.__doc__)
                print(f"An unexpected error occurred: {e}")
            finally:
                if file.closed == False:
                    file.close()        # close/save file 
            print('''
                  Saved to file 
                  ''')

        # Stop the loop
        elif menu_choice == "4":
            break  # out of the loop   

        else:
            print("Please only choose option 1, 2, or 3")

    print("Program Ended")
