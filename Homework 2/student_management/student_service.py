from student import Student # I am importing Student class from student.py

class Student_Service: # this is the service layer with the implementation of the business logic layer
    def __init__(self, repo):
        self.repo = repo # this will call the repository methods

    def add_student(self, student_id, name, age, grade):
        if age <= 15: # this will check if the age is invalid
            return "Age must be greater than 15 years old." # if not, prints this error message

        if grade <= 70:
            return "Grade must be greater than grade level 70."

        student = Student(student_id, name, age, grade)
        self.repo.add_student(student) # this will send object to repository layer to store in the database
        return "Student is added successfully."

    def get_students(self):
        return self.repo.get_students() # I use this to get result from repository

    def delete_student(self, student_id):
        self.repo.delete_student(student_id) # calls repository layer to delete student from the database
        return "Student is deleted successfully."