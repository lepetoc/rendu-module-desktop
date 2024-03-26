from tasks_manager import tasks_manager

def main():
    app = tasks_manager('tasks.json')

    while True:
        print("\nTasks:")
        for task_id, task_description in app.tasks.items():
            print(f"{task_id}: {task_description}")
        
        print("\nOptions:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_description = input("Enter task description: ")
            app.add_task(task_description)
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to delete: "))
                app.delete_task(task_id)
            except ValueError:
                print("Please enter a valid integer for the task ID.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()