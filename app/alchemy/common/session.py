import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, current_app 


class AlchemySession():

    Base = declarative_base()

    # use session_factory() to get a new Session
    _SessionFactory = None

    def session_factory(self):
        with current_app.app_context():
            # within this block, current_app points to app.
            connectionString = current_app.config['SQLALCHEMY_DATABASE_URI']
            engine = create_engine(connectionString, connect_args={'check_same_thread': False})
            self.Base.metadata.create_all(engine)
            self._SessionFactory = sessionmaker(bind=engine)
        return self._SessionFactory()

