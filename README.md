# Quantum Core

Reusable FastAPI backend starter framework with authentication and user management built in.

## Overview

Quantum Core is a backend foundation designed to reduce repeated setup work across projects.

It provides:

* Authentication
* User management
* Database setup
* Migration workflow
* Centralized responses
* Exception handling
* Configuration management
* Modular architecture

The goal is:

Build authentication and user infrastructure once → reuse across projects.

---

## Features

### Authentication

* Register
* Login
* JWT access tokens
* Current user endpoint
* Logout
* Refresh token endpoint
* Forgot password
* Reset password
* Email verification

### User Management

* User model
* User profile endpoints
* Extendable user schema

### Infrastructure

* PostgreSQL
* SQLAlchemy
* Alembic migrations
* Environment configuration
* Logging
* Standard API responses

---

## Installation

Clone project:

```bash
git clone https://github.com/QuantumCodr/core-identity-api.git or BaseAPI.git
cd quantum-core
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Copy:

```bash
copy .env.example .env
```

Update values inside `.env`.

---

## Database Setup

Run migrations:

```bash
python -m alembic upgrade head
```

---

## Run Development Server

```bash
uvicorn quantum_core.main:app --reload
```

Open:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Authentication Routes

```plaintext
POST /auth/register
POST /auth/login
POST /auth/logout
POST /auth/refresh
POST /auth/forgot-password
POST /auth/reset-password
POST /auth/verify-email
GET  /auth/me
```

---

## Project Structure

```plaintext
quantum_core/

auth/
users/
database/
core/
utils/
tests/
```

---

## Extending Users

To add additional fields:

1. Update `users/models.py`
2. Update `users/schemas.py`
3. Generate migration

```bash
python -m alembic revision --autogenerate -m "add user fields"
```

4. Apply migration

```bash
python -m alembic upgrade head
```

Example additions:

```plaintext
name
phone
role
avatar
bio
```

Do not modify historical migrations.

---

## Testing

Run:

```bash
pytest
```

---

## Version

Current version:

```plaintext
v0.1.0-alpha
```

---

## Philosophy

Keep the framework simple.

Business rules belong in modules.

Framework code should stay reusable.

---

## License

See LICENSE file.
