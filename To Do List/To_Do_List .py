todo_list = []


def menu ():
    while(True):
        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter Your Choice :  ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Please enter a valid choice (1-5).")

def add_task():
    task = input("Enter a Task :  ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New task Added Successfully ! \n")


def view_tasks():
    print("Your To-Do List :  ")
    if len(todo_list) == 0:
        print("No Pending Tasks")
    else:
        for index, task in enumerate(todo_list,1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

def remove_task():
    if len(todo_list)==0:
        print("List is empty !")
    else:
        search_index = int(input("Enter the Task Number that You Want to Remove :  " )) - 1
    

            
