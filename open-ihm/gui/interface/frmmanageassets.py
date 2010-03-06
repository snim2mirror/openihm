#-------------------------------------------------------------------	
#	Filename: frmmanageassets.py
#
#	Class to create the Manage Asset Details form - FrmManageAssetDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Asset Types Dialog design class
from gui.designs.ui_manageassets import Ui_ManageAssetDetails

class FrmManageAssetDetails(QtGui.QDialog, Ui_ManageAssetDetails):	
	''' Creates the Manage Asset Details from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)


		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnAssetsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
