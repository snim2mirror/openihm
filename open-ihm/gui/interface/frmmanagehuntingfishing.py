#-------------------------------------------------------------------	
#	Filename: frmmanagefishinghunting.py
#
#	Class to create the Manage Wild Foods form - FrmManageFishingHunting.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Fishing & Hunting Details design class
from gui.designs.ui_managehuntingfishing import Ui_HuntingFishing

class FrmManageHuntingFishing(Ui_HuntingFishing):	
	''' Creates the Manage Hunting & Fishing Details form. Uses the design class
		in gui.designs.ui_managefishinghunting. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_HuntingFishing.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnHuntingFishingClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
