from config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

from sqlalchemy.exc import IntegrityError

class Alchemy(object):

    @classmethod
    def setupDB(cls):
        cls.connection_string = Config.config.sqlalchemy_superuser_connection_string()
        engine = create_engine(cls.connection_string)
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
def error_wrapper(error_handler):
    """
    Provides error messages to the user when a problem occurs.
    Designed to be usable with the UI as necessary.  Provide it
    an error message object to call.

    This does not suppress any exception, it simply detects them
    and uses the error_handler object to tell the user about the
    problem.  Catching exceptions is programmers problem.  This
    should be used outside the session scope because it is likely that
    the UI will block; blocking while in the middle of a transaction
    would be a bad idea.

        with error_wrapper(QErrorMessage(self)):
            with session_scope() as session:
                ...
    """
    try:
        yield
    except IntegrityError, e:
        if e.message.find('Duplicate entry') != -1:
            error_handler.duplicate_entry(e.message)
        # FIXME: still very much in debug mode, need to determine
        # what errors we are likely to see.
        print "Database error"
        print type(e)
        print e
        raise
    except Exception, e:
        print "Database error"
        print type(e)
        print e
        raise


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
