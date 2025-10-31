from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔗 URL Database dari Railway
DATABASE_URL = "postgresql://postgres:lDydWOXAFJiGytjhZprEomwzWwhhKUVD@centerbeam.proxy.rlwy.net:17783/railway"

# Engine koneksi
engine = create_engine(DATABASE_URL, echo=False)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk model
Base = declarative_base()
