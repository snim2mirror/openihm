#---------------------------------------------------------------------------------------------------------------------	
#	Filename: frmpersonalcharacteristics.py
#
#	Class to create the form for adding, editing, or deleting Personal characteristics - FrmPersonalCharacteristics.
#----------------------------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create House Characteristics Dialog design class
from gui.designs.ui_personalcharacteristics import Ui_PersonalCharacteristics

class FrmPersonalCharacteristics(Ui_PersonalCharacteristics):		
	def setupUi(self,Form,Mdi):
		Ui_PersonalCharacteristics.setupUi(self,Form)
		
		QtCore.QObject.connect(self.btnPCharsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
