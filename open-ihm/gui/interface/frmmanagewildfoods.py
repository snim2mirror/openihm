#-------------------------------------------------------------------	
#	Filename: frmmanagewildfoods.py
#
#	Class to create the Manage Wild Foods form - FrmManageWildFoods.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Other Tradable Goods Dialog design class
from gui.designs.ui_managewildfoods import Ui_WildFoods

class FrmManageWildFoods(Ui_WildFoods):	
	''' Creates the Manage Wild Foods from. Uses the design class
		in gui.designs.ui_managewildfoods. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_WildFoods.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnManageWildFoodsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
