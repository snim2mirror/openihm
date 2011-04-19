#-------------------------------------------------------------------	
#	Filename: frmhouseholds_edit.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_households_edit import Ui_Households_Edit

class FrmEditHousehold(QDialog, Ui_Households_Edit):	
    ''' Creates the Edit Household form. '''	
    def __init__(self, parent, projectid, projectname, hhid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.projectid = projectid
        self.hhid = hhid
        self.config = Config.dbinfo().copy()
        self.mdi = None
        
        # get current project details
        self.getHouseholdData()
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(projectname)
        
    def setMdi(self, mdi):
        self.mdi = mdi
        
    def mdiClose(self):
	self.mdi.closeActiveSubWindow()

    def getHouseholdData(self):
        ''' Retrieve and display household data '''
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT hhid, householdname, dateofcollection 
                     FROM households WHERE hhid=%s''' % (self.hhid)
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            hhid = row[0]
            householdname = row[1]
            dateofcollection = row[2]
            
        # close database connection
        cursor.close()
        db.close()
        
        self.txtShortHouseHoldName.setText(str(hhid))
        self.dtpDateVisted.setDate(dateofcollection)
        self.txtHouseholdName.setText(householdname)
        
    def saveHousehold(self):
        ''' Saves changes to household to database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        hhid              = self.txtShortHouseHoldName.text()
        householdname     = self.txtHouseholdName.text()
        dateofcollection  = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid               = self.projectid
        
        # create UPDATE query
        query = '''UPDATE households SET hhid=%s, dateofcollection='%s', householdname='%s'
                     WHERE hhid=%s AND pid=%s''' % (hhid, dateofcollection, householdname,  self.hhid,  pid)
    
        # execute query and commit changes
        cursor.execute(query)
        db.commit()
        
        # close database connection
        cursor.close()
        db.close()
        
        # close new project window
        self.parent.getHouseholds()
        self.close()
