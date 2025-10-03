from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Switch between SQLite and PostgreSQL
DATABASE_URL = "sqlite:///practice.db"  
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/practice_db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True = shows SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
