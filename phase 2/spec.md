# Todo Web App - Phase II Specification

## 1. Overview

### Purpose
A modern, full-stack web application that allows users to manage their tasks through a responsive web interface. The application will provide all essential todo management features with persistent storage and user authentication.

### Scope
- Create, read, update, delete tasks via web interface
- User authentication and authorization using Better Auth
- Persistent storage in Neon Serverless PostgreSQL database
- Responsive web interface using Next.js
- RESTful API endpoints with JWT authentication

### Out of Scope
- Mobile app native development
- Email notifications
- Advanced analytics
- Third-party integrations
- Offline functionality

## 2. Functional Requirements

### 2.1 User Authentication
- User can sign up with email and password
- User can sign in with existing credentials
- User can sign out of the application
- JWT tokens issued upon successful authentication
- Sessions managed by Better Auth

### 2.2 Add Task
- Authenticated user can add a new task with title and description
- Task is stored in the database with user association
- Task has a unique ID and "incomplete" status by default
- Validation: Title is required (1-200 characters), description is optional (max 1000 characters)

### 2.3 View Tasks
- Authenticated user can view all their tasks with status (complete/incomplete)
- Tasks displayed with ID, status, title, and description
- Support for filtering by status (all, pending, completed)
- Support for sorting by creation date, title, or due date

### 2.4 Update Task
- Authenticated user can update a task title and description by ID
- Validation: Task must exist and belong to the user, title cannot be empty
- Error handling for invalid task IDs or unauthorized access

### 2.5 Delete Task
- Authenticated user can delete a task by ID
- Error handling for invalid task IDs or unauthorized access

### 2.6 Mark Complete/Incomplete
- Authenticated user can toggle task completion status by ID
- Error handling for invalid task IDs or unauthorized access
- Clear indication of status change

## 3. Non-Functional Requirements

### 3.1 Performance
- API responses under 500ms for typical operations
- Page load times under 2 seconds
- Efficient database queries with proper indexing

### 3.2 Security
- JWT token validation on all protected endpoints
- User data isolation - users can only access their own tasks
- Input validation and sanitization
- Secure authentication with Better Auth

### 3.3 Usability
- Responsive web interface that works on desktop and mobile
- Intuitive user interface with clear navigation
- Loading states and error handling for better UX
- Accessible design following WCAG guidelines

### 3.4 Reliability
- Proper error handling with user-friendly messages
- Graceful degradation when services are unavailable
- Data integrity maintained during operations

### 3.5 Compatibility
- Modern web browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for mobile and desktop
- Cross-platform compatibility

## 4. API Specification

### 4.1 Authentication Flow
- User logs in via frontend → Better Auth creates JWT token
- Frontend includes JWT in Authorization header for API calls
- Backend verifies JWT and extracts user information
- Backend filters data by authenticated user's ID

### 4.2 REST API Endpoints
```
GET    /api/{user_id}/tasks          # List all tasks for user
POST   /api/{user_id}/tasks          # Create a new task
GET    /api/{user_id}/tasks/{id}     # Get specific task
PUT    /api/{user_id}/tasks/{id}     # Update a task
DELETE /api/{user_id}/tasks/{id}     # Delete a task
PATCH  /api/{user_id}/tasks/{id}/complete  # Toggle completion status
```

### 4.3 Request/Response Examples
GET /api/user123/tasks?status=pending
Response: [{"id": 1, "title": "Buy groceries", "completed": false, ...}]

POST /api/user123/tasks
Request: {"title": "Buy groceries", "description": "Milk, eggs, bread"}
Response: {"id": 1, "title": "Buy groceries", "completed": false, ...}

## 5. Database Schema

### 5.1 Tables
**users** (managed by Better Auth):
- id: string (primary key)
- email: string (unique)
- name: string
- created_at: timestamp

**tasks**:
- id: integer (primary key)
- user_id: string (foreign key -> users.id)
- title: string (not null, 1-200 chars)
- description: text (nullable, max 1000 chars)
- completed: boolean (default false)
- created_at: timestamp
- updated_at: timestamp

### 5.2 Indexes
- tasks.user_id (for filtering by user)
- tasks.completed (for status filtering)

## 6. Frontend Requirements

### 6.1 Pages
- Landing page with sign up/sign in options
- Dashboard showing user's tasks
- Task creation form
- Individual task view/edit page

### 6.2 Components
- Task list component with filtering/sorting
- Task item component with completion toggle
- Form components for task creation/editing
- Authentication components (login, register)

## 7. Success Criteria

- All CRUD operations work correctly with persistent storage
- User authentication and authorization work properly
- API endpoints follow REST principles and handle JWT authentication
- Responsive web interface works across different devices
- Database schema supports efficient queries and data integrity
- Proper error handling and user feedback
- Application is deployable to Vercel