tasks = []


def add_task(description):
    task = {"id": len(tasks) + 1, "description": description, "status": "todo"}
    tasks.append(task)


def list_tasks():
    if not tasks:
        print("No tasks yet")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']}")


while True:
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        desc = input("Task: ").strip()
        if desc:
            add_task(desc)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
