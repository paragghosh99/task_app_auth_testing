---
layout: default
title: FastAPI Task API — A Journey From Code to Cloud
---

# FastAPI Task API — A Journey From Code to Cloud

This page walks you through  
**what it is**, **why it matters**, and **how it actually works** — end to end.

---

## What Problem Are We Solving?

Most tutorials stop at “here’s CRUD.”

Real software must also:

1. Authenticate users  
2. Run consistently across machines  
3. Build reproducible containers  
4. Pass CI checks  
5. Deploy to the cloud  

That’s what this project focuses on.

---

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)
2. [Authentication Flow](#authentication-flow)
3. [APIs You Can Call](#apis-you-can-call)
4. [Building & Running Locally](#building--running-locally)
5. [Docker: One Image, Many Environments](#docker-one-image-many-environments)
6. [CI & Deployment](#ci--deployment)
7. [Testing Strategy](#testing-strategy)
8. [Lessons Learned & Next Steps](#lessons-learned--next-steps)

---

## High-Level Architecture

At its core, the FastAPI Task API has three pillars:

- **HTTP API** — FastAPI handles routing and validation  
- **Security** — JWT protects user-specific data  
- **Infrastructure** — Docker, CI, and cloud deployment  

**Request lifecycle:**

Client → Auth guard → Business logic → Database → JSON response

---

## Authentication Flow

Authentication is handled using **JWT (JSON Web Tokens)**.

### Login

- Client sends credentials  
- Server validates them  
- A JWT is issued  

### Token Contains

- `sub` — User ID  
- `exp` — Expiration timestamp  

### Authenticated Requests

**Authorization header:**

`Authorization: Bearer <token>`

Token is verified → user identity extracted → request proceeds.

---

## APIs You Can Call

### Public

- `POST /register` — Create a new user  
- `POST /login` — Authenticate and receive JWT  

### Protected (JWT required)

- `GET /tasks`  
- `POST /tasks`  
- `PUT /tasks/{id}`  
- `DELETE /tasks/{id}`  

---

## Building & Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Visit:

API Docs → `http://localhost:8000/docs`

## Docker: One Image, Many Environments
Docker guarantees the same behavior everywhere.

Build the image:

```bash
docker build -t task_api .
```

Run the container:

```bash
docker run -p 8000:8000 task_api
```

Same image locally.
Same image in production.
No “works on my machine” excuses.

## CI & Deployment
Every push triggers GitHub Actions:

- Builds the Docker image from scratch
- Runs tests
- Blocks deployment on failure
- Only validated builds reach production


## Testing Strategy

Testing focuses on high-value coverage:

- Integration tests for:
  - Authentication flow
  - Task CRUD behavior
- Unit tests will be added as pure business logic grows
- All tests are executed using Pytest


## Lessons Learned & Next Steps
### What This Project Teaches

- Docker builds must be deterministic
- JWT must be validated on every request
- SQLite inside containers is ephemeral by nature


### Next Improvements

- Replace SQLite with PostgreSQL
- Add migrations
- Introduce role-based access control (RBAC)


## Try It Live

- **Base URL:** https://task-app-nstq.onrender.com/
- **Interactive Docs:** https://task-app-nstq.onrender.com/docs

---

_Made with ❤️ by Parag · Hosted on GitHub Pages_
