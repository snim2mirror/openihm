from PyQt4 import QtGui, QtCore,  uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import controller
#from controller.controller import Controller

(Ui_ImportFromAccessDB, QDialog) = uic.loadUiType('./gui/designs/importfromaccessdb.ui')

class FrmImportFromAccessDB (QDialog, Ui_ImportFromAccessDB):
     """FrmImportFromAccessDB inherits QDialog"""

     def __init__ (self, parent = None):
         QDialog.__init__(self, parent)

         self.setupUi(self)
         
         self.cmdGetDB.setIcon(QIcon('resources/images/getdb.png'))
         self.cmdGetDB.setIconSize(QSize(32, 32))

     def __del__ (self):
         self.ui = None
         
     def closeForm(self):
         self.close()
         
     def getDB(self):
         self.filename = QFileDialog.getOpenFileName(self, 'Open file','/home', 'Access Database (*.mdb)')
         self.txtFilename.setText( self.filename )
         self.loadProjects()
         
     def loadProjects(self):
         pass
         
     def importAll(self):
         pass 
         
     def importSelected(self):
         pass 
