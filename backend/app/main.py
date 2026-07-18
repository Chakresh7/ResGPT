from fastapi import FastAPI
from sqlalchemy import text

from app.api import auth, projects
from app.core.config import settings
from app.db.redis import redis_client
from app.db.session import engine

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router)
app.include_router(projects.router)


@app.get("/health")
def health():
    db_status = "ok"
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        db_status = "error"

    redis_status = "ok"
    try:
        redis_client.ping()
    except Exception:
        redis_status = "error"

    overall = "ok" if db_status == "ok" and redis_status == "ok" else "error"
    return {"status": overall, "database": db_status, "redis": redis_status}
