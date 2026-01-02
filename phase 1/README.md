# Todo Console App

A simple, feature-rich console-based todo application built in Python 3.13+.

## Features

- **Add Tasks**: Create new todo items with descriptions
- **View Tasks**: List all tasks with their completion status
- **Update Tasks**: Modify existing task descriptions
- **Delete Tasks**: Remove tasks from the list
- **Mark Task Complete**: Mark tasks as complete
- **Mark Task Incomplete**: Mark tasks as incomplete
- **In-Memory Storage**: All tasks stored in memory during runtime

## Requirements

- Python 3.13 or higher
- No external dependencies

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application with Python:

```bash
python src/main.py
```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Enter a new task description
2. **View Tasks**: Display all tasks with their status
3. **Update Task**: Modify an existing task by ID
4. **Delete Task**: Remove a task by ID
5. **Mark Task Complete**: Mark a task as complete
6. **Mark Task Incomplete**: Mark a task as incomplete
7. **Exit**: Quit the application

## Project Structure

```
├── src/                    # Source code files
│   ├── __init__.py         # Package initialization
│   ├── main.py             # Main application entry point
│   ├── todo.py             # Todo data model and operations
│   └── ui.py               # User interface logic
├── specs-history/          # Specification history
├── README.md              # Project documentation
├── CLAUDE.md              # Claude Code rules
└── constitution.md        # Project constitution
```

## Architecture

The application follows clean code principles with clear separation of concerns:

- **Data Layer**: Task models and in-memory storage
- **Business Logic**: Task operations and validation
- **Presentation Layer**: Console user interface

## License

This project is open source and available under the MIT License.