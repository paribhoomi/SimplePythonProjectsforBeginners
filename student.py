def student_manager():
    students = {}

    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice")

        if choice == "1":
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            students[name] = marks

        elif choice == "2" :
            for name,marks in students.items():
                grade ="Pass" if marks >= 40 else "Fail"
                print(f"{name}: {marks} ({grade})")

        elif choice == "3":
            break

        else: 
            print("Invalid choice")


student_manager()