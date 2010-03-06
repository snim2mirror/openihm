#-------------------------------------------------------------------	
#	Filename: frmincomesourcedetails.py
#
#	Class to create the Manage Income Types form - FrmIncomeSourceDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Income Dialog design class
from gui.designs.ui_manageincomedetails import Ui_ManageIncome

class FrmIncomeSourceDetails(QtGui.QDialog, Ui_ManageIncome):	
	''' Creates the Manage Income Source Details from. Uses the design class
		in gui.designs.ui_manageincomedetails. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)

		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnManageIncomeClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
