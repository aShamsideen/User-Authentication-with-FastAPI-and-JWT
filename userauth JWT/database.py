from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_DATABASE_URL = 'mysql+pymysql://root:adeSUNbo+231#@localhost:3306/myapplication'

engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommmit=False, autoflush=False, bind=engine)

Base = declarative_base() 