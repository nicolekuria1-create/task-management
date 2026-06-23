"""Validation helpers for the task management system."""


def validate_task_name(task_name):
    """Return True when task name is a non-empty string after trimming spaces."""
    if not isinstance(task_name, str):
        return False
    if len(task_name.strip()) == 0:
        return False
    return True


def validate_task_index(task_index, tasks):
    """Return True when task_index can reference an item in tasks."""
    if not isinstance(tasks, list):
        return False

    if not isinstance(task_index, int):
        return False

    if len(tasks) == 0:
        return False

    if task_index < 0 or task_index >= len(tasks):
        return False

    return True
