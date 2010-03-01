#-------------------------------------------------------------------	
#	Filename: frmmanagelivestockproducts.py
#
#	Class to create the Manage Wild Foods form - FrmManageLivestockProducts.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Livestock Dialog design class
from gui.designs.ui_managelivestockproducts import Ui_LivestockProducts

class FrmManageLivestockProducts(Ui_LivestockProducts):	
	''' Creates the Manage Livestock Products from. Uses the design class
		in gui.designs.ui_managelivestockproducts. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_LivestockProducts.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnLiveStockProductsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
