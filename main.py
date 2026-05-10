students = []

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    # ADD STUDENT
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

    # VIEW STUDENTS
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

    # SEARCH STUDENT
    elif choice == "3":

        search_roll = input("Enter roll number to search: ")

        found = False

        for s in students:

            if s["roll"] == search_roll:

                print("\nStudent Found")
                print("Name:", s["name"])
                print("Roll:", s["roll"])
                print("Branch:", s["branch"])

                found = True
                break

        if not found:
            print("Student not found.")

    # DELETE STUDENT
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

    # UPDATE STUDENT
    elif choice == "5":

        update_roll = input("Enter roll number to update: ")

        found = False

        for s in students:

            if s["roll"] == update_roll:

                found = True

                print("\nStudent Found")
                print("-------------------")
                print("Current Name :", s["name"])
                print("Current Roll :", s["roll"])
                print("Current Branch :", s["branch"])

                # BEFORE UPDATE
                print("\nOld Data:")
                print(s)

                # UPDATE INPUTS
                new_name = input("Enter new name (press enter to skip): ")
                new_roll = input("Enter new roll number (press enter to skip): ")
                new_branch = input("Enter new branch (press enter to skip): ")

                # EMPTY VALIDATION + SKIP OPTION
                if new_name != "":
                    s["name"] = new_name

                if new_roll != "":
                    s["roll"] = new_roll

                if new_branch != "":
                    s["branch"] = new_branch

                # CONFIRMATION
                confirm = input("\nConfirm update? (y/n): ")

                if confirm.lower() == "y":

                    print("\nStudent updated successfully!")

                    # AFTER UPDATE
                    print("Updated Data:")
                    print(s)

                else:
                    print("Update cancelled.")

                break

        if not found:
            print("Student not found.")

    # EXIT
    elif choice == "6":

        print("Program closed.")
        break

    else:
        print("Invalid choice.")