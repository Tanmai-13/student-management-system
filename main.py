students = []

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        branch = input("Enter branch: ")

        student = {
            "name": name,
            "roll": roll,
            "branch": branch
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\nStudent Records:")

            for s in students:
                print("-------------------")
                print("Name:", s["name"])
                print("Roll:", s["roll"])
                print("Branch:", s["branch"])

    elif choice == "3":

        search_roll = input("Enter roll number to search: ")

        found = False

        for s in students:

            if s["roll"] == search_roll:

                print("\nStudent Found")
                print("Name:", s["name"])
                print("Branch:", s["branch"])

                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":

        delete_roll = input("Enter roll number to delete: ")

        found = False

        for s in students:

            if s["roll"] == delete_roll:

                students.remove(s)

                print("Student deleted successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":

        print("Program closed.")
        break

    else:
        print("Invalid choice.")    