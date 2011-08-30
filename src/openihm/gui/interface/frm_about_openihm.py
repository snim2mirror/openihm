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

# import the About OpenIHM design class
Ui_AboutOpenIHM, base_class = uic.loadUiType("gui/designs/ui_about_openihm.ui")

from mixins import MDIDialogMixin

class FrmAboutOpenIHM(QDialog, Ui_AboutOpenIHM, MDIDialogMixin):
	''' Creates the About Open-IHM from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
