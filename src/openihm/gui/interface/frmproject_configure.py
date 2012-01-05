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

from control.controller import Controller

# import the Create Project Dialog design class
Ui_ProjectConfiguration, base_class = uic.loadUiType("gui/designs/ui_projectconfiguration.ui")

from frmproject_configure_cropincome import CropIncomeManager
from frmproject_configure_livestockincome import LivestockIncomeManager
from frmproject_configure_wildfoodincome import WildfoodIncomeManager
from frmproject_configure_employmentincome import EmploymentIncomeManager
from frmproject_configure_transferincome import TransferIncomeManager
from frmproject_configure_householdcharacteristics import HouseholdCharacteristicsManager
from frmproject_configure_personalcharacteristics import PersonalCharacteristicsManager
from frmproject_configure_standardofliving import StandardOfLivingManager
from frmproject_configure_diet import DietManager

from mixins import MDIDialogMixin, MySQLMixin, TableViewMixin

class FrmConfigureProject(QDialog, Ui_ProjectConfiguration, PersonalCharacteristicsManager,  HouseholdCharacteristicsManager,  DietManager,  StandardOfLivingManager,  CropIncomeManager, LivestockIncomeManager, WildfoodIncomeManager, EmploymentIncomeManager, TransferIncomeManager, TableViewMixin, MySQLMixin, MDIDialogMixin):	
     ''' Creates the Edit Project form. '''	
     def __init__(self, parent):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.parent = parent
         self.dietid = 0                     # selected diet item
         self.currentItem = ""           # selected standard of living item
         self.setupUi(self)
        
         controller = Controller()
         self.project = controller.getProject( self.parent.projectid )
        
         # show first tab first
         self.tabProject.setCurrentIndex(0)
        
         # display project name
         self.lblProjectName.setText(self.parent.projectname)
        
         # display Available and Selected Household Characteristics
         self.displayAvailableHouseholdCharacteristics()
         self.displaySelectedHouseholdCharacteristics()
         
         self.displayAvailablePersonalCharacteristics()
         self.displaySelectedPersonalCharacteristics()
         
         self.listDiets()
         self.getCropTypes()
         self.displayStandardOfLiving()
         self.getExpenseItems()
         self.getAgeRange(self.cmbAgeBottom, 0, 100)
         self.getAgeRange(self.cmbAgeTop, 1, 101)
         
         self.displayAvailableCrops()
         self.displaySelectedCrops()
         
         self.displayAvailableLivestock()
         self.displaySelectedLivestock()
         
         self.displayAvailableWildfoods()
         self.displaySelectedWildfoods()
         
         self.displayAvailableEmployment()
         self.displaySelectedEmployment()
         
         self.displayAvailableTransfers()
         self.displaySelectedTransfers()
