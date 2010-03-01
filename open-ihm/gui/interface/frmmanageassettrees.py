#-------------------------------------------------------------------	
#	Filename: frmmanageassettrees.py
#
#	Class to create the Manage Asset Tree form - FrmManageTrees.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Other Tradable Goods Dialog design class
from gui.designs.ui_managetrees import Ui_Trees

class FrmManageAssetTrees(Ui_Trees):	
	''' Creates the Manage Asset Trees from. Uses the design class
		in gui.designs.ui_manageassettrees. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_Trees.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnOtherTradableGoodsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
