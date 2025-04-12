from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.core.database import engine

router = APIRouter()

@router.get("/db-test")
def test_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"connected": True, "result": result.scalar()}
    except Exception as e:
        return {"connected": False, "error": str(e)}
