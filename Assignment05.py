# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   mkeel, Michael Keel,05/21/2025,Created Script
# ------------------------------------------------------------------------------------------ #
import json

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

#Below pulled straight from Lab02 for r op to .json
try:
    file = open(FILE_NAME, 'r')
    students=json.load(file)
    file.close()
except Exception as e:
    #I think this prompt is the minimum for most cases of errors
    print(e)
    print('An error occurred while attempting to read the .json file')
    print(e.__doc__)
    print(e.__str__())
    #Not positive all of these are necessary
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            #pulled from Lab03
            if not student_first_name.isalpha():
                raise ValueError('Response must be in alphabet characters only')
            if not student_first_name:
                raise ValueError('Response cannot be null entry')
            #probably more error handling could/should be added here?

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError('Response must be in alphabet characters only')
            if not student_last_name:
                raise ValueError('Response cannot be null entry')

            course_name = input("Please enter the name of the course: ").strip()
            #Also pulled from Lab03
            student_data = {
                "firstName":student_first_name,
                "lastName":student_last_name,
                "courseName":course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            print(e)
            print('An error occurred with the input data')
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["firstName"]}"
                  f"{student["lastName"]}"
                  f" is enrolled in {student["courseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student["firstName"]}"
                  f"{student["lastName"]}"
                  f" is enrolled in {student["courseName"]}")
        except Exception as e:
            if file.closed == False:
                file.close()
            print('Error: Unable to write to file')
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
