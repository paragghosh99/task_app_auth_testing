---
layout: default
title: FastAPI Task API — Story & Guide
---

<style>
body { font-family: Arial, sans-serif; line-height:1.6; }
h1, h2, h3 { border-bottom: 2px solid #ddd; padding-bottom: 0.2em; }
code { background: #f7f7f7; padding: 0.2em 0.4em; border-radius: 4px; }
pre { background: #f7f7f7; padding: 0.8em; border-radius: 6px; overflow-x: auto;}
</style>

# FastAPI Task API — A Journey From Code to Cloud

This page walks you through:  
**what it is**, **why it matters**, and **how it really works** — just like a proper software story should.

---

## What Problem Are We Solving?

Most tutorials stop at “here’s CRUD.”  
But real software must:

1. Authenticate users
2. Run consistently across machines
3. Build reproducible containers
4. Pass CI checks
5. Deploy to the cloud

That’s what this project does.

---

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)  
2. [Authentication Flow](#authentication-flow)  
3. [APIs You Can Call](#apis-you-can-call)  
4. [Building & Running Locally](#building--running-locally)  
5. [Docker: One Image, Many Environments](#docker-one-image-many-environments)  
6. [CI & Deployment with GitHub Actions + Render](#ci--deployment-with-github-actions--render)  
7. [Testing Strategy](#testing-strategy)  
8. [Lessons Learned & Next Steps](#lessons-learned--next-steps)

---

## High-Level Architecture

At its core, the FastAPI Task API has **three pillars**:

1. **HTTP API** — written with FastAPI  
2. **Security** — JWT for protected endpoints  
3. **Infrastructure** — Docker, CI, Deployment

<div style="text-align: center;">
<img src="assets/architecture.png" alt="Architecture diagram" width="600px">
</div>

Requests come in → Auth guard checks user → Task logic runs → DB responds → JSON out.

---

## Authentication Flow

The API uses **JWT (JSON Web Tokens)** to prove identity.

```text
Client        Server
  |   Login   |
  | --------> |
  |   200 OK  |
  | <======== |  JWT
  |           |
Auth required endpoint
  | Bearer JWT |
  | ----------> |
  | 200 OK     |
  | <----------|
Token contains:

sub — The user’s ID

exp — Expiration

APIs You Can Call
Public
POST /register  → Create a user
POST /login     → Get a JWT
Protected
GET /tasks
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}
Pass the JWT as:

Authorization: Bearer <token>
Building & Running Locally
Install dependencies:

pip install -r requirements.txt
Start the server:

uvicorn app.main:app --reload
Visit:

API docs → http://localhost:8000/docs

Docker: One Image, Many Environments
Docker ensures your code works everywhere.

Build the image:

docker build -t task_api .
Run it:

docker run -p 8000:8000 task_api
Notice: same image locally and in production.

CI & Deployment with GitHub Actions + Render
Every push:

Builds a fresh Docker image

Runs tests

Blocks deployment on failure

This gives confidence before release.

Testing Strategy
We favor high-value tests:

Integration tests for:

Auth flow

CRUD behavior

Unit tests will come as logic grows

Pytest drives all checks.

Lessons Learned & Next Steps
This project teaches:

Docker builds must be deterministic

JWT must be validated on every request

SQLite inside Docker is ephemeral — intentional for learning

Next steps:

Replace SQLite with PostgreSQL

Add real migrations

Add RBAC

Try It Live
Base URL: https://task-app-nstq.onrender.com/

Interactive docs: /docs

<footer style="text-align:center; margin-top:30px;"> Made with ❤️ by Parag Hosted on GitHub Pages </footer> ```