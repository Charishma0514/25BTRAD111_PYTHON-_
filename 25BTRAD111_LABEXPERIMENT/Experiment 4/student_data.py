import os

filename = "students.txt"

while True:
    print("\nSTUDENT DATA MANAGER")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        with open(filename, "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print("\nStudent Records:")
                print(file.read())
        else:
            print("No student records found!")

    elif choice == "3":
        search = input("Enter Roll Number to search: ")
        found = False

        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if data[0] == search:
                        print("Student Found:", data)
                        found = True

        if not found:
            print("Student not found!")

    elif choice == "4":
        search = input("Enter Roll Number to update: ")
        found = False
        records = []

        if os.path.exists(filename):
            with open(filename, "r") as file:
                records = file.readlines()

            with open(filename, "w") as file:
                for line in records:
                    data = line.strip().split(",")

                    if data[0] == search:
                        name = input("Enter New Name: ")
                        marks = input("Enter New Marks: ")
                        line = search + "," + name + "," + marks + "\n"
                        found = True

                    file.write(line)

        if found:
            print("Student record updated!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
