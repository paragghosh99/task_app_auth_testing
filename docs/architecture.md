# Architecture Decision Record (ADR) — V2 Refactor

## 1. Current State

The current application is a FastAPI-based task management API using SQLAlchemy ORM and SQLite as the database for both development and production. Authentication is handled via JWT, and core features include task creation and listing.

SQLite in production is a limitation due to lack of concurrency support and unreliable persistence in containerized deployments. The system also lacks structured migrations, multi-tenant isolation, and background job processing.

---

## 2. Why PostgreSQL?

PostgreSQL provides strong concurrency support, reliability, and scalability compared to SQLite. It supports connection pooling and advanced query analysis via EXPLAIN ANALYZE, which is essential for performance tuning.

Moving to PostgreSQL aligns the system with production-grade database standards and enables future scaling.

---

## 3. Why Alembic?

Alembic enables version-controlled database schema migrations with both upgrade and rollback capabilities. This ensures safe and traceable schema evolution.

Unlike raw SQL scripts, Alembic integrates directly with SQLAlchemy models, reducing drift between code and database schema.

This enables safe rollback during failed deployments.

---

## 4. Why Multi-tenant RBAC?

The system will evolve into a multi-tenant architecture using workspaces. Each workspace will isolate its own users and tasks.

Role-Based Access Control (RBAC) ensures proper authorization (owner, member, guest) and prevents cross-tenant data access, improving security and scalability.

Isolation is enforced at the ORM query layer to prevent accidental cross-tenant data leaks.

---

## 5. Why Cursor-based Pagination?

Offset-based pagination breaks under concurrent inserts, leading to duplicate or skipped records.

Cursor-based pagination provides stable and consistent traversal using a cursor derived from (created_at, id), making it suitable for real-time systems.

---

## 6. Why Redis Task Queue?

The current system uses synchronous or simulated operations for tasks like email notifications.

Introducing a Redis-backed async task queue enables background processing, retries, and better system responsiveness. This decouples heavy operations from request-response cycles and ensures reliability through retries and failure handling.