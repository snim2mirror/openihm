#-------------------------------------------------------------------	
#	Filename: frmmanagelivestock.py
#
#	Class to create the Manage Wild Foods form - FrmManageLivestock.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Livestock Dialog design class
from gui.designs.ui_managelivestock import Ui_LivestockDetails

class FrmManageLivestock(Ui_LivestockDetails):	
	''' Creates the Manage Livestock from. Uses the design class
		in gui.designs.ui_managelivestock. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_LivestockDetails.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnManageLiveStockClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
