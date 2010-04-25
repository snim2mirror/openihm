#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_getid.py
#
#	form that gets the ID of a household to be editted.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

# import forms required to edit household
from gui.designs.ui_edithousehold_getid import Ui_EditHouseholdGetID
from frmhousehold_edit_details import FrmEditHouseholdDetails

class FrmEditHouseholdGetID(QDialog, Ui_EditHouseholdGetID):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        self.setupUi(self)
        
        self.config = Config.dbinfo().copy()
        
        # get projects
        self.getHouseholds()
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdOk, SIGNAL("clicked()"), self.showDetails)
        
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
    
    def showDetails(self):
        ''' Show Household Details '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]
        form = FrmEditHouseholdDetails(self.parent, hhid)
        subWin = self.parent.mdi.addSubWindow(form)
        self.parent.centerSubWindow(subWin)
        # close this form
        self.parent.mdi.closeActiveSubWindow()
        # show the details form
        form.show()
