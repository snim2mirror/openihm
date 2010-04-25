#------------------------------------------------------------------------------------------------	
#	Filename: frmhousehold_add.py
#
#	Class to create the Add Household form - FrmAddHousehold.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from data.config import Config
import data.mysql.connector 

# import the Create Project Dialog design class
from gui.designs.ui_addhousehold import Ui_AddHousehold

class FrmAddHousehold(QtGui.QDialog, Ui_AddHousehold):	
    ''' Creates the Create (New) Project from. Uses the design class
    in gui.designs.ui_addhousehold. '''	

    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.config = Config.dbinfo().copy()
        
        # set the dates to the date of today
        now = QtCore.QDate.currentDate()
        self.dtpDateVisted.setDate(now)
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(self.parent.projectname)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveHousehold)
        
    def saveHousehold(self):
        ''' Saves newly created household data to database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        hhid                = self.txtShortHouseHoldName.text()
        householdname = self.txtHouseholdName.text()
        dateofcollection       = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid              = self.parent.projectid
        
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
        self.parent.mdi.closeActiveSubWindow()
