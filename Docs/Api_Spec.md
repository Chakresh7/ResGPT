# API Specification

## Overview

This document lists the HTTP API endpoints for the Res-GPT service. All endpoints that require authentication use Bearer tokens (JWT) unless otherwise noted.

## Authentication

- POST /auth/register
	- Description: Create a new user account.
	- Body: `{ "name", "email", "password" }`
	- Response: `201 Created` with user metadata.

- POST /auth/login
	- Description: Authenticate and receive an access token.
	- Body: `{ "email", "password" }`
	- Response: `200 OK` with `{ "access_token": "...", "token_type": "bearer" }`.

- GET /auth/me
	- Description: Get current authenticated user profile.
	- Auth: Bearer token
	- Response: `200 OK` user object.

## Projects

- POST /projects
	- Description: Create a new project.
	- Auth: Bearer token
	- Body: `{ "title", "description" }`
	- Response: `201 Created` with project object.

- GET /projects
	- Description: List projects for the current user.
	- Auth: Bearer token
	- Query: optional pagination `?page=&limit=`.
	- Response: `200 OK` list of projects.

- GET /projects/{id}
	- Description: Get a single project by id.
	- Auth: Bearer token
	- Path param: `id` (UUID)
	- Response: `200 OK` project object.

- DELETE /projects/{id}
	- Description: Delete a project and related resources (careful with cascade behavior).
	- Auth: Bearer token
	- Response: `204 No Content`.

## Research

- POST /research/start
	- Description: Start a research run for a project.
	- Auth: Bearer token
	- Body: `{ "project_id", "query", "options" }`
	- Response: `202 Accepted` with `{ "research_id": "..." }`.

- GET /research/{id}
	- Description: Get results or report for a completed research run.
	- Auth: Bearer token
	- Response: `200 OK` with research metadata and links to report.

- GET /research/{id}/status
	- Description: Poll status of a research run (queued, running, done, failed).
	- Auth: Bearer token
	- Response: `200 OK` `{ "status": "running" }`.

## Sources

- GET /projects/{id}/sources
	- Description: List sources discovered or added for a project.
	- Auth: Bearer token
	- Response: `200 OK` list of sources.

## Reports

- GET /projects/{id}/report
	- Description: Retrieve the generated report (markdown or structured JSON).
	- Auth: Bearer token
	- Response: `200 OK` report content or metadata.

- GET /projects/{id}/report/pdf
	- Description: Download PDF export of report.
	- Auth: Bearer token
	- Response: `200 OK` with `application/pdf`.

- GET /projects/{id}/report/docx
	- Description: Download DOCX export of report.
	- Auth: Bearer token
	- Response: `200 OK` with `application/vnd.openxmlformats-officedocument.wordprocessingml.document`.

## Chat

- POST /chat
	- Description: Send a message to the research chat assistant (returns assistant reply or message id).
	- Auth: Bearer token
	- Body: `{ "project_id", "message" }`
	- Response: `200 OK` with message/response object.

- GET /chat/history/{project_id}
	- Description: Get chat history for a project.
	- Auth: Bearer token
	- Response: `200 OK` list of messages.

## Health

- GET /health
	- Description: Service health check (liveness/readiness).
	- Auth: none
	- Response: `200 OK` `{ "status": "ok" }`.

## Notes & Recommendations

- Use standard HTTP status codes. Implement pagination for list endpoints.
- Rate-limit research-start endpoints to prevent abuse.
- Return minimal metadata for long-running jobs and provide links to download artifacts.
