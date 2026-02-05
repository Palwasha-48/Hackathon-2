# ADR-004: API Architecture and Communication Pattern

## Status
Proposed

## Date
2026-02-04

## Context
We need to establish the API architecture and communication pattern between the frontend and backend. This includes defining the API style, endpoint structure, authentication mechanism, and error handling approach.

## Decision
We will implement a REST API with the following characteristics:
- **API Style**: RESTful API with resource-based endpoints
- **Authentication**: JWT tokens passed in Authorization header
- **Endpoint Design**: Standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- **Error Handling**: Consistent error response format with appropriate HTTP status codes
- **Data Format**: JSON for request and response bodies
- **CORS Configuration**: Restricted to frontend origin only

The API will follow standard REST conventions with endpoints for tasks including filtering, sorting, and CRUD operations.

## Alternatives Considered
- **GraphQL**: More flexible querying but adds complexity and learning curve
- **gRPC**: High-performance but not ideal for web frontend communication
- **WebSocket**: Real-time communication but unnecessary for basic todo operations
- **REST with HATEOAS**: More discoverable APIs but adds complexity
- **JSON:API**: Standardized format but restricts flexibility

## Consequences
**Positive:**
- REST is widely understood and well-documented
- JWT authentication provides stateless security
- Standard HTTP methods are intuitive for developers
- Consistent error handling simplifies frontend error management
- CORS protection enhances security
- Good tooling support for testing and documentation

**Negative:**
- REST can lead to over-fetching/under-fetching compared to GraphQL
- Multiple endpoints may be needed for complex operations
- Less efficient for complex nested data retrieval
- May require more round trips compared to GraphQL

## References
- plan.md: Section 1.3 describes API endpoints
- specs/api/rest-endpoints.md: REST API endpoint specification