# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display all tasks
def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print()

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!\n")

# Function to delete a task
def delete_task():
    show_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Main function to run the To-Do List app
def main():
    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the main function
if __name__ == "__main__":
    main()
