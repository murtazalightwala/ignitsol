from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from config import DB_URI
from sqlalchemy.orm import sessionmaker


engine = create_engine(DB_URI)


def validate_database(engine):
     if not database_exists(engine.url): # Checks for the first time  
         create_database(engine.url)     # Create new DB    
         print("New Database Created" + database_exists(engine.url)) # Verifies if database is there or not.
     else:
         print("Database Already Exists")

Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db():
    db = Session()

    try:
        yield db
    finally:
        db.close()
