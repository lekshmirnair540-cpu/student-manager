import os

FILE_NAME = "students.txt"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

# Add student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{age},{course}\n")

    print("✅ Student added successfully!\n")

# View all students
def view_students():
    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    if not data:
        print("No records found.\n")
        return

    print("\n📋 Student Records:")
    for line in data:
        name, age, course = line.strip().split(",")
        print(f"Name: {name}, Age: {age}, Course: {course}")
    print()

# Search student
def search_student():
    search_name = input("Enter name to search: ")

    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            name, age, course = line.strip().split(",")
            if search_name.lower() == name.lower():
                print(f"Found: Name: {name}, Age: {age}, Course: {course}\n")
                found = True

    if not found:
        print("❌ Student not found.\n")

# Menu
def main():
    while True:
        print("===== Student Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()