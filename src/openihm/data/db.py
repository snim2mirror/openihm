from config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
import logging

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


class ErrorHandler(object):
    """
    Provides error messages to the user when a problem occurs.
    Designed to be usable with the UI as necessary.  Provide it
    an error message object to call.

    This will suppress the exceptions it displays an error for.
    The rest it will log then re-raise for you to catch.

    If you need to determine whether the code finished okay
    check the success property of the object.  It will be set
    to True if your code completes.

        eh = ErrorHandler(QErrorMessage(self))
        with eh.error_wrapper():
            with session_scope() as session:
                ...
        if eh.success:
            self.close() # only close the window if succeeded

    """

    def __init__(self, error_handler):
        self.success = False
        self.error_handler = error_handler

    @contextmanager
    def error_wrapper(self):
        try:
            yield
            self.success = True
        except IntegrityError, e:
            if e.message.find('Duplicate entry') != -1:
                self.error_handler.duplicate_entry(e.message)
            else:
                log = logging.getLogger('sqlalchemy.engine')
                log.warning("Database error - %s", type(e), exc_info=1)
                raise
            # FIXME: still very much in debug mode, need to determine
            # what errors we are likely to see.
        except Exception, e:
            log = logging.getLogger('sqlalchemy.engine')
            log.warning("Database error - %s", type(e), exc_info=1)
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
