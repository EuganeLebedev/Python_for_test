from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres@localhost/postgres', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class User(Base):
    __tablename__ = 'users'

    name = Column(String, primary_key=True)
    lastname = Column(String)

Base.metadata.create_all(engine)

user1 = User(name="Ivan", lastname="Petrov")
session.add(user1)

session.commit()

