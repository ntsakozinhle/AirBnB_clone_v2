#!/usr/bin/python3
from os import getenv
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(getenv('HBNB_MYSQL_USER'),
                                            getenv('HBNB_MYSQL_PWD'),
                                            getenv('HBNB_MYSQL_HOST'),
                                            getenv('HBNB_MYSQL_DB')),
                                    pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects, optionally filtered by class
        """
        session = self.__session

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            return session.query(cls).all()
        else:
            objects = {}
            for c in [State, City]:
                table = Table(c.__tablename__, Base.metadata, autoload=True, autoload_with=self.__engine)
                for obj in session.query(table).all():
                    key = "{}.{}".format(c.__tablename__, obj.id)
                    objects[key] = obj
            return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads objects from database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        self.__session.close()
                                            
