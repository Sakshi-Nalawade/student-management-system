# Student Management System

## Description
The Student Management System is a simple console-based application developed using Python and SQLite. It helps users manage student records easily by performing basic operations such as adding, displaying, searching, updating, and deleting student information.

## Features
- **Add Student:** Add a new student with roll number, name, age, and course.
- **Display Students:** View all registered student records.
- **Search Student:** Search for a student using their roll number.
- **Update Student:** Modify the details of an existing student.
- **Delete Student:** Remove a student record from the database.
- **Data Persistence:** Student information is stored in an SQLite database.
- **Duplicate Prevention:** Prevents adding students with an existing roll number.

## Technologies Used
- **Programming Language:** Python
- **Database:** SQLite
- **Database Library:** Python's built-in `sqlite3` module
- **Version Control:** Git
- **Source Code Hosting:** GitHub

## Project Structure

```text
StudentManagementSystem/
├── main.py
├── README.md
├── .gitignore
├── LICENSE
└── students.db
```

**Note:** The `students.db` database file is created automatically when the program runs. It may be excluded from GitHub using `.gitignore`.

## Requirements
- Python 3 installed on your computer
- A code editor such as Visual Studio Code
- Git (for uploading the project to GitHub)

No additional Python packages are required because SQLite support is included with standard Python installations.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/student-management-system.git
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository URL.

### 2. Navigate to the Project Directory

```bash
cd student-management-system
```

### 3. Run the Application

```bash
python main.py
```

On some Windows systems, you may need to use:

```bash
py main.py
```

## How to Use

After running the program, a menu will appear:

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

Enter the number corresponding to the operation you want to perform and follow the instructions displayed on the screen.

### Example

To add a student, select option `1` and enter the required details:

```text
Enter Roll Number: 101
Enter Student Name: Rahul
Enter Age: 21
Enter Course: Computer Science

Student added successfully!
```

The student record is saved in the SQLite database and can be accessed later.

## Database Details

The application automatically creates a table named `students` with the following fields:

| Field | Description |
|---|---|
| `roll_no` | Unique student roll number and primary key |
| `name` | Student name |
| `age` | Student age |
| `course` | Student's course name |

## Learning Outcomes
- Understanding Python functions and conditional statements.
- Performing CRUD operations (Create, Read, Update, and Delete).
- Connecting Python applications to an SQLite database.
- Using SQL queries to manage student information.
- Managing project files and publishing source code using Git and GitHub.

## Future Enhancements
- Add a graphical user interface.
- Add input validation and better error handling.
- Add student attendance and marks management.
- Generate student reports.
- Introduce login and authentication features.

## License
This project is intended for educational purposes. See the `LICENSE` file in this repository for the applicable license terms.

## Author
**Your Name**

Developed as an academic project for learning Python, SQLite, and open-source software development.
