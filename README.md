## Login 
---
### To run the app
-- `uvicorn main:app --reload`

---

### .env.py
-- contains `GS_DATABASE_URL`

---

### Alembic
-- Create a new migration: `alembic revision --autogenerate -m "<message>"`

-- Run migrations: `alembic upgrade head`

-- Check out the documentation: https://alembic.sqlalchemy.org/en/latest/tutorial.html