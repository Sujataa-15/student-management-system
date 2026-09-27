# Student Management System

A beginner Python project to manage student records — built as a console (terminal-based) application.

## Features

- **Add Student** — add a new student with Roll Number, Name, and Marks (with input validation)
- **View All Students** — display the full list of students
- **Delete Student** — remove a student using their Roll Number
- **Update Student** — edit a student's Name or Marks
- **Search Student** — find a student by Roll Number or Name
- **Permanent Storage** — all data is saved in `students.json`, so it stays even after closing the program

## Input Validation

- Roll Number, Name, and Marks cannot be left empty
- Roll Number must be numeric and unique (no duplicates)
- Name must contain only letters
- Marks must be numeric

## How to Run

1. Clone this repository:
   ```
   git clone https://github.com/Sujataa-15/student-management-system.git
   ```
2. Navigate into the project folder:
   ```
   cd student-management-system
   ```
3. Run the program:
   ```
   python main.py
   ```

## Tech Used

- Python 3
- JSON (for data storage)

## Author

Sujata