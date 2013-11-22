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
from mixins import MDIDialogMixin, TableViewMixin
from data.report_settingsmanager import ReportsSettingsManager
from frm_report_disposableincome import HouseholdDisposableIncome
from outputs.routines.report_disposable_income import DisposableHouseholdIncome

Ui_AssetsByDisposableIncome, base_class = uic.loadUiType("gui/designs/ui_report_assets.ui")

class FrmAssetsByDisposableIncome(QDialog, Ui_AssetsByDisposableIncome,MDIDialogMixin,TableViewMixin):
    
    ''' Creates the run simulations form '''	
    def __init__(self, parent, hhid=0):
        
	''' Set up the dialog box interface '''
	QDialog.__init__(self)
	self.setupUi(self)
	self.parent = parent
	
    def getPorjects(self):
        ''' populate projects combobox with available projects'''
                
        pass

    def getselectedProject(self):
        ''' get name of project selected by user'''
                
        pass
                
    def getProjectID(self):

        ''' get ID for the selected project'''
                
        pass
