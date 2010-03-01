#-------------------------------------------------------------------	
#	Filename: frmothertradablegoods.py
#
#	Class to create the Manage Other Tradable Goods form - FrmOtherTradableGoods.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Other Tradable Goods Dialog design class
from gui.designs.ui_othertradablegoods import Ui_OtherTradableGoods

class FrmOtherTradableGoods(Ui_OtherTradableGoods):	
	''' Creates the Manage Other Tradable Goods from. Uses the design class
		in gui.designs.ui_othertradablegoods. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_OtherTradableGoods.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnOtherTradableGoodsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
