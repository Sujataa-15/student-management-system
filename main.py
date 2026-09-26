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


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting the program. Bye!")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
    