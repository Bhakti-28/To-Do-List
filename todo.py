# Import required modules
import json
import os

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(SCRIPT_DIR, 'tasks.json')

# Function to load tasks from file
def load_tasks():
    try:
        # Try to open and read the tasks file
        with open(TASKS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Warning: tasks.json was empty or invalid. Starting with empty task list.")
                return []
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        print("Note: Creating new tasks.json file.")
        return []

# Function to save tasks to file
def save_tasks(tasks):
    try:
        # Open file in write mode and save tasks
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)  # Added indent for better readability
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Function to add a new task
def add_task(tasks):
    # Get task from user
    task = input("Enter your task: ").strip()
    if task:  # Only add non-empty tasks
        # Add task to list
        tasks.append({"task": task, "done": False})
        # Save tasks to file
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:  # If tasks list is empty
        print("No tasks found!")
        return
    
    # Print each task with its number
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['task']}")

# Function to mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:  # If no tasks exist
        return
    
    # Get task number from user
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:  # If no tasks exist
        return
    
    # Get task number from user
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num-1)
            save_tasks(tasks)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program
def main():
    # Load existing tasks when program starts
    tasks = load_tasks()
    
    while True:
        # Show menu
        print("\n=== Todo List Menu ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ")
        
        # Process user choice
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the Todo List!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start the program
if __name__ == "__main__":
    main() 