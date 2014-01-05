from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.db_errors import ErrorMessage


class QErrorMessage(ErrorMessage):

    def __init__(self, parent, custom_duplicate_message=None):

        self.parent = parent
        self.duplicate_message = custom_duplicate_message or 'Entry already exists'

    def duplicate_entry(self, message):
        """
        This will be called when there is a database error indiicating that
        the item already exists in the database.  This can be via an insert
        or an update.
        """
        QMessageBox.information(self.parent, self.parent.windowTitle(), 
                                self.duplicate_message)
