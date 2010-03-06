#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_details.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from gui.designs.ui_edithousehold_details import Ui_EditHousehold

class FrmEditHouseholdDetails(QtGui.QDialog, Ui_EditHousehold):	
	''' Creates the Edit Project form. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
