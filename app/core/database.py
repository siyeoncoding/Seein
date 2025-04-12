from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

#상속받아야지
Base = declarative_base()


load_dotenv()  # .env 파일 로드

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ 데이터베이스 연결 성공:", result.scalar())
    except SQLAlchemyError as e:
        print("❌ 데이터베이스 연결 실패:", str(e))