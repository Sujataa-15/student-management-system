# Student Management System

students = []  # this list stores all student records (list of dictionaries)


def add_student():
    """Add a new student"""
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
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

    # search through the list to find a matching student
    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            print(f"\n✅ Student with Roll No {roll_no} has been deleted.\n")
            return

    # this runs only if no match was found in the loop above
    print(f"\n⚠️ No student found with Roll No {roll_no}.\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting the program. Bye!")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()