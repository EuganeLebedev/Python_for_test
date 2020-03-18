from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
        'postgresql+psycopg2://e_lebedev:1248@localhost/e_lebedev',
        echo=True
        )

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

#Создание щаписей в таблице
#Сам класс - таблица
#Объектт класса - запись в таблице
user1 = User(name='Ivan', lastname='Petrov')
user1.name='John'
print(user1.name)
print(user1.lastname)
