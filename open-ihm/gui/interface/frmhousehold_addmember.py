#-------------------------------------------------------------------	
#	Filename: frmhousehold_addmember.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_addmember import Ui_AddHouseholdMember

class FrmAddHouseholdMember(QDialog, Ui_AddHouseholdMember):	
    ''' Creates the Add Household Member form. '''	
    def __init__(self, parent,  hhid, hhname):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        
        # connect to database
        config = Config.dbinfo().copy()
        self.db = data.mysql.connector.Connect(**config)
        
        # allow the calendar widget to pop up
        now = QDate.currentDate()
        self.dtpDOB.setDate(now)
        self.dtpDOB.setCalendarPopup(True)
        
        # display household name
        self.lblHouseholdName.setText(hhname)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveMember)
        
    def saveMember(self):
        ''' Saves changes to household to database '''    	
        
        # get the data entered by user
        memberid        = self.txtMemberID.text()
        sex   			= self.cboSex.currentText()
        dateofbirth  	= self.dtpDOB.date().toString("yyyy-MM-dd")
        education       = self.txtEducation.text()
        if self.chkHeadHousehold.isChecked():
        	headhousehold = "Yes"
        else:
        	headhousehold = "No"
        
        # create UPDATE query
        query = '''INSERT INTO householdmembers 
			    VALUES(%s,'%s','%s','%s','%s','%s')''' % (self.hhid, memberid, headhousehold, dateofbirth, sex, education)
    
        # execute query and commit changes
        cursor =  self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        
        # close database connection
        cursor.close()
        self.db.close()
        
        # close new project window
        self.parent.retrieveHouseholdMembers()
        self.close()
