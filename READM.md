# FastAPI Task API

A simple FastAPI CRUD application demonstrating database persistence using SQLAlchemy and SQLite.

## Tech Stack
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pytest

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

## AUTH FLOW NARRATIVE (PLAIN ENGLISH):

	# Login
	- User sends credentials (username/password).
	- Server verifies them.
	- If valid → server creates a JWT (JSON Web Token).
	- Token Creation
	- Token contains:
		sub / user_id (who you are)
		exp (when it dies)
	- Token is signed, not encrypted. Anyone can read it; only the server can vouch for it.

	# Client Storage
	- Client stores token (usually memory or secure storage).
	- No token = no identity.
	- Authenticated Request
	- Client sends: Authorization: Bearer <token>
	- Every protected request repeats this ritual. No exceptions.

	# Server Verification
	- Middleware:
		- Extracts token
		- Verifies signature
		- Checks expiration
		- Extracts user id
		- Attaches user to request context
		- Endpoint Logic
	- Endpoint assumes:
		“If I’m running, the user is already authenticated.”
		
## Testing Strategy

- Integration tests cover:
  - API authentication behavior
  - Database CRUD correctness

- Unit tests are intentionally deferred until
  reusable helpers or pure business logic
  are extracted from routes or dependencies.
