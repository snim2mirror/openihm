#-------------------------------------------------------------------	
#	Filename: frmfindhousehold.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config

# import the Create Project Dialog design class
from gui.designs.ui_findhousehold import Ui_FindHousehold
from frmfindhouseholdresults import FrmFindHouseholdResults

from mixins import MDIDialogMixin, MySQLMixin

class FrmFindHousehold(QDialog, Ui_FindHousehold, MDIDialogMixin):
	''' Creates the Find Household form'''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		self.config = Config.dbinfo().copy()

	def findHousehold(self):
		''' Find a household matching the criteria entered by user '''
		hhid 			= self.txtHouseholdNo.text()
		hhname 			= self.txtHouseholdName.text()
	
		SQLcondition 	= ""
		if ( hhid != "" ):
			SQLcondition = " hhid='%s'" % ( hhid )
		
		if ( hhname != "" ):
			if ( SQLcondition == "" ):
				SQLcondition = "householdname LIKE '%" + "%s" % ( hhname ) + "%'" 
			else:
				SQLcondition = "(" + SQLcondition + " OR householdname LIKE '%" + "%s" % ( hhname ) + "%' )" 
				 
		if ( SQLcondition != "" ):  
			query = ''' SELECT hhid FROM households WHERE pid=%i AND %s ''' % ( self.parent.projectid, SQLcondition ) 
		else:
			query = ''' SELECT hhid FROM households WHERE pid=%i ''' % ( self.parent.projectid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		cursor.execute(query)
		count = len( cursor.fetchall() )
		cursor.close()
		db.close()
		
		if ( count != 0 ):
			form = FrmFindHouseholdResults( self.parent, hhid, hhname )
			subWin = self.parent.mdi.addSubWindow( form )
			self.parent.centerSubWindow( subWin )
			# close this form
			self.parent.mdi.closeActiveSubWindow()
			# show the details form
			form.show()
		else:
			msg = "No household matching the criteria specified exists."
			QMessageBox.information( self, "Find Household", msg )
			
		
				
		
				
			
