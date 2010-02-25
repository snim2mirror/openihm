#-------------------------------------------------------------------	
#	Filename: frmmanagelandtypes.py
#
#	Class to create the Manage Expenditure Types form - FrmManageLandTypes.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Land Types Dialog design class
from gui.designs.ui_managelandtypes import Ui_LandTypes

class FrmManageLandTypes(Ui_LandTypes):	
	''' Creates the Manage Expenditure Types from. Uses the design class
		in gui.designs.ui_expendituretypes. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_LandTypes.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnLandTypesClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
