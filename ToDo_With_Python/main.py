print("📝 Smart To-Do List")

tasks = []

while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("❌ No tasks to remove")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑 Removed: {removed}")
            else:
                print("⚠ Invalid task number")

    elif choice == "4":
        print("👋 Exiting To-Do List. Bye!")
        break

    else:
        print("⚠ Invalid choice. Try again.")
