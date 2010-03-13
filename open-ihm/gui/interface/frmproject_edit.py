#-------------------------------------------------------------------	
#	Filename: frmproject_edit.py
#
#	Class to create the Edit Project form - FrmEditProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Edit Project Dialog design class
from gui.designs.ui_editproject_details import Ui_EditProject

class FrmEditProject(QtGui.QDialog, Ui_EditProject):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, Parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.lblProjectID.setText(str(Parent.projectid))
        self.txtProjectName.setText(Parent.projectname)
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), Parent.mdi.closeActiveSubWindow)
