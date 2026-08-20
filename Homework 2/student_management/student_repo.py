import sqlite3 # I use this to imprt in SQLite libary

class Student_Repo: # I use this as the data access layer
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self): #using notes from class and online, this will immediately create a table for students
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_student(self, student):  # It will take a student as a object into the database
        self.cursor.execute("""
            INSERT INTO students (student_id, name, age, grade)
            VALUES (?, ?, ?, ?)""",
         (student.student_id, student.name, student.age, student.grade))
        self.conn.commit() # it will saves the student permanently.

    def get_students(self): # this will get all students from the database
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def delete_student(self, student_id): # This method would delete student by using Student ID
        self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.conn.commit()

    def close_connection(self): # it will close the database connection
        self.conn.close()        # permanently