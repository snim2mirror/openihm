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

Ui_AddHouseholdCharacteristic, QDialog = uic.loadUiType('./gui/designs/ui_managehouseholdcharacteristic_add.ui')

class FrmAddHouseholdCharacteristic (QDialog, Ui_AddHouseholdCharacteristic):
     """FrmAddHouseholdCharacteristic inherits QDialog"""

     def __init__ (self, parent = None,  characteristic=""):
         QDialog.__init__(self, parent)

         self.setupUi(self)
         
         self.parent = parent
         self.characteristic = characteristic
         
         if self.characteristic != "":
             self.setWindowTitle("Edit Household Characteristic")
             self.showDetails()

     def __del__ (self):
         self.ui = None
         
     def closeForm(self):
         self.close()
         
     def showDetails(self):
         controller = Controller()
         char = controller.getGlobalCharacteristic(self.characteristic)
         self.txtCharacteristic.setText( char.name )
         self.txtDescription.setText( char.description )
         self.cmbDataType.setCurrentIndex( self.cmbDataType.findText( char.datatypestr ) )
              
     def saveCharacteristic(self):
         controller = Controller()
         
         charname = self.txtCharacteristic.text()
         datatype = self.getDataType( self.cmbDataType.currentText() )
         description = self.txtDescription.text()
         
         if self.characteristic == "":
             if controller.existsGlobalCharacteristic( charname ):
                 QMessageBox.information(self,"Add Household Characteristic","Household Characteristic Already Exists.")
                 return
             else:
                 controller.addGlobalCharacteristic(charname, "Household", datatype, description)
         else:
             char = controller.getGlobalCharacteristic( self.characteristic )
             char.editData(charname, "Household", datatype, description)
         
         self.parent.loadCharacteristics()
         
         self.close()
         
     def getDataType(self,  strDataType):
         if strDataType == "Boolean/Yes/No":
             return 1
         elif strDataType == "Integer":
             return 2
         elif strDataType == "String":
             return 3
         elif strDataType == "Double":
             return 4
         else:
             return 3
