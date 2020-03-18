from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
        'postgresql+psycopg2://e_lebedev:1248@localhost/e_lebedev',
        echo=True
        )

    name = Column(String, primary_key=True)
Base = declarative_base()

class User(Base):
    """
    Класс для работы с БД postgreess
    """
    __tablename__ = 'users'

    name = Column(String, primary_key=True)
    lastname = Column(String)

#Создать все таблицы
Base.metadata.create_all(engine)


