from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def coonect_to_db():
    engine = create_engine('postgresql://postgres:roman2002@localhost/diploma_beholder')
    Session = sessionmaker(bind=engine)
    session = Session()

    return session
