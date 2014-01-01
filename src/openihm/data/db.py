from config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager


class Alchemy(object):

    @classmethod
    def setupDB(cls):
        cls.connection_string = Config.config.sqlalchemy_superuser_connection_string()
        engine = create_engine(cls.connection_string, echo=True) # FIXME: turn off echo
        cls._session = sessionmaker(bind=engine)

    @classmethod
    def getSession(cls): 
        """
        Get an SQL Alchemy session object.
        """
        # FIXME: this is pretty ugly, really ought to put more thought into this.
        if not hasattr(cls, '_session'):
            cls.setupDB()
        return cls._session()
    
@contextmanager
def session_scope():
    """
    Automatically manages the commit/rollbacks for an SQL alchemy transaction 

        with session_scope() as session:
            session.query()....
        
    If an exception is thrown you will need to catch the exception, but the 
    transaction will have been automatically rolled back.
    """
    session = Alchemy.getSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

