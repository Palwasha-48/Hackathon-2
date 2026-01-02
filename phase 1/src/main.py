"""
Main entry point for the Todo Console App.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo import TodoList
from ui import TodoUI


def main():
    """Initialize and run the Todo Console App."""
    # Create the todo list and user interface
    todo_list = TodoList()
    ui = TodoUI(todo_list)

    # Run the application
    ui.run()


if __name__ == "__main__":
    main()