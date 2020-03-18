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
        return f'Users id={user.id} name={user.name} lastname={user.lastname}'

#Создать все таблицы
Base.metadata.create_all(engine)

#Создание щаписей в таблице
#Сам класс - таблица
#Объектт класса - запись в таблице
user1 = User(name='Ivan', lastname='Petrov')
#Добавляем в сессию объект
#Пока не в базе. 
#При открытии начинается транзакция. Пока не комитится
session.add(user1)
#Добавлене ихменения
session.commit()
#Грязный объект.
#Пока не добавлен в сессию, но изменен уде созраненный
session.dirty


all_users = session.query(User).filter_by(lastname='Petrov').all()
print(all_users)
