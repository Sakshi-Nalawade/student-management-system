
import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


# Add a new student
def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll_no, name, age, course)
        )
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Roll number already exists.")


# Display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"Roll No: {student[0]}, "
            f"Name: {student[1]}, "
            f"Age: {student[2]}, "
            f"Course: {student[3]}"
        )


# Search for a student
def search_student():
    roll_no = int(input("Enter Roll Number to search: "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )
    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
    else:
        print("Student not found.")


# Update student details
def update_student():
    roll_no = int(input("Enter Roll Number to update: "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    if cursor.fetchone():
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")

        cursor.execute("""
            UPDATE students
            SET name = ?, age = ?, course = ?
            WHERE roll_no = ?
        """, (name, age, course, roll_no))

        conn.commit()
        print("Student details updated successfully!")
    else:
        print("Student not found.")


# Delete a student
def delete_student():
    roll_no = int(input("Enter Roll Number to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll_no,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Student Management System.")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
