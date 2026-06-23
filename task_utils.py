"""Compatibility wrapper for task utility helpers."""

from task_manager.task_utils import add_task, get_pending_tasks, get_progress, mark_task_complete

__all__ = [
    "add_task",
    "mark_task_complete",
    "get_pending_tasks",
    "get_progress",
]
