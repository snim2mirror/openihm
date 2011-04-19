#-------------------------------------------------------------------	
#	Filename: frmhousehold_delete.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

# import form design
from gui.designs.ui_household_delete import Ui_DeleteHousehold

class FrmDelHousehold(QDialog, Ui_DeleteHousehold):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
        self.config = Config.dbinfo().copy()
        
        # get projects
        self.getHouseholds()

    def mdiClose(self):
        self.parent.mdi.closeActiveSubWindow()

    def getHouseholds(self):
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT hhid, householdname 
                     FROM households WHERE pid=%i''' % (self.parent.projectid)
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            hhid = row[0]
            householdname = row[1]
            self.cboHouseholdName.addItem(householdname, QVariant(hhid))
            
        cursor.close()
        db.close()
    
    def delHousehold(self):
        ''' Delete Selected Household '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT * FROM households WHERE pid=%i AND hhid=%s''' % (self.parent.projectid, hhid)
        
        cursor.execute(query)
        
        numresult = len(cursor.fetchall())
        
        if numresult:
        	msg = "Are sure sure you want to delete this household?"
        	ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
        	if ret == QMessageBox.Yes:
        		query = '''DELETE FROM households WHERE pid=%i AND hhid=%s''' % (self.parent.projectid, hhid)
        		cursor.execute(query)
        		db.commit()
        		QMessageBox.information(self,"Notice","Household has been deleted")
        else:
        	QMessageBox.information(self, "Notice", "Household Not found")
        	
        cursor.close()
        db.close()
        
        self.close()
        
        
        
        
