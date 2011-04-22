#	Filename: frmstandardoflivingmanager.py
#
#	Form for adding and deleting standardofliving items
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

# import the Standard of Living  Manager design class
from gui.designs.ui_manage_standardofliving import Ui_StandardOfLivingManager

from mixins import MDIDialogMixin

class FrmStandardOfLivingManager(QDialog, Ui_StandardOfLivingManager, MDIDialogMixin):	
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

     def countRowsSelected(self, tblVw):
         selectedRows = self.getSelectedRows(tblVw)
         return len(selectedRows)
         
     def getSelectedRows(self, tblVw):
         selectedRows = []
         selectedIndexes = tblVw.selectedIndexes()
         
         for indexVal in selectedIndexes:
             if indexVal.row() not in selectedRows:
                 selectedRows.append(indexVal.row())
                 
         return selectedRows
                 
     def getCurrentRow(self, tblVw):
         indexVal = tblVw.currentIndex()
         return indexVal.row()
         
     def saveItem(self):
         ''' Save the details of an item being added or edited '''
         itemname = self.txtItem.text()
         itemtype = self.cmbItemType.currentText()
         
         db = data.mysql.connector.Connect(**self.config)
         
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
         ''' show details of a selected currency for editing '''
         self.currentitem = self.tblStandardOfLiving.model().item(index.row(),0).text()
         itemtype = self.tblStandardOfLiving.model().item(index.row(),1).text()
         self.txtItem.setText(self.currentitem)
         self.cmbItemType.setCurrentIndex( self.cmbItemType.findText( itemtype ) )
         
     def listItems(self):
         ''' List available currencies '''
         # select query to retrieve currencies
         query = '''SELECT * FROM setup_standardofliving '''
         
         # retrieve and display members
         db = data.mysql.connector.Connect(**self.config)             
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
             
             db = data.mysql.connector.Connect(**self.config)
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
