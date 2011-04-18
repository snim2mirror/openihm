from PyQt4.QtGui import *
from PyQt4.QtCore import *

# import interface design
from gui.designs.ui_databasemessage import Ui_DatabaseMessage

class FrmDatabaseMessage(QDialog, Ui_DatabaseMessage):
     def __init__(self, message,  parent = None):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)

         self.parent = parent
         self.setupUi(self)
         self.lblMessage.setText( message )
         self.setWindowIcon( QIcon('resources/images/openihm.png') )

     def reject(self):
          self.parent.closeActiveSubWindow()
