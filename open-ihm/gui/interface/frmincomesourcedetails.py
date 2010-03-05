#-------------------------------------------------------------------	
#	Filename: frmincomesourcedetails.py
#
#	Class to create the Manage Income Types form - FrmIncomeSourceDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Income Dialog design class
from gui.designs.ui_manageincomedetails import Ui_ManageIncome

class FrmIncomeSourceDetails(Ui_ManageIncome):	
	''' Creates the Manage Income Source Details from. Uses the design class
		in gui.designs.ui_manageincomedetails. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_ManageIncome.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnManageIncomeClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
