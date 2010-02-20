#-------------------------------------------------------------------	
#	Filename: frmnewproject.py
#
#	Class to create the Create Project form - FrmNewProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_newproject import Ui_NewProject

class FrmNewProject(Ui_NewProject):	
	''' Creates the Create (New) Project from. Uses the design class
		in gui.designs.ui_newproject. '''	
	def setupUi(self, Form, Mdi):
		''' Set up the dialog box interface '''
		Ui_NewProject.setupUi(self, Form)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.BtnProjectCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)