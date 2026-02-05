"""
Task data model and operations for the Todo Console App.
"""

from typing import List, Optional


class Task:
    """Represents a single task in the todo list."""

    def __init__(self, task_id: int, description: str, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            description (str): Description of the task
            completed (bool): Completion status of the task (default: False)
        """
        self.id = task_id
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string showing task status and description
        """
        status = "+" if self.completed else "-"
        return f"[{status}] {self.id}. {self.description}"

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def update_description(self, new_description: str) -> None:
        """
        Update the task description.

        Args:
            new_description (str): New description for the task
        """
        self.description = new_description


class TodoList:
    """Manages a collection of tasks in memory."""

    def __init__(self):
        """Initialize an empty todo list."""
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task to the list.

        Args:
            description (str): Description of the new task

        Returns:
            Task: The newly created task
        """
        if not description.strip():
            raise ValueError("Task description cannot be empty")

        task = Task(self.next_id, description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list.

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update a task's description.

        Args:
            task_id (int): ID of the task to update
            new_description (str): New description for the task

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            if not new_description.strip():
                raise ValueError("Task description cannot be empty")
            task.update_description(new_description.strip())
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle a task's completion status.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            if task.completed:
                task.mark_incomplete()
            else:
                task.mark_complete()
            return True
        return False

    def is_empty(self) -> bool:
        """
        Check if the todo list is empty.

        Returns:
            bool: True if no tasks exist, False otherwise
        """
        return len(self.tasks) == 0