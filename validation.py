"""Validation helpers for the task management system."""

from datetime import datetime


def validate_task_name(task_name):
	"""Return True when task name is a non-empty string after trimming spaces."""
	if not isinstance(task_name, str):
		return False
	if len(task_name.strip()) == 0:
		return False
	return True


def validate_task_description(task_description):
	"""Return True when task description is a non-empty string."""
	if not isinstance(task_description, str):
		return False
	if len(task_description.strip()) == 0:
		return False
	return True


def validate_due_date(due_date):
	"""Return True when due_date is in YYYY-MM-DD format."""
	if not isinstance(due_date, str):
		return False
	if len(due_date.strip()) == 0:
		return False

	try:
		datetime.strptime(due_date.strip(), "%Y-%m-%d")
	except ValueError:
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


__all__ = [
	"validate_task_name",
	"validate_task_description",
	"validate_due_date",
	"validate_task_index",
]
