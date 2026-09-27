# Student Management System

import json

FILE_NAME = "students.json"  # data will be permanently saved in this file

students = []  # this list stores all student records (list of dictionaries)


def load_students():
    """Load saved students from the file when the program starts"""
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def save_students():
    """Save the current students list into the file"""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def roll_number_exists(roll_no):
    """Check if a roll number is already used by another student"""
    for s in students:
        if s["roll_no"] == roll_no:
            return True
    return False


def add_student():
    """Add a new student, with validation checks"""

    # keep asking until a valid, numeric, non-empty, non-duplicate roll number is given
    while True:
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no == "":
            print("⚠️ Roll Number cannot be empty. Try again.")
        elif not roll_no.isdigit():
            print("⚠️ Roll Number must be a number. Try again.")
        elif roll_number_exists(roll_no):
            print(f"⚠️ Roll Number {roll_no} already exists. Try a different one.")
        else:
            break

    # keep asking until a valid name (letters and spaces only) is given
    while True:
        name = input("Enter Name: ").strip()
        if name == "":
            print("⚠️ Name cannot be empty. Try again.")
        elif not name.replace(" ", "").isalpha():
            print("⚠️ Name should only contain letters. Try again.")
        else:
            break

    # keep asking until marks is a valid number
    while True:
        marks = input("Enter Marks: ").strip()
        if marks.isdigit():
            break
        else:
            print("⚠️ Marks must be a number. Try again.")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()
    print(f"\n✅ {name} has been added successfully!\n")


def view_students():
    """Display all students"""
    if len(students) == 0:
        print("\n⚠️ No students have been added yet.\n")
        return

    print("\n----- Students List -----")
    for s in students:
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Marks: {s['marks']}")
    print("--------------------------\n")


def delete_student():
    """Delete a student using their roll number"""
    if len(students) == 0:
        print("\n⚠️ No students to delete.\n")
        return

    roll_no = input("Enter Roll Number of the student to delete: ")

    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            save_students()
            print(f"\n✅ Student with Roll No {roll_no} has been deleted.\n")
            return

    print(f"\n⚠️ No student found with Roll No {roll_no}.\n")


def update_student():
    """Update an existing student's name or marks using their roll number"""
    if len(students) == 0:
        print("\n⚠️ No students to update.\n")
        return

    roll_no = input("Enter Roll Number of the student to update: ")

    for s in students:
        if s["roll_no"] == roll_no:
            print(f"Current Name: {s['name']}, Current Marks: {s['marks']}")

            new_name = input("Enter new Name (leave blank to keep same): ").strip()

            # keep asking for marks until it's valid, or left blank
            while True:
                new_marks = input("Enter new Marks (leave blank to keep same): ").strip()
                if new_marks == "" or new_marks.isdigit():
                    break
                else:
                    print("⚠️ Marks must be a number. Try again.")

            if new_name != "":
                s["name"] = new_name
            if new_marks != "":
                s["marks"] = new_marks

            save_students()
            print(f"\n✅ Student with Roll No {roll_no} has been updated.\n")
            return

    print(f"\n⚠️ No student found with Roll No {roll_no}.\n")


def search_student():
    """Search for a student by roll number or name"""
    if len(students) == 0:
        print("\n⚠️ No students to search.\n")
        return

    keyword = input("Enter Roll Number or Name to search: ")
    found = False

    for s in students:
        if s["roll_no"] == keyword or s["name"].lower() == keyword.lower():
            print("\n----- Student Found -----")
            print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Marks: {s['marks']}")
            print("--------------------------\n")
            found = True

    if not found:
        print(f"\n⚠️ No student found matching '{keyword}'.\n")


def main():
    load_students()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting the program. Bye!")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.\n")


if __name__ == "__main__":
    main()