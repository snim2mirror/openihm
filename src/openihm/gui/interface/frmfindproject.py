#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""


# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from data.controller import Controller

# import the Create Project Dialog design class
Ui_FindProject, base_class = uic.loadUiType("gui/designs/ui_findproject.ui")

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
