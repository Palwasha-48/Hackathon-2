# ADR-003: Database and Data Architecture

## Status
Proposed

## Date
2026-02-04

## Context
We need to select a database solution and define the data architecture for the todo application. The database must support user authentication, task management, and proper data relationships while being suitable for the development stage and potential production deployment.

## Decision
We will use SQLite with SQLModel ORM for our data architecture:
- **Database Engine**: SQLite file-based database for development
- **ORM**: SQLModel as the Object-Relational Mapping layer
- **Schema Design**: Two main tables (users and tasks) with proper relationships
- **Data Types**: UUID primary keys, proper field constraints and validation
- **Indexing Strategy**: Strategic indexes on foreign keys and frequently queried fields

This provides a lightweight, file-based solution that's ideal for development while using a modern, typed ORM.

## Alternatives Considered
- **PostgreSQL**: Production-ready database with advanced features but more complex setup
- **MySQL**: Popular relational database but lacks some modern features of PostgreSQL
- **MongoDB**: Document-based approach but would complicate user-task relationships
- **Supabase**: Hosted Postgres solution with additional features but adds external dependency
- **Prisma ORM**: Alternative to SQLModel but would require different migration approach

## Consequences
**Positive:**
- SQLite requires zero setup, perfect for development
- SQLModel provides excellent type safety and integrates well with FastAPI
- Proper UUID primary keys ensure global uniqueness
- Foreign key relationships enforce data integrity
- Strategic indexing improves query performance
- SQLModel supports both SQLAlchemy and Pydantic features

**Negative:**
- SQLite doesn't scale well for production with many concurrent users
- May require migration to different database for production deployment
- Limited concurrency compared to server-based databases
- File-based storage may not work well in containerized environments

## References
- plan.md: Section 1.1 describes database models
- specs/database/schema.md: Database schema specification