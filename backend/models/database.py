from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chatbox.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    file_type = Column(String)  # e.g., "CDR", "REVENUE", "TRANSACTION"
    upload_date = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String)
    metadata = Column(String)  # JSON string for additional metadata

class CDRRecord(Base):
    __tablename__ = "cdr_records"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    timestamp = Column(DateTime)
    caller_number = Column(String)
    receiver_number = Column(String)
    duration = Column(Float)
    call_type = Column(String)
    region = Column(String)

class RevenueRecord(Base):
    __tablename__ = "revenue_records"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    timestamp = Column(DateTime)
    region = Column(String)
    service_type = Column(String)
    amount = Column(Float)
    currency = Column(String)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create all tables
Base.metadata.create_all(bind=engine) 