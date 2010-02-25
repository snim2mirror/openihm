#-------------------------------------------------------------------	
#	Filename: frmincomesourcetypes.py
#
#	Class to create the Manage Income Types form - FrmIncomeSourcesTypes.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Asset Types Dialog design class
from gui.designs.ui_incomesourcetypes import Ui_IncomeSourcesTypes

class FrmIncomeSourcesTypes(Ui_IncomeSourcesTypes):	
	''' Creates the Manage Income Sources Types from. Uses the design class
		in gui.designs.ui_incomesourcetypes. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_IncomeSourcesTypes.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.btnIncomeSourcesClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
