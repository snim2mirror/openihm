#	Filename: frm_currencymanager.py
#
#	Form for adding and deleting currencies
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
#import data.mysql.connector 

# import the Currency Manager design class
from gui.designs.ui_currencymanager import Ui_CurrencyManager

from mixins import MDIDialogMixin, MySQLMixin

class FrmCurrencyManager(QDialog, Ui_CurrencyManager, MDIDialogMixin, MySQLMixin):	
     ''' Creates the Currency Manager from. '''	

     def __init__(self, parent):
         ''' Set up the dialog box interface '''
         self.parent = parent
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent = parent
         self.currencyid = 0
         
         # connect to database
         self.config = Config.dbinfo().copy()
         
         self.listCurrencies()
         
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
         
     def saveCurrency(self):
         ''' Save the currency details of a currency being added or edited '''
         currencyName = self.txtCurrencyName.text()
         abbreviation = self.txtAbbreviation.text()
         symbol = self.txtSymbol.text()
                  
         # create INSERT or UPDATE query
         if (self.currencyid == 0):
             query = '''INSERT INTO currencies (currencyname,abbreviation,symbol )
                         VALUES('%s','%s','%s') ''' % ( currencyName, abbreviation, symbol )
         else:
             query = ''' UPDATE currencies SET currencyname='%s', abbreviation='%s', symbol='%s'
                         WHERE id=%s ''' % ( currencyName, abbreviation, symbol, self.currencyid)


         self.executeUpdateQuery(query)
         
         # clear text boxes and refresh list
         self.txtCurrencyName.setText("")
         self.txtAbbreviation.setText("")
         self.txtSymbol.setText("")
         self.currencyid = 0
         self.listCurrencies()
         
     def showSelectedCurrency(self, index):
         ''' show details of a selected currency for editing '''
         self.currencyid = self.tblCurrencies.model().item(index.row(),1).text()
         currencyName = self.tblCurrencies.model().item(index.row(),2).text()
         abbreviation = self.tblCurrencies.model().item(index.row(),3).text()
         symbol = self.tblCurrencies.model().item(index.row(),4).text()
         self.txtCurrencyName.setText(currencyName)
         self.txtAbbreviation.setText(abbreviation)
         self.txtSymbol.setText(symbol)
         
     def listCurrencies(self):
         ''' List available currencies '''
         # select query to retrieve currencies
         query = '''SELECT * FROM currencies '''
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('No.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Currency ID'))
         model.setHorizontalHeaderItem(2,QStandardItem('Currency Name'))
         model.setHorizontalHeaderItem(3,QStandardItem('Abbreviation'))
         model.setHorizontalHeaderItem(4,QStandardItem('Symbol'))
         
         # add  data rows
         num = 0

         results = self.executeResultsQuery(query)
         
         for row in results: # cursor.fetchall():
             qtNo = QStandardItem("%i" % (num + 1) )
             qtNo.setTextAlignment( Qt.AlignCenter )
             qtID = QStandardItem("%i" % row[0])
             qtID.setTextAlignment( Qt.AlignCenter )
             qtCurrencyName = QStandardItem( row[1] )	
             qtAbbreviation = QStandardItem( row[2] )
             
             qtSymbol = QStandardItem( row[3] )
             qtSymbol.setTextAlignment( Qt.AlignCenter )
             			
             model.setItem( num, 0, qtNo )
             model.setItem( num, 1, qtID )
             model.setItem( num, 2, qtCurrencyName )
             model.setItem( num, 3, qtAbbreviation )
             model.setItem( num, 4, qtSymbol )
             num = num + 1
         
         self.tblCurrencies.setModel(model)
         self.tblCurrencies.resizeColumnsToContents()
         self.tblCurrencies.hideColumn(1)
         self.tblCurrencies.show()
         
     def delCurrencies(self):
         ''' Delete a selected currencies '''
         numSelected = self.countRowsSelected(self.tblCurrencies)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected currency?"
             else:
                 msg = "Are you sure you want to delete the selected currencies?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected currencies
             selectedRows = self.getSelectedRows(self.tblCurrencies)
             selectedIds = []
             for row in selectedRows:
                 selectedIds.append( self.tblCurrencies.model().item(row,1).text() )

             queries = ["DELETE FROM currencies WHERE id='%s'" % (currencyid)	for currencyid in selectedIds]
             
             self.executeMultipleUpdateQueries(queries)
             
             self.currencyid = 0
             self.listCurrencies()

         else:
             QMessageBox.information(self,"Delete Currencies","Please select the rows containing currencies to be deleted.")
