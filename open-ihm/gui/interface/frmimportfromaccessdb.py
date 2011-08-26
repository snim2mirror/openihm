from PyQt4 import QtGui, QtCore,  uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyodbc

# import controller
from data.controller import Controller

(Ui_ImportFromAccessDB, QDialog) = uic.loadUiType('./gui/designs/importfromaccessdb.ui')

class FrmImportFromAccessDB (QDialog, Ui_ImportFromAccessDB):
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
     
     # START: to be replaced with mixins by Sarah    
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
     # END: to be replaced with mixins by Sarah
         
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
         DBfile = str(self.txtFilename.text())
         conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
         cursor = conn.cursor()
 
         SQL = 'SELECT ProjectID, ProjectName, DateOfDataCollection FROM TblProject'
         cursor.execute(SQL)
         
         model = QStandardItemModel(1,1)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Project ID'))
         model.setHorizontalHeaderItem(1,QStandardItem('Project Name'))
         model.setHorizontalHeaderItem(2,QStandardItem('Date of Data Collection'))
         
         num = 0
         for row in cursor.fetchall():
             qtID = QStandardItem( str (row.ProjectID) )
             qtName = QStandardItem( row.ProjectName )
             qtDateCollected = QStandardItem( str( row.DateOfDataCollection ) )
             			
             model.setItem( num, 0, qtID )
             model.setItem( num, 1, qtName)
             model.setItem( num, 2, qtDateCollected)
        
             num = num + 1
             
         cursor.close()
         conn.close()

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

         DBfile = str(self.txtFilename.text())
         conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
         cursor = conn.cursor()
             
         # need projectid, projectname, startdate, enddate, description and currency
         SQL = 'SELECT ProjectID, ProjectName, DateOfDataCollection, Currency FROM TblProject'
         cursor.execute(SQL)
             
         # old IHM does not have these
         description = ""
         enddate = "0000-00-00"
             
         # transfer retrieved projects
         controller      = Controller()
         for row in cursor.fetchall():
             projectname = row.ProjectName
             startdate = row.DateOfDataCollection
             currency = row.Currency
             project         = controller.addProject(projectname, startdate, enddate, description, currency)
         
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
             selectedItems = []
             for row in selectedRows:
                 selectedItems.append( self.tblProjects.model().item(row,0).text() )
             # import selected projects
             
             DBfile = str(self.txtFilename.text())
             conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
             cursor = conn.cursor()
             
             projectIDs = ""
             for item in selectedItems:
                 projectIDs = item if projectIDs == "" else projectIDs + ",%s" % item
            
             # need projectid, projectname, startdate, enddate, description and currency
             SQL = '''SELECT ProjectID, ProjectName, DateOfDataCollection, Currency FROM TblProject 
                        WHERE ProjectID IN (%s) ''' % (projectIDs) 
             print SQL
             cursor.execute(SQL)
             
             # old IHM does not have these
             description = ""
             enddate = "0000-00-00"
             
             # transfer retrieved projects
             controller      = Controller()
             for row in cursor.fetchall():
                 projectname = row.ProjectName
                 startdate = row.DateOfDataCollection
                 currency = row.Currency
                 project         = controller.addProject(projectname, startdate, enddate, description, currency)
         else:
             QMessageBox.information(self,"Import Data from Access","Please select the rows containing projects to be imported.") 
