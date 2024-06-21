from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError
import os
import time
import subprocess



load_dotenv()
# Check if POSTGRES_URL environment variable is set
postgres_url = os.getenv('POSTGRES_URL')
if postgres_url is None:
    raise ValueError("POSTGRES_URL environment variable is not set")

presto_mongo_url = os.getenv('PRESTO_MONGO')
if presto_mongo_url is None:
    raise ValueError("PRESTO_MONGO environment variable is not set")

# Postgres Engine
engine = create_engine(postgres_url,
                       pool_size=20, max_overflow=0,
                       echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

engine_presto = create_engine(
    presto_mongo_url,
    pool_size=20,
    max_overflow=0,
    echo=False  # Adjust as needed
)

def restart_mongo_container():
    container_id = '747225c6a12ec73d03e8f828ccbbd835f88ab9a430ae8d8281e8db2f02d256da'

    # Check if MongoDB container is running
    try:
        result = subprocess.run(['docker', 'inspect', '--format={{.State.Running}}', container_id], check=True,
                                capture_output=True, text=True)
        if result.stdout.strip() == "true":
            print("MongoDB container is running.")
        else:
            raise subprocess.CalledProcessError(1, 'docker inspect')  # Simulate non-zero return code if not running
    except subprocess.CalledProcessError:
        print("MongoDB container is not running. Waiting 20 seconds before restarting...")
        time.sleep(20)
        print("Restarting MongoDB container...")
        subprocess.run(['docker', 'restart', container_id], check=True)

# Call the function to restart MongoDB container if needed
restart_mongo_container()
def restart_presto_container():
    container_id = 'f9e0ab4b36443a75941e93a173fced4262228a1df532ba386c0a8cb250a35369'

    # Check if Presto container is running
    try:
        result = subprocess.run(['docker', 'inspect', '--format={{.State.Running}}', container_id], check=True,
                                capture_output=True, text=True)
        if result.stdout.strip() == "true":
            print("Presto container is running.")
        else:
            raise subprocess.CalledProcessError(1, 'docker inspect')  # Simulate non-zero return code if not running
    except subprocess.CalledProcessError:
        print("Presto container is not running. Waiting 20 seconds before restarting...")
        time.sleep(20)
        print("Restarting Presto container...")
        subprocess.run(['docker', 'restart', container_id], check=True)

# Call the function to restart Presto container if needed
restart_presto_container()


PrestoSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_presto)
PrestoBase = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_presto_db():
    retries = 3
    delay = 1
    for _ in range(retries):
        db = PrestoSessionLocal()
        try:
            yield db
        except SQLAlchemyError as e:
            print(f"Error connecting to Presto database: {e}")
            time.sleep(delay)
            delay *= 2
        finally:
            db.close()

    raise ValueError("Failed to connect to Presto database after retries")



# Check if PRESTO_MONGO environment variable is set
mongo_url = os.getenv('PRESTO_MONGO')
if mongo_url is None:
    raise ValueError("PRESTO_MONGO environment variable is not set")
# Presto Engine
enginePresto = create_engine(mongo_url,
                             pool_size=20, max_overflow=0,
                             echo=False)

PrestoSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=enginePresto)
PrestoBase = declarative_base()

# TODO - use get_presto_db instead of prestoDb
prestoDb = SQLDatabase(engine=enginePresto)


def get_presto_db():
    db = PrestoSessionLocal()
    try:
        yield db
    finally:
        db.close()


