tasks = []

def add_task():
    task = input("Enter task :")
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete :"))
        tasks.pop(index-1)
    except:
        print("Invalid input")

while True:
    print("\n1. Add task\n2. View task\n3.Delete task\n4.Exit")
    choice = input("Choose: ")

    if choice =="1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        delete_task()
    elif choice =="4":
        break
    else:
        print("Invalid choice")