# Todo Web App - Phase II

This is the Phase II implementation of the Todo application - a full-stack web application with Next.js frontend, FastAPI backend, and Neon database.

## Overview

A modern, full-stack web application that allows users to manage their tasks through a responsive web interface. The application provides all essential todo management features with persistent storage and user authentication.

## Architecture

### Frontend
- **Framework**: Next.js 16+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.13+
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens with Better Auth integration

## Features

- User authentication and authorization
- Create, read, update, delete tasks
- Mark tasks as complete/incomplete
- Responsive web interface
- Task filtering and sorting
- Persistent data storage

## Project Structure

```
phase 2/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database connection and configuration
│   ├── auth.py              # JWT authentication middleware
│   ├── models/              # Database models
│   │   └── task.py          # Task model definition
│   ├── routes/              # API route handlers
│   │   └── tasks.py         # Task-related endpoints
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── app/                 # Next.js app router pages
    │   └── page.tsx         # Main application page
    ├── components/          # Reusable UI components
    ├── lib/                 # Utility functions and API client
    │   └── api.ts           # API client for backend communication
    ├── types/               # TypeScript type definitions
    │   └── task.ts          # Task-related type definitions
    ├── public/              # Static assets
    ├── package.json         # Node.js dependencies
    ├── next.config.js       # Next.js configuration
    ├── tsconfig.json        # TypeScript configuration
    └── tailwind.config.js   # Tailwind CSS configuration
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd phase 2/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/todo_db"
   export SECRET_KEY="your-super-secret-key"
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd phase 2/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set environment variables:
   ```bash
   # Create .env.local file
   NEXT_PUBLIC_API_URL=http://localhost:8000
   NEXT_PUBLIC_OPENAI_DOMAIN_KEY=your-domain-key
   ```

4. Run the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

The backend provides the following RESTful API endpoints:

- `GET /api/{user_id}/tasks` - List all tasks for user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion status

## Authentication

The application uses Better Auth for user authentication with JWT tokens. All API endpoints (except authentication) require a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

## Database Schema

### Tasks Table
- `id`: integer (primary key, auto-increment)
- `user_id`: string (foreign key to users table)
- `title`: string (1-200 characters, not null)
- `description`: text (nullable, max 1000 characters)
- `completed`: boolean (default false)
- `created_at`: timestamp with timezone
- `updated_at`: timestamp with timezone

## Deployment

### Frontend
Deploy to Vercel:
```bash
vercel --prod
```

### Backend
Deploy to any cloud provider that supports Python applications (AWS, GCP, Azure, etc.)

## Environment Variables

### Backend
- `DATABASE_URL`: PostgreSQL database connection string
- `SECRET_KEY`: Secret key for JWT token signing

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL
- `NEXT_PUBLIC_OPENAI_DOMAIN_KEY`: OpenAI domain key (for ChatKit)

## Testing

### Backend Tests
```bash
# Run backend tests
pytest
```

### Frontend Tests
```bash
# Run frontend tests
npm run test
```

## Security Considerations

- JWT tokens are used for authentication
- User data isolation - users can only access their own tasks
- Input validation and sanitization
- Proper error handling without exposing internal details

## Error Handling

The application provides comprehensive error handling:

- Backend: Proper HTTP status codes and error messages
- Frontend: User-friendly error messages and loading states
- Database: Transaction safety and integrity constraints

## Performance

- Efficient database queries with proper indexing
- Optimized API endpoints
- Responsive UI with loading states
- Caching strategies (to be implemented)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is open source and available under the MIT License.