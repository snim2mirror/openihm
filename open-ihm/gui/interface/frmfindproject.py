#-------------------------------------------------------------------	
#	Filename: frmfindproject.py
#
#	Class to create the Create Project form - FrmFindProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_findproject import Ui_FindProject

class FrmFindProject(QtGui.QDialog, Ui_FindProject):	
	''' Creates the Find Project from, under the Edit menu. Uses the design class
		in gui.designs.ui_findproject. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.btnFindProjectClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
