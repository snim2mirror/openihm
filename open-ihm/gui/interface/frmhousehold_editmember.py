#-------------------------------------------------------------------	
#	Filename: frmhousehold_editmember.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_editmember import Ui_EditHouseholdMember

class FrmEditHouseholdMember(QDialog, Ui_EditHouseholdMember):	
    ''' Creates the Edit Household Member form. '''	
    def __init__(self, parent,  hhid, hhname, memberid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        self.currentid = memberid
        
        # configure connect to database
        self.config = Config.dbinfo().copy()
        
        # add years to the year of birth combo box: current year to 150 years ago
        thisyear = date.today().year
        for year in range(thisyear, thisyear-151,  -1):
             self.cmbYearOfBirth.addItem("%i" % year)
        
        # display household name
        self.lblHouseholdName.setText(hhname)
        
        # get and display member details
        self.getMemberDetails()
        
        # connect relevant signals and slots
        self.connect(self.txtAge, SIGNAL("textChanged()"), self.updateYearOfBirth)
        self.connect(self.txtAge, SIGNAL("editingFinished()"), self.updateYearOfBirth)
        self.connect(self.cmbYearOfBirth, SIGNAL("currentIndexChanged(int)"), self.updateAge)
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveMember)
        
    def updateYearOfBirth(self):
        ''' updates year of birth when the value of age is modified '''
        thisyear = date.today().year
        age = self.txtAge.text()
        yearOfBirth = thisyear - int(age)
        self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % yearOfBirth ) )
        
    def updateAge(self):
        ''' updates age when year of birth is modified'''
        yearOfBirth = self.cmbYearOfBirth.currentText()
        thisyear = date.today().year
        age = thisyear - int(yearOfBirth)
        self.txtAge.setText( "%i" % age )
        
    def getMemberDetails(self):
		''' retrieves and displays details of the member being editted '''
		pid = self.parent.parent.projectid
		# query to retrieve member details
		query = '''SELECT personid, headofhousehold, yearofbirth, sex 
		           FROM householdmembers WHERE hhid=%s AND personid='%s' AND pid=%s ''' % (self.hhid, self.currentid, pid)
		
		# execute query and commit changes
		db = data.mysql.connector.Connect(**self.config)
		cursor =  db.cursor()
		cursor.execute(query)
		
		for row in cursor.fetchall():
			self.lblMemberID.setText( row[0] )
			
			if row[1] == "Yes":
				self.chkHeadHousehold.setChecked(True)	
			
			age = date.today().year - row[2]
			self.txtAge.setText( "%i" % age )
			self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % row[2] ) )
			
			self.cboSex.setCurrentIndex(self.cboSex.findText(row[3]))
			
		# close database connection
		cursor.close()
		db.close()
			
    def saveMember(self):
		''' Saves changes to household to database '''    	
		
		# get the data entered by user
		sex   			= self.cboSex.currentText()
		age = self.txtAge.text()
		
		if ( sex == "Male"):
		     memberid = "m%s" % age
		else:
		     memberid = "f%s" % age
		     
		education       = ""
		yearofbirth = self.cmbYearOfBirth.currentText()
		if self.chkHeadHousehold.isChecked():
			headhousehold = "Yes"
		else:
			headhousehold = "No"
		
		pid = self.parent.parent.projectid
		# create UPDATE query
		query = '''UPDATE householdmembers SET personid='%s', headofhousehold='%s', yearofbirth=%s, sex='%s',
			    education='%s' WHERE hhid=%s AND personid='%s' AND pid=%s''' % (memberid, headhousehold, yearofbirth, sex, education, self.hhid, self.currentid, pid)
    
		# execute query and commit changes
		db = data.mysql.connector.Connect(**self.config)
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdMembers()
		self.close()
