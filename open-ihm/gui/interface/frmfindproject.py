#-------------------------------------------------------------------	
#	Filename: frmfindproject.py
#
#	Class to create the Create Project form - FrmFindProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

# import the Create Project Dialog design class
from gui.designs.ui_findproject import Ui_FindProject
from frmfindprojectresults import FrmFindProjectResults

from mixins import MDIDialogMixin

class FrmFindProject(QDialog, Ui_FindProject, MDIDialogMixin):	
    ''' Creates the Find Project from, under the Project menu. Uses the design class
        in gui.designs.ui_findproject. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent

    def findProject(self):
        ''' Find a project matching the criteria entered by user '''
        pid 			= self.txtProjectID.text()
        ptitle 			= self.txtProjectTitle.text()
        controller  = Controller()
        if ( controller.existsProjectMatching( pid,  ptitle ) ):
            form = FrmFindProjectResults(self.parent, pid, ptitle)
            subWin = self.parent.mdi.addSubWindow(form)
            self.parent.centerSubWindow(subWin)
            # close this form
            self.parent.mdi.closeActiveSubWindow()
            # show the details form
            form.show()
        else:
            msg = "No project matching the criteria specified exists."
            QMessageBox.information(self,"Find Project", msg)
