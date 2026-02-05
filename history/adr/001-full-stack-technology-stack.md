# ADR-001: Full-Stack Technology Stack

## Status
Proposed

## Date
2026-02-04

## Context
We need to select a technology stack for the full-stack todo web application that will serve as the foundation for development. The application requires a frontend for user interaction, a backend for business logic and data management, and proper authentication mechanisms.

## Decision
We will use the following technology stack:
- **Frontend**: Next.js 16 with App Router, TypeScript, Tailwind CSS
- **Backend**: FastAPI with Python 3.12+, SQLModel ORM
- **Database**: SQLite for development and prototyping
- **Authentication**: Better Auth for user management and JWT tokens
- **API Communication**: REST API with JSON

This represents an integrated full-stack solution that provides:
- Modern React-based frontend with server-side rendering capabilities
- High-performance Python backend with automatic API documentation
- Lightweight database suitable for development and small-scale production
- Integrated authentication solution with JWT support

## Alternatives Considered
- **MERN Stack** (MongoDB, Express, React, Node.js): More familiar to many developers but lacks type safety and Python ecosystem benefits
- **Remix + Supabase**: Alternative modern stack but with different hosting considerations
- **Traditional Django + React**: More established but potentially heavier than needed
- **Node.js backend with Express/Fastify**: Would maintain JavaScript/TypeScript consistency but miss Python benefits

## Consequences
**Positive:**
- FastAPI provides automatic API documentation and excellent performance
- Next.js offers excellent developer experience with hybrid rendering options
- Type safety across both frontend and backend through TypeScript
- SQLite allows for easy setup and development without complex database infrastructure
- Better Auth provides secure, well-maintained authentication solution

**Negative:**
- Requires managing two different runtime environments (Python + Node.js)
- Learning curve for team members unfamiliar with either technology
- SQLite may not scale well for larger datasets or concurrent users
- Potential complexity in deployment compared to single-language stacks

## References
- plan.md: Sections 1-3 describe the full-stack architecture
- specs/overview.md: Technology stack overview