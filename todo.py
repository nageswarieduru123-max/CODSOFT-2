students = []

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                students.append(line.strip())
    except FileNotFoundError:
        pass

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

def view_students():
    if len(students) == 0:
        print("\nNo student records found.")
    else:
        print("\n----- Student Records -----")
        for i in range(len(students)):
            print(f"{i+1}. {students[i]}")

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    save_students()
    print("Student added successfully!")

def update_student():
    view_students()
    if len(students) == 0:
        return
    try:
        n = int(input("Enter student number to update: "))
        if 1 <= n <= len(students):
            students[n-1] = input("Enter new student name: ")
            save_students()
            print("Student updated successfully!")
        else:
            print("Invalid student number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_student():
    view_students()
    if len(students) == 0:
        return
    try:
        n = int(input("Enter student number to delete: "))
        if 1 <= n <= len(students):
            removed = students.pop(n-1)
            save_students()
            print(f"{removed} deleted successfully!")
        else:
            print("Invalid student number.")
    except ValueError:
        print("Please enter a valid number.")

load_students()

while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
