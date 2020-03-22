from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres@localhost/postgres', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return f"User id={self.id} name={self.name} lastname={self.lastname}"

Base.metadata.create_all(engine)

all_users = session.query(User).filter_by(lastname='Smith').all()
print(all_users)

first_user = session.query(User).filter_by(id=1).all()
print(first_user)
