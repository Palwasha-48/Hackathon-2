"""
User interface for the Todo Console App.
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo import TodoList


class TodoUI:
    """Handles user interface and input/output operations."""

    def __init__(self, todo_list: TodoList):
        """
        Initialize the user interface.

        Args:
            todo_list (TodoList): The todo list to manage
        """
        self.todo_list = todo_list

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\nTodo Console App")
        print("================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print()

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's choice
        """
        return input("Enter your choice: ").strip()

    def display_tasks(self) -> None:
        """Display all tasks in the list."""
        if self.todo_list.is_empty():
            print("\nNo tasks available.")
            return

        print("\nTasks:")
        for task in self.todo_list.get_all_tasks():
            print(task)

    def add_task_ui(self) -> None:
        """Handle adding a new task through the UI."""
        description = input("\nEnter task description: ").strip()

        try:
            task = self.todo_list.add_task(description)
            print(f"Task '{task.description}' added successfully with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def update_task_ui(self) -> None:
        """Handle updating a task through the UI."""
        if self.todo_list.is_empty():
            print("\nNo tasks available to update.")
            return

        self.display_tasks()
        try:
            task_id = int(input("\nEnter task ID to update: "))
            new_description = input("Enter new description: ").strip()

            if self.todo_list.update_task(task_id, new_description):
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Task with ID {task_id} not found")
        except ValueError:
            print("Invalid input. Please enter a valid task ID (number).")

    def delete_task_ui(self) -> None:
        """Handle deleting a task through the UI."""
        if self.todo_list.is_empty():
            print("\nNo tasks available to delete.")
            return

        self.display_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: "))

            if self.todo_list.delete_task(task_id):
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Task with ID {task_id} not found")
        except ValueError:
            print("Invalid input. Please enter a valid task ID (number).")

    def mark_task_complete_ui(self) -> None:
        """Handle marking a task as complete through the UI."""
        if self.todo_list.is_empty():
            print("\nNo tasks available to mark.")
            return

        self.display_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark complete: "))

            task = self.todo_list.get_task(task_id)
            if task:
                if not task.completed:
                    task.mark_complete()
                    print(f"Task {task_id} marked as complete")
                else:
                    print(f"Task {task_id} is already complete")
            else:
                print(f"Task with ID {task_id} not found")
        except ValueError:
            print("Invalid input. Please enter a valid task ID (number).")

    def mark_task_incomplete_ui(self) -> None:
        """Handle marking a task as incomplete through the UI."""
        if self.todo_list.is_empty():
            print("\nNo tasks available to mark.")
            return

        self.display_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark incomplete: "))

            task = self.todo_list.get_task(task_id)
            if task:
                if task.completed:
                    task.mark_incomplete()
                    print(f"Task {task_id} marked as incomplete")
                else:
                    print(f"Task {task_id} is already incomplete")
            else:
                print(f"Task with ID {task_id} not found")
        except ValueError:
            print("Invalid input. Please enter a valid task ID (number).")

    def run(self) -> None:
        """Run the main application loop."""
        print("Welcome to Todo Console App!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task_ui()
            elif choice == "2":
                self.display_tasks()
            elif choice == "3":
                self.update_task_ui()
            elif choice == "4":
                self.delete_task_ui()
            elif choice == "5":
                self.mark_task_complete_ui()
            elif choice == "6":
                self.mark_task_incomplete_ui()
            elif choice == "7":
                print("\nThank you for using Todo Console App. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-7.")