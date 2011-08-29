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

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# import interface design
from gui.designs.ui_databasemessage import Ui_DatabaseMessage

from mixins import MDIDialogMixin

class FrmDatabaseMessage(QDialog, Ui_DatabaseMessage, MDIDialogMixin):
     def __init__(self, message,  parent = None):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)

         self.parent = parent
         self.setupUi(self)
         self.lblMessage.setText( message )
         self.setWindowIcon( QIcon('resources/images/openihm.png') )
