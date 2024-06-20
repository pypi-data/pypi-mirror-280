from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os


load_dotenv()
# Check if POSTGRES_URL environment variable is set
postgres_url = os.getenv('POSTGRES_URL')
if postgres_url is None:
    raise ValueError("POSTGRES_URL environment variable is not set")
# Postgres Engine
engine = create_engine(postgres_url,
                       pool_size=20, max_overflow=0,
                       echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#
# # Check if PRESTO_MONGO environment variable is set
# mongo_url = os.getenv('PRESTO_MONGO')
# if mongo_url is None:
#     raise ValueError("PRESTO_MONGO environment variable is not set")
# # Presto Engine
# enginePresto = create_engine(mongo_url,
#                              pool_size=20, max_overflow=0,
#                              echo=False)
#
# PrestoSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=enginePresto)
# PrestoBase = declarative_base()
#
# # TODO - use get_presto_db instead of prestoDb
# prestoDb = SQLDatabase(engine=engine)
#
#
# def get_presto_db():
#     db = PrestoSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
