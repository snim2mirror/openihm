#-----------------------------------------------------------------------------------------------	
#	Filename: frmmanagefoodtypes.py
#
#	Class to create the form for adding, editing, or deleting Food Types - FrmManageFoodTypes.
#------------------------------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
from gui.designs.ui_managefoodtypes import Ui_FoodTypes

class FrmManageFoodTypes(Ui_FoodTypes):		
	def setupUi(self,Form,Mdi):
		Ui_FoodTypes.setupUi(self,Form)
		
		QtCore.QObject.connect(self.btnManageFoodClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)

