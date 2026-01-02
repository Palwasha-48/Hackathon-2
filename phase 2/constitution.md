# Todo Web App Constitution - Phase II

## Core Principles

### I. Full-Stack Architecture
The application must follow a proper full-stack architecture with clear separation between frontend and backend. The frontend (Next.js) handles user interface and user experience, while the backend (FastAPI) manages business logic and data persistence.

### II. RESTful API Design
All communication between frontend and backend must follow RESTful principles with properly designed endpoints, HTTP methods, and status codes. APIs must be consistent, predictable, and well-documented.

### III. Database-Driven Data Storage
All tasks must be stored in a persistent database (Neon Serverless PostgreSQL) with proper schema design, relationships, and indexing. The application must maintain data integrity and provide efficient data access.

### IV. User Authentication and Authorization
The system must implement proper user authentication using Better Auth with JWT tokens. Each user should only access their own data, with proper authorization checks on all endpoints.

### V. Complete CRUD Functionality
The application must implement full Create, Read, Update, Delete operations for tasks with proper validation, error handling, and user feedback on both frontend and backend.

### VI. Responsive User Interface
The frontend must provide a responsive, user-friendly interface that works well on different screen sizes. The UI should be intuitive and provide good user experience.

## Additional Requirements

### Technology Stack
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- Backend: Python FastAPI, SQLModel ORM, Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens
- Spec-Driven: Claude Code + Spec-Kit Plus

### Database Schema
- Users table (managed by Better Auth)
- Tasks table with user_id foreign key, title, description, completed status, timestamps
- Proper indexing for efficient queries

### Security Standards
- JWT token validation on all protected endpoints
- User data isolation - users can only access their own tasks
- Input validation and sanitization
- Proper error handling without exposing internal details

## Development Workflow

### Implementation Standards
- Follow Next.js best practices for frontend development
- Follow FastAPI best practices for API development
- Use SQLModel for database operations
- Implement proper TypeScript types
- Follow REST API design principles

### Quality Gates
- All API endpoints work correctly with proper authentication
- Frontend communicates properly with backend
- User authentication and authorization work correctly
- Database operations are efficient and secure
- Responsive UI works across different devices

## Governance

This constitution defines the mandatory practices for the Todo Web App project. All implementations must comply with these principles. Changes to this constitution require explicit approval and documentation of the rationale for changes.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02