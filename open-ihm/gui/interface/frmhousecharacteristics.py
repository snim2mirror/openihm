#---------------------------------------------------------------------------------------------------------------------	
#	Filename: frmhousecharacteristics.py
#
#	Class to create the form for adding, editing, or deleting Household characteristics - FrmHouseCharacteristics.
#----------------------------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create House Characteristics Dialog design class
from gui.designs.ui_housecharacteristics import Ui_HouseCharacteristics

class FrmHouseCharacteristics(Ui_HouseCharacteristics):		
	def setupUi(self,Form,Mdi):
		Ui_HouseCharacteristics.setupUi(self,Form)
		
		QtCore.QObject.connect(self.btnHouseClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
