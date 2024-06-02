#!/usr/bin/python3
"""New storage engine module for SQLAlchemy mapping"""
from os import getenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Database abstraction class for SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize database

        Description:
        Creates a connection engine for the database
        """

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        con = f"mysql+pymysql://{user}:{passwd}@{host}/{db}"
        self.__engine = create_engine(con, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Fetch objects

        Description:
        Fetches all objects of a given class from the database storage.
        If cls is None, it fetches all objects of all classes

        Args:
        cls (class): the class type to fetch its objects

        Returns:
        A dictionary of all objects of the specified class or
        of all classes if cls is None
        """

        objs = {}  # initialize an empty dictionary

        if cls:
            if type(cls) is str:
                cls = eval(cls)

            query = self.__session.query(cls)
            for val in query:
                key = f"{type(val).__name__}.{val.id}"
                objs[key] = val
        else:
            mods = [State, City, Place, User, Amenity, Review]
            for mod in mods:
                query = self.__session.query(mod)

                for val in query:
                    key = f"{type(val).__name__}.{val.id}"
                    objs[key] = val

        return objs

    def new(self, obj):
        """Add object to session

        Description:
        Adds an object to the current database session

        Args:
        obj (object): the object to add to the database session
        """

        self.__session(obj)

    def save(self):
        """Commit changes

        Description:
        Commits all changes to the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """Delete object

        Description:
        Deletes an object (obj) from the database if not None
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configure session

        Description:
        Creates a database session and all database tables
        """

        Base.metadata.create_all(self.__engine)
        make_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(make_session)
        self.__session = Session()

    def close(self):
        """Close the session

        Description:
        This method calls the remove() method on the private session attribute
        """

        self.__session.remove()
