tasks = []

while True:
    print("\n=== TO DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Your Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(i, t)

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            print(i, t)
        index = int(input("Enter task number to remove: "))
        if 0 < index <= len(tasks):
            tasks.pop(index - 1)
            print("Task removed!")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
