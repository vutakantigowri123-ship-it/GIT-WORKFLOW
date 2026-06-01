# task_manager.py
# A simple command-line task manager using loops

tasks = []

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            status = "✅ Done" if t["done"] else "❌ Not Done"
            print(f"{i}. {t['task']} - {status}")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num-1]["done"] = True
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid choice.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num-1)
        print(f"Task '{removed['task']}' deleted!")
    except (ValueError, IndexError):
        print("Invalid choice.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid option, try again.")
