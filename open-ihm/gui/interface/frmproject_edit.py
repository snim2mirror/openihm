#-------------------------------------------------------------------	
#	Filename: frmproject_edit.py
#
#	Class to create the Edit Project form - FrmEditProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_editproject_details import Ui_EditProject

class FrmEditProject(QtGui.QDialog, Ui_EditProject):	
	''' Creates the Edit Project form. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
