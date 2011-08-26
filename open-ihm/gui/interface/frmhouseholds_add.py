#------------------------------------------------------------------------------------------------	
#	Filename: frmhouseholds_add.py
#
#	Class to create the Add Household form - FrmAddHousehold.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import includes.mysql.connector as connector

# import the Create Project Dialog design class
from gui.designs.ui_households_add import Ui_Households_Add

from mixins import MDIDialogMixin

class FrmAddHousehold(QDialog, Ui_Households_Add, MDIDialogMixin):	
    ''' Creates the add household form '''	

    def __init__(self, parent, projectid, projectname):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.projectid = projectid
        self.config = Config.dbinfo().copy()
        self.mdi = None
        
        # set the dates to the date of today
        now = QDate.currentDate()
        self.dtpDateVisted.setDate(now)
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(projectname)

    def saveHousehold(self):
        ''' Saves newly created household data to database '''
        
        # connect to mysql database
        db = connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        hhid             = self.txtShortHouseHoldName.text()
        householdname 	 = self.txtHouseholdName.text()
        dateofcollection = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid              = self.projectid
        
        # create INSERT INTO query
        query = '''INSERT INTO households(hhid,pid,dateofcollection,householdname) 
                     VALUES(%s,%s, '%s', '%s')''' % (hhid, pid, dateofcollection, householdname)
                     
    
        # execute query and commit changes
        cursor.execute(query)
        db.commit()
        
        # close database connection
        cursor.close()
        db.close()
        
        # close new project window
        self.parent.getHouseholds()
        self.mdiClose()
