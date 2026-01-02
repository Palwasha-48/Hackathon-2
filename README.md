# Hackathon II - Todo Spec-Driven Development

This repository contains the implementation of the Hackathon II project, evolving a simple todo console app into a cloud-native AI system across 5 phases.

## Project Structure

```
h-3_2/
├── .claude/                 # Claude Code configuration
├── .specify/                # Spec-Kit Plus configuration
├── pdf.txt                  # Text content of Hackathon II PDF
├── README.md               # This file
├── phase 1/                # Phase I: Todo In-Memory Python Console App
│   ├── constitution.md     # Project principles for Phase I
│   ├── spec.md            # Specification for Phase I
│   ├── plan.md            # Implementation plan for Phase I
│   ├── tasks.md           # Task breakdown for Phase I
│   ├── src/               # Source code for Phase I
│   │   ├── main.py        # Main application entry point
│   │   ├── todo.py        # Task data model and operations
│   │   └── ui.py          # User interface logic
│   ├── specs-history/     # Historical specification files
│   ├── test_todo_app.py   # Test suite for Phase I
│   ├── requirements.txt   # Python dependencies
│   ├── CLAUDE.md          # Claude Code instructions
│   └── README.md          # Phase I documentation
└── phase 2/                # Phase II: Todo Full-Stack Web Application
    ├── constitution.md     # Project principles for Phase II
    ├── spec.md            # Specification for Phase II
    ├── plan.md            # Implementation plan for Phase II
    ├── tasks.md           # Task breakdown for Phase II
    ├── backend/           # FastAPI backend implementation
    │   ├── main.py        # Backend entry point
    │   ├── database.py    # Database configuration
    │   ├── auth.py        # Authentication middleware
    │   ├── models/        # Database models
    │   ├── routes/        # API routes
    │   └── requirements.txt # Python dependencies
    ├── frontend/          # Next.js frontend implementation
    │   ├── app/           # Next.js app router pages
    │   ├── components/    # UI components
    │   ├── lib/           # Utility functions
    │   ├── types/         # TypeScript definitions
    │   ├── public/        # Static assets
    │   └── package.json   # Node.js dependencies
    └── README.md          # Phase II documentation
```

## Phases Overview

### Phase I: Todo In-Memory Python Console App
- Command-line interface for managing todos
- In-memory storage during runtime
- Core CRUD operations (Add, View, Update, Delete, Mark Complete)
- Clean architecture with separation of concerns
- Comprehensive test suite

### Phase II: Todo Full-Stack Web Application
- Next.js frontend with responsive design
- FastAPI backend with RESTful API
- Neon Serverless PostgreSQL database
- User authentication with Better Auth
- JWT-based authorization
- Full CRUD operations with persistent storage

## Getting Started

### Phase I Setup
1. Navigate to Phase I directory:
   ```bash
   cd phase 1
   ```

2. Run the console application:
   ```bash
   python src/main.py
   ```

3. Run tests:
   ```bash
   python test_todo_app.py
   ```

### Phase II Setup
1. Navigate to Phase II directory:
   ```bash
   cd phase 2
   ```

2. Backend setup:
   ```bash
   cd backend
   # Follow Phase II backend setup instructions
   ```

3. Frontend setup:
   ```bash
   cd frontend
   # Follow Phase II frontend setup instructions
   ```

## Technologies Used

### Phase I
- Python 3.13+
- Standard library only (no external dependencies)

### Phase II
- Frontend: Next.js 16+, TypeScript, Tailwind CSS
- Backend: Python FastAPI, SQLModel, Neon PostgreSQL
- Authentication: Better Auth with JWT
- Spec-Driven: Claude Code + Spec-Kit Plus

## Spec-Driven Development

This project follows a spec-driven development approach:
1. Define specifications (constitution.md, spec.md)
2. Create implementation plan (plan.md)
3. Break into tasks (tasks.md)
4. Implement based on specifications

## Contributing

1. Follow the spec-driven development workflow
2. Update specifications before implementing changes
3. Create plans for new features
4. Break implementations into testable tasks

## License

This project is open source and available under the MIT License.