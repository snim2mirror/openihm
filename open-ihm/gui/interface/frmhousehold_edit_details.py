#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_details.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_edithousehold_details import Ui_EditHousehold

class FrmEditHouseholdDetails(QDialog, Ui_EditHousehold):	
    ''' Creates the Edit Household form. '''	
    def __init__(self, parent,  hhid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        self.config = Config.dbinfo().copy()
        
        # get current project details
        self.getHouseholdData()
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(self.parent.projectname)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveHousehold)
        
    def getHouseholdData(self):
        ''' Retrieve and display household data '''
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT hhid, householdname, dateofcollection 
                     FROM households WHERE hhid=%i''' % (self.hhid)
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            hhid = row[0]
            householdname = row[1]
            dateofcollection = row[2]
        
        self.txtShortHouseHoldName.setText(str(hhid))
        self.dtpDateVisted.setDate(dateofcollection)
        self.txtHouseholdName.setText(householdname)
        
    def saveHousehold(self):
        ''' Saves changes to household to database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        hhid                    = self.txtShortHouseHoldName.text()
        householdname     = self.txtHouseholdName.text()
        dateofcollection    = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid                     = self.parent.projectid
        
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
        self.parent.mdi.closeActiveSubWindow()
