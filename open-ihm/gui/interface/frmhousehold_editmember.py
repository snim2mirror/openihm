#-------------------------------------------------------------------	
#	Filename: frmhousehold_editmember.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_editmember import Ui_EditHouseholdMember

class FrmEditHouseholdMember(QDialog, Ui_EditHouseholdMember):	
    ''' Creates the Add Household Member form. '''	
    def __init__(self, parent,  hhid, hhname, memberid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        self.currentid = memberid
        
        # configure connect to database
        self.config = Config.dbinfo().copy()
        
        # allow the calendar widget to pop up
        now = QDate.currentDate()
        self.dtpDOB.setDate(now)
        self.dtpDOB.setCalendarPopup(True)
        
        # display household name
        self.lblHouseholdName.setText(hhname)
        
        # get and display member details
        self.getMemberDetails()
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveMember)
        
    def getMemberDetails(self):
		''' retrieves and displays details of the member being editted '''
		# query to retrieve member details
		query = '''SELECT personid, headofhousehold, dateofbith, sex, education 
		           FROM householdmembers WHERE hhid=%s AND personid=%s''' % (self.hhid, self.currentid)
		
		# execute query and commit changes
		db = data.mysql.connector.Connect(**self.config)
		cursor =  db.cursor()
		cursor.execute(query)
        
		for row in cursor.fetchall():
			self.txtMemberID.setText( "%i" % row[0])
			
			if row[1] == 1:
				self.chkHeadHousehold.setChecked(True)	
			
			self.dtpDOB.setDate( row[2] )
			
			self.cboSex.setCurrentIndex(self.cboSex.findText(row[3]))
			
			self.txtEducation.setText( row[4] )
			
		# close database connection
		cursor.close()
		db.close()
        	
        
    def saveMember(self):
		''' Saves changes to household to database '''    	
		
		# get the data entered by user
		memberid        = self.txtMemberID.text()
		sex   			= self.cboSex.currentText()
		dateofbirth  	= self.dtpDOB.date().toString("yyyy-MM-dd")
		education       = self.txtEducation.text()
		if self.chkHeadHousehold.isChecked():
			headhousehold = 1
		else:
			headhousehold = 0
		
		# create UPDATE query
		query = '''UPDATE householdmembers SET personid=%s, headofhousehold=%s, dateofbith='%s', sex='%s',
			    education='%s' WHERE hhid=%s AND personid=%s ''' % (memberid, headhousehold, dateofbirth, sex, education, self.hhid, self.currentid)
    
		# execute query and commit changes
		db = data.mysql.connector.Connect(**self.config)
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.displayHouseholdMembers()
		self.close()
