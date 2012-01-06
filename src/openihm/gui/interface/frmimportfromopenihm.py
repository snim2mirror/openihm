#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""


from PyQt4 import QtGui, QtCore,  uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyodbc

# import controller
from control.controller import Controller

Ui_ImportFromOpenIHM, QDialog = uic.loadUiType('./gui/designs/importfromopenihm.ui')

from mixins import TableViewMixin

class FrmImportFromOpenIHM (QDialog, TableViewMixin, Ui_ImportFromOpenIHM):
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
         self.filename = QFileDialog.getOpenFileName(self, 'Open file','/home', 'IHM file (*.ihm)')
         if self.filename:
             self.txtFilename.setText( self.filename )
             self.showProject()
         
     def showProject(self):
         controller = Controller()
         projectdata = controller.getProjectFromFile( str(self.txtFilename.text()) )
         
         self.lblProjectName.setText( projectdata["projectname"] )
         self.lblStartDate.setText( projectdata["startdate"] )
         self.lblCurrency.setText( projectdata["currency"] )
         
     def importProject(self):
         ''' Import all projects '''
         msg = "Are you sure you want to to import this project?"    
         ret = QMessageBox.question(self,"Confirm Import", msg, QMessageBox.Yes|QMessageBox.No)
         # if import is rejected return without deleting
         if ret == QMessageBox.No:
             return
         
         # import project    
         controller = Controller()
         controller.importIhmProject( str(self.txtFilename.text()) )  
       
         # import message
         QMessageBox.information(self,"Importing Data from OpenIHM file","Project data has been imported.") 
             
         self.close()  
