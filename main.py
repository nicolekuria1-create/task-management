"""CLI entrypoint for the task management system."""

from task_manager.task_utils import (
    add_task,
    get_pending_tasks,
    get_progress,
    mark_task_complete,
)


def display_menu():
    """Print the available actions."""
    print("\nTask Management System")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")


def display_all_tasks(tasks):
    """Print all tasks with their status."""
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")


def run_task_manager():
    """Run the main application loop."""
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task_name = input("Enter task name: ")
            if add_task(tasks, task_name):
                print("Task added successfully")
            else:
                print("Invalid task name. Please enter a non-empty value.")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available to mark as complete.")
                continue

            display_all_tasks(tasks)
            task_number_input = input("Enter task number to mark complete: ").strip()

            if not task_number_input.isdigit():
                print("Invalid task number.")
                continue

            task_number = int(task_number_input)
            if mark_task_complete(tasks, task_number):
                print("Task marked as complete")
            else:
                print("Task number out of range.")

        elif choice == "3":
            pending_tasks = get_pending_tasks(tasks)

            if len(pending_tasks) == 0:
                print("No working currently")
            else:
                print("Pending tasks:")
                for index, task in enumerate(pending_tasks, start=1):
                    print(f"{index}. {task['name']}")

        elif choice == "4":
            completed, total, percent = get_progress(tasks)
            print(f"Progress: {completed}/{total} tasks completed ({percent:.2f}%).")

        elif choice == "5":
            print("Exiting task manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    run_task_manager()
