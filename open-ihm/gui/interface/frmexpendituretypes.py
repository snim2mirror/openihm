#-------------------------------------------------------------------	
#	Filename: frmexpendituretypes.py
#
#	Class to create the Manage Expenditure Types form - FrmExpenditureTypes.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Asset Types Dialog design class
from gui.designs.ui_expendituretypes import Ui_ExpenditureTypes

class FrmExpenditureTypes(Ui_ExpenditureTypes):	
	''' Creates the Manage Expenditure Types from. Uses the design class
		in gui.designs.ui_expendituretypes. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_ExpenditureTypes.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnExpenditureTypesClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
