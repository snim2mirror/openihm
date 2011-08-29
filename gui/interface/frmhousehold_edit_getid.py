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

# import forms required to edit household
Ui_EditHouseholdGetID, base_class = uic.loadUiType("gui/designs/ui_edithousehold_getid.ui")


from frmhousehold_edit_details import FrmEditHouseholdDetails

from mixins import MDIDialogMixin

class FrmEditHouseholdGetID(QDialog, Ui_EditHouseholdGetID, MDIDialogMixin):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        self.setupUi(self)
        
        # get projects
        self.getHouseholds()
        
    def getHouseholds(self):
        controller = Controller()
        project = controller.getProject( self.parent.projectid )
        households = project.getHouseholds()
        
        for household in households:
            hhid = household.getHouseholdID()
            householdname = household.getHouseholdName()
            self.cboHouseholdName.addItem(householdname, QVariant(hhid))
    
    def showDetails(self):
        ''' Show Household Details '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]
        form = FrmEditHouseholdDetails(self.parent, hhid)
        subWin = self.parent.mdi.addSubWindow(form)
        self.parent.centerSubWindow(subWin)
        # close this form
        self.parent.mdi.closeActiveSubWindow()
        # show the details form
        form.show()
