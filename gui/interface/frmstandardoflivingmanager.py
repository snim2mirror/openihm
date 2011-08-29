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

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from data.config import Config
import includes.mysql.connector as connector

# import the Standard of Living  Manager design class
Ui_StandardOfLivingManager, base_class = uic.loadUiType("gui/designs/ui_manage_standardofliving.ui")

from mixins import MDIDialogMixin, TableViewMixin

class FrmStandardOfLivingManager(QDialog, Ui_StandardOfLivingManager, TableViewMixin, MDIDialogMixin):	
     ''' Creates the Standard of Living Manager form. '''	

     def __init__(self, parent):
         ''' Set up the dialog box interface '''
         self.parent = parent
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent = parent
         self.currentitem = ""
         
         # connect to database
         self.config = Config.dbinfo().copy()
         
         self.listItems()
         
     def saveItem(self):
         ''' Save the details of an item being added or edited '''
         itemname = self.txtItem.text()
         itemtype = self.cmbItemType.currentText()
         
         db = connector.Connect(**self.config)
         
         # create INSERT or UPDATE query
         if (self.currentitem == ""):
             query = '''INSERT INTO setup_standardofliving (item,type )
                         VALUES('%s','%s') ''' % ( itemname, itemtype )
         else:
             query = ''' UPDATE setup_standardofliving SET item='%s', type='%s'
                             WHERE item='%s' ''' % ( itemname, itemtype, self.currentitem)
         
         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()
         
         # close database connection
         cursor.close()
         db.close()
         
         # clear text boxes and refresh list
         self.txtItem.setText("")
         self.currentitem = ""
         self.listItems()
         
     def showSelectedItem(self, index):
         ''' show details of a selected standard of living item for editing '''
         self.currentitem = self.tblStandardOfLiving.model().item(index.row(),0).text()
         itemtype = self.tblStandardOfLiving.model().item(index.row(),1).text()
         self.txtItem.setText(self.currentitem)
         self.cmbItemType.setCurrentIndex( self.cmbItemType.findText( itemtype ) )
         
     def listItems(self):
         ''' List available currencies '''
         # select query to retrieve currencies
         query = '''SELECT * FROM setup_standardofliving '''
         
         # retrieve and display members
         db = connector.Connect(**self.config)             
         cursor = db.cursor()
         
         cursor.execute(query)
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Item Name'))
         model.setHorizontalHeaderItem(1,QStandardItem('Item Type'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
             qtItem = QStandardItem( row[0] )	
             qtItemType = QStandardItem( row[1] )
             			
             model.setItem( num, 0, qtItem )
             model.setItem( num, 1, qtItemType)
        
             num = num + 1
             
         cursor.close()   
         db.close()
         
         self.tblStandardOfLiving.setModel(model)
         self.tblStandardOfLiving.resizeColumnsToContents()
         self.tblStandardOfLiving.show()
         
     def delItems(self):
         ''' Delete a selected items '''
         numSelected = self.countRowsSelected(self.tblStandardOfLiving)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected item?"
             else:
                 msg = "Are you sure you want to delete the selected items?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected items
             selectedRows = self.getSelectedRows(self.tblStandardOfLiving)
             selectedItems = []
             for row in selectedRows:
                 selectedItems.append( self.tblStandardOfLiving.model().item(row,0).text() )
             # delete selected items
             
             db = connector.Connect(**self.config)
             cursor =  db.cursor()
             
             for itemname in selectedItems:
                 query = '''DELETE FROM setup_standardofliving WHERE item='%s' ''' % (itemname)	
                 cursor.execute(query)
                 db.commit()
    
             # close database connection
             cursor.close()
             db.close()
             
             self.currentitem = ""
             self.listItems()

         else:
             QMessageBox.information(self,"Delete Standard of Living Items","Please select the rows containing items to be deleted.")
