#-------------------------------------------------------------------	
#	Filename: frmassettypes.py
#
#	Class to create the Manage Asset Types form - FrmAssetTypes.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Asset Types Dialog design class
from gui.designs.ui_assettypes import Ui_AssetTypes

class FrmAssetTypes(Ui_AssetTypes):	
	''' Creates the Manage Asset Types from. Uses the design class
		in gui.designs.ui_assettypes. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_AssetTypes.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnAssetTypesClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
