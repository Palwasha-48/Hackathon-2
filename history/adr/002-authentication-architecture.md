# ADR-002: Authentication Architecture

## Status
Proposed

## Date
2026-02-04

## Context
The application requires secure user authentication and authorization to ensure proper user isolation and protect sensitive data. We need to decide on the authentication approach that balances security, developer experience, and maintenance overhead.

## Decision
We will implement authentication using Better Auth with JWT tokens for the following integrated solution:
- **Frontend Authentication**: Better Auth client library integrated with Next.js App Router
- **Token Management**: JWT tokens stored in httpOnly cookies for security
- **Backend Verification**: JWT middleware in FastAPI for protecting API endpoints
- **Shared Secret**: Common BETTER_AUTH_SECRET between frontend and backend
- **User Management**: Email/password authentication with proper validation

This creates a seamless authentication experience while maintaining security best practices.

## Alternatives Considered
- **Custom JWT Implementation**: Building our own authentication system would require more development time and security expertise
- **Auth0/Clerk**: Third-party providers offer robust solutions but add vendor lock-in and recurring costs
- **Next-Auth.js**: Popular for Next.js applications but doesn't integrate as seamlessly with our FastAPI backend
- **Session-based Authentication**: Traditional approach but requires server-side session storage

## Consequences
**Positive:**
- Better Auth provides secure, well-tested authentication with good security practices
- JWT tokens eliminate need for server-side session storage
- Seamless integration with Next.js App Router
- Proper security with httpOnly cookies prevents XSS attacks
- Consistent authentication flow across frontend and backend

**Negative:**
- Adds dependency on third-party library
- Requires careful secret management across frontend and backend
- JWT tokens cannot be invalidated server-side (until expiration)
- Learning curve for team members unfamiliar with Better Auth

## References
- plan.md: Section 2 describes authentication implementation
- specs/features/authentication.md: Authentication feature specification