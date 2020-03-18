from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#разовое подклчение
engine = create_engine(
        'postgresql+psycopg2://e_lebedev:1248@localhost/e_lebedev',
        echo=True
        )
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class User(Base):
    """
    Класс для работы с БД postgreess
    """
    __tablename__ = 'users'
    #Автоинкримент для разных баз создается по разному
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)

    def __str__(self):
        return f'Users id={self.id} name={self.name} lastname={self.lastname}'
    def __repr__(self):
        return f'Users id={self.id} name={self.name} lastname={self.lastname}'

#Создать все таблицы
Base.metadata.create_all(engine)

user1 = session.query(User).filter_by(id=1).first()
user1.lastname = 'Sidorov'

print(session.dirty)

session.rollback()
#session.commit()
