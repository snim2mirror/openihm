#-------------------------------------------------------------------	
#	Filename: frmhousehold_addmember.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_addmember import Ui_AddHouseholdMember

from mixins import MDIDialogMixin

class FrmAddHouseholdMember(QDialog, Ui_AddHouseholdMember, MDIDialogMixin):	
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
        
        # add years to the year of birth combo box: current year to 150 years ago
        thisyear = date.today().year
        for year in range(thisyear, thisyear-151,  -1):
             self.cmbYearOfBirth.addItem("%i" % year)
        
        # display household name
        self.lblHouseholdName.setText(hhname)
        
    def updateYearOfBirth(self):
        ''' updates year of birth when the value of age is modified '''
        thisyear = date.today().year
        age = self.txtAge.text()
        if age is not None:
            yearOfBirth = thisyear - int(age)
        self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % yearOfBirth ) )
        
    def updateAge(self):
        ''' updates age when year of birth is modified'''
        yearOfBirth = self.cmbYearOfBirth.currentText()
        thisyear = date.today().year
        age = thisyear - int(yearOfBirth)
        self.txtAge.setText( "%i" % age )
        
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
        periodaway = self.cmbMonthsAbsent.currentText()
        reason = self.txtReason.text()
        whereto = self.txtWhere.text()
        # create UPDATE query
        query = '''INSERT INTO householdmembers 
        	    VALUES('%s',%s,'%s',%s,'%s','%s',%s,%s,'%s','%s')''' % (memberid, self.hhid, headhousehold, yearofbirth, sex, education, pid, periodaway, reason, whereto)
    
        # execute query and commit changes
        cursor =  self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        
        # close database connection
        cursor.close()
        self.db.close()
        
        # close new project window
        self.parent.retrieveHouseholdMembers()
        self.mdiClose()
