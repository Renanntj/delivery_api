from models import db
from sqlalchemy.orm import sessionmaker
def open_section():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session

    finally:
    
        session.close()