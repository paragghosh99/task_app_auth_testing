# 🚀 FastAPI Task API

A real-world backend API built with **FastAPI**, focused on *shipping software*, not just writing CRUD.

> From local code → Docker image → CI → live deployment

---

## 🧠 What This Is

- 🧩 RESTful Task Management API  
- 🔐 JWT-based authentication  
- 📦 Dockerized for reproducible builds  
- ☁️ Deployed on Render  
- ✅ CI-validated on every push  

---

## 🎯 Why This Project Exists

Writing backend code is easy.  
Running the **same code reliably in production** is the real skill.

This project focuses on:

- ❌ Eliminating “works on my machine” issues  
- 🐳 Understanding Docker images vs containers  
- 🔁 Seeing how CI validates deployability  
- 🌍 Experiencing real cloud constraints  

---

## 🛠 Tech Stack

| Layer | Tool |
|-----|------|
| Backend | FastAPI |
| Auth | JWT |
| ORM | SQLAlchemy |
| Database | SQLite |
| Container | Docker |
| CI | GitHub Actions |
| Deployment | Render |
| Testing | Pytest |

---

## 🌐 Live Deployment

- **Base URL:** `https://task-app-nstq.onrender.com/`
- **Docs:** `/docs` (Swagger UI)

---

## 🔐 Authentication Flow (Plain English)

**Login**
- Client sends credentials  
- Server verifies them  
- JWT is issued  

**Token Contains**
- `sub` → user id  
- `exp` → expiration  

**Authenticated Request**
Authorization: Bearer <token>
Server verifies → extracts user → request proceeds.

▶️ Run Locally (Without Docker)
pip install -r requirements.txt
uvicorn app.main:app --reload
🐳 Run Using Docker (Recommended)
docker build -t task_api .
docker run -p 8000:8000 task_api
Same image. Same behavior. No surprises.

🔁 CI Behavior
Every push triggers GitHub Actions

Docker image is built from scratch

Broken builds never deploy

🗃 Persistence Notes
⚠ SQLite lives inside the container
Redeploy = new container = fresh database

This is intentional.

🧪 Testing Strategy
Integration tests for:

Auth flow

CRUD behavior

Unit tests deferred until pure logic emerges

🧾 What This Project Signals
✔ Backend fundamentals
✔ Docker fluency
✔ CI/CD awareness
✔ Real deployment experience

✅ Status
✔ Live
✔ CI-passing
✔ Documented
✔ Recruiter-readable