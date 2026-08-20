from student_repo import Student_Repo # this will get repository class from student_repo
from student_service import Student_Service # service class will be implemented from student_service

def main():
    repo = Student_Repo() # I created this object to setup database connection and create table.
    service = Student_Service(repo)

    while True:  # I implemented the infinite loop that will end with an Exit choice.
        print("\nStudent Management System") # This is the title of the program
        print("1. Add Student") # From 1 to 4, these are the options
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ") #  user will enter their choice

        if choice == "1": # if user chooses choice 1
            try: # I used it to ensure that the program doesn't crash when errors occur
                student_id = int(input("Enter the student ID: ")) # user will enter the necessary
                name = input("Enter the student name: ")           # information
                age = int(input("Enter the student age: "))
                grade = float(input("Enter the student grade: "))
                message = service.add_student(student_id, name, age, grade)
                print(message)
            except ValueError: # when value is invalid
                print("Invalid input. Please enter the correct data type.") # this will show an error message

        elif choice == "2":   # if user chooses choice 2
            students = service.get_students() # this will get the service layer to retrieve the students
            if students:
                print("\nThe Student Records:") # I use this for the headline
                for student in students: # From the line below, this will output student's name age and  grade
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
            else:
                print("No students are found.")

        elif choice == "3":  # if user chooses choice 3
            try:
                student_id = int(input("Enter the student ID to delete: "))
                message = service.delete_student(student_id) # This will delete student from the database
                print(message)
            except ValueError:
                print("Invalid student ID.") # if input is invalid, it will output this

        elif choice == "4":  # if user chooses choice 4
            repo.close_connection()
            print("Exiting the system........")  # this will exit the program
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()