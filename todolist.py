import os
import json

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {'Done' if task['done'] else 'Not done'}")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to mark a task as done
def mark_task_done(tasks):
    display_tasks(tasks)
    idx = int(input("Enter the number of the task to mark as done: ")) - 1
    tasks[idx]["done"] = True
    save_tasks(tasks)
    print("Task marked as done!")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    idx = int(input("Enter the number of the task to delete: ")) - 1
    del tasks[idx]
    save_tasks(tasks)
    print("Task deleted successfully!")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("\nEnter your choice: ")
1
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
