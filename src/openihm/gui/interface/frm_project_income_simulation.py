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
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from data.config import Config
from control.controller import Controller
from mixins import MDIDialogMixin


Ui_HouseholdData, base_class = uic.loadUiType("gui/designs/ui_simulation.ui")

class FrmRunIncomeSimulation(QDialog, Ui_HouseholdData,MDIDialogMixin):
    
    ''' Creates the run simulations form '''	
    def __init__(self, parent, hhid=0):
        
	''' Set up the dialog box interface '''
	QDialog.__init__(self)
	self.setupUi(self)
	self.parent = parent
