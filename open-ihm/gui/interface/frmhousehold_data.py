#-------------------------------------------------------------------	
#	Filename: frmhousehold_data.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from gui.designs.ui_household_data import Ui_HouseholdData

class FrmHouseholdData(QtGui.QDialog, Ui_HouseholdData):	
	''' Creates the household data (income, assets, expenditure, etc) form '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
