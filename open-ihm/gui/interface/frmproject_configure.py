#---------------------------------------------------------------------------------	
#	Filename: frmproject_configure.py
#
#	Class to create the Configure Project form - FrmConfigureProject.
#---------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_projectconfiguration import Ui_ProjectConfiguration

class FrmConfigureProject(QtGui.QDialog, Ui_ProjectConfiguration):	
	''' Creates the Edit Project form. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
