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

Ui_ImportFromAccessDB, QDialog = uic.loadUiType('./gui/designs/importfromaccessdb.ui')

from mixins import TableViewMixin

class FrmImportFromAccessDB (QDialog, TableViewMixin, Ui_ImportFromAccessDB):
     """FrmImportFromAccessDB inherits QDialog"""

     def __init__ (self, parent = None):
         QDialog.__init__(self, parent)

         self.setupUi(self)
         
         self.cmdGetDB.setIcon(QIcon('resources/images/getdb.png'))
         self.cmdGetDB.setIconSize(QSize(32, 32))
         
         self.initProjectList()

     def __del__ (self):
         self.ui = None
         
     def closeForm(self):
         self.close()
              
     def initProjectList(self):
         model = QStandardItemModel(1,1)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Project ID'))
         model.setHorizontalHeaderItem(1,QStandardItem('Project Name'))
         model.setHorizontalHeaderItem(2,QStandardItem('Date of Data Collection'))
         
         self.tblProjects.setModel(model)
         
     def getDB(self):
         self.filename = QFileDialog.getOpenFileName(self, 'Open file','/home', 'Access Database (*.mdb)')
         self.txtFilename.setText( self.filename )
         self.loadProjects()
         
     def loadProjects(self):
         
         model = QStandardItemModel(1,1)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Project ID'))
         model.setHorizontalHeaderItem(1,QStandardItem('Project Name'))
         model.setHorizontalHeaderItem(2,QStandardItem('Date of Data Collection'))
         
         controller = Controller()
         rows = controller.getProjectsFromAccess( str(self.txtFilename.text()) )
         
         num = 0
         for row in rows:
             qtID = QStandardItem( str (row.ProjectID) )
             qtName = QStandardItem( row.ProjectName )
             qtDateCollected = QStandardItem( str( row.DateOfDataCollection ) )
             			
             model.setItem( num, 0, qtID )
             model.setItem( num, 1, qtName)
             model.setItem( num, 2, qtDateCollected)
        
             num = num + 1

         self.tblProjects.setModel(model)
         self.tblProjects.resizeColumnsToContents()
         self.tblProjects.show()
         
     def importAll(self):
         ''' Import all projects '''
         msg = "Are you sure you want to to import all listed projects?"    
         ret = QMessageBox.question(self,"Confirm Import", msg, QMessageBox.Yes|QMessageBox.No)
         # if import is rejected return without deleting
         if ret == QMessageBox.No:
             return

         selectedProjects = []
         # get all project ids as selected items
         for row in range(0, self.tblProjects.model().rowCount()) :
             selectedProjects.append( self.tblProjects.model().item(row,0).text() )
         
         # import projects    
         controller = Controller()
         controller.importProjects( str(self.txtFilename.text()),  selectedProjects )  
       
         # import message
         QMessageBox.information(self,"Importing Data from Access","All projects in the database have been imported.") 
             
         self.close()  
         
     def importSelected(self):
         ''' Import selected projects '''
         numSelected = self.countRowsSelected(self.tblProjects)
         if  numSelected != 0:
             # confirm import
             if numSelected == 1:
                 msg = "Are you sure you want to import the selected project?"
             else:
                 msg = "Are you sure you want to to import the selected projects?"
             
             ret = QMessageBox.question(self,"Confirm Import", msg, QMessageBox.Yes|QMessageBox.No)
             # if import is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get project id of the selected projects
             selectedRows = self.getSelectedRows(self.tblProjects)
             selectedProjects = []
             for row in selectedRows:
                 selectedProjects.append( self.tblProjects.model().item(row,0).text() )
             
             # import selected projects
             controller = Controller()
             controller.importProjects( str(self.txtFilename.text()),  selectedProjects )
             
             # import message
             QMessageBox.information(self,"Importing Data from Access","The selected projects have been imported.") 
             
             self.close()
         else:
             QMessageBox.information(self,"Import Data from Access","Please select the rows containing projects to be imported.") 
