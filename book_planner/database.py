from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///books.db"  # SQLite database

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables

Session = sessionmaker(bind=engine)
session = Session()
