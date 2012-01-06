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

# import controller
from control.controller import Controller

Ui_ExportToOpenIHM, QDialog = uic.loadUiType('./gui/designs/exporttoopenihm.ui')

from mixins import TableViewMixin

class FrmExportToOpenIHM (QDialog, TableViewMixin, Ui_ExportToOpenIHM):
     """FrmExportToOpenIHM inherits QDialog"""

     def __init__ (self, parent = None, projectid=""):
         QDialog.__init__(self, parent)

         self.setupUi(self)
         self.pid = projectid
         self.showProject()

     def __del__ (self):
         self.ui = None
         
     def closeForm(self):
         self.close()
         
     def showProject(self):
         controller = Controller()
         project = controller.getProject( self.pid )
         
         self.lblProjectName.setText( project.projectname )
         self.lblStartDate.setText( str(project.startdate) )
         self.lblCurrency.setText( project.currency )
         
     def exportProject(self):
         ''' export project data to selected file '''
         mydialog = QtGui.QFileDialog()     
        
         filename = mydialog.getSaveFileName(self, 'Export to', '.', 'IHM file (*.ihm)')
        
         if filename:
             controller = Controller()
             controller.exportIhmProject(self.pid, filename)
             QMessageBox.information(self,"Exporting Project to IHM file","Project data has been imported to "+filename) 
             self.close()  
