"""Utility functions for task operations."""

from task_manager.validation import (
    validate_due_date,
    validate_task_description,
    validate_task_index,
    validate_task_name,
)


def add_task(tasks, task_name, task_description="", due_date=""):
    """Add a new pending task to the list."""
    if not validate_task_name(task_name):
        return False

    if not validate_task_description(task_description):
        return False

    if not validate_due_date(due_date):
        return False

    task = {
        "name": task_name.strip(),
        "description": task_description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return True


def mark_task_complete(tasks, task_number):
    """Mark the selected task as complete."""
    task_index = task_number - 1

    if not validate_task_index(task_index, tasks):
        return False

    tasks[task_index]["completed"] = True
    return True


def get_pending_tasks(tasks):
    """Return all pending tasks."""
    return [task for task in tasks if not task.get("completed", False)]


def get_progress(tasks):
    """Return a tuple: (completed_count, total_count, percent_complete)."""
    total_count = len(tasks)

    if total_count == 0:
        return 0, 0, 0.0

    completed_count = sum(1 for task in tasks if task.get("completed", False))
    percent_complete = (completed_count / total_count) * 100

    return completed_count, total_count, percent_complete
