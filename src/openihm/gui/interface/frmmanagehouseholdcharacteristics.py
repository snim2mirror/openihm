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
from frmmanagehouseholdcharacteristics_add import FrmAddHouseholdCharacteristic

Ui_ManageHouseholdCharacteristics, QDialog = uic.loadUiType('./gui/designs/ui_managehouseholdcharacteristics.ui')

from mixins import MDIDialogMixin, TableViewMixin

class FrmManageHouseholdCharacteristics (QDialog, TableViewMixin, MDIDialogMixin, Ui_ManageHouseholdCharacteristics):
     """FrmManageHouseholdCharacteristics inherits QDialog"""

     def __init__ (self, parent = None):
         QDialog.__init__(self, parent)

         self.setupUi(self)
         
         self.parent = parent
         
         self.loadCharacteristics()

     def __del__ (self):
         self.ui = None
         
     def closeForm(self):
         self.mdiClose()  # defined in mixins
         
     def addCharacteristic(self):
         form = FrmAddHouseholdCharacteristic(self)
         form.exec_()
         
     def editCharacteristic(self):
         if self.countRowsSelected(self.tblHouseholdCharacteristics) != 0:
             # get the characteristic name
             selectedRow = self.getCurrentRow(self.tblHouseholdCharacteristics)
             charname = self.tblHouseholdCharacteristics.model().item(selectedRow,0).text()
             # show edit household characteristic form
             form = FrmAddHouseholdCharacteristic(self, charname)
             form.exec_()
         else:
             QMessageBox.information(self,"Edit Household Characteristic","Please select the row containing a household characteristic to be editted.")
         
     def delCharacteristic(self):
         numSelected = self.countRowsSelected(self.tblHouseholdCharacteristics)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected characteristic?"
             else:
                 msg = "Are you sure you want to delete the selected characteristicss?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             # delete selected characteristics
             controller = Controller()
             selectedRows = self.getSelectedRows(self.tblHouseholdCharacteristics)
             for row in selectedRows:
                 charname = self.tblHouseholdCharacteristics.model().item(row,0).text()
                 controller.delCharacteristic(charname)

             self.loadCharacteristics()

         else:
             QMessageBox.information(self,"Delete Characteristics","Please select the rows containing characteristics to be deleted.")
         
     def loadCharacteristics(self):
         
         model = QStandardItemModel(1,1)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
         model.setHorizontalHeaderItem(1,QStandardItem('Data Type'))
         model.setHorizontalHeaderItem(2,QStandardItem('Description'))
         
         # get characteristics
         controller = Controller()
         characteristics = controller.getGlobalCharacteristics("Household")
         
         num = 0
         for char in characteristics:
             qtName = QStandardItem( char.name )
             qtDataType = QStandardItem( char.datatypestr )
             qtDescription = QStandardItem( char.description )
             			
             model.setItem( num, 0, qtName )
             model.setItem( num, 1, qtDataType)
             model.setItem( num, 2, qtDescription)
        
             num = num + 1

         self.tblHouseholdCharacteristics.setModel(model)
         self.tblHouseholdCharacteristics.resizeColumnsToContents()
         self.tblHouseholdCharacteristics.show()
