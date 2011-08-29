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
from PyQt4 import QtGui, QtCore

# import the Manage Employment design class
from gui.designs.ui_manageemployment import Ui_ManageEmployment

from mixins import MDIDialogMixin

class FrmManageEmployment(Ui_ManageEmployment, MDIDialogMixin):    
    ''' Creates the Manage Employment Details form. Uses the design class
        in gui.designs.ui_manageemploymant. '''    
    def setupUi(self, Form, Mdi):
        ''' Set up the dialog box interface '''
        Ui_ManageEmployment.setupUi(self, Form)
        self.parent = Mdi
        # connect relevant signals and slots
        QtCore.QObject.connect(self.btnManageEmploymentClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
