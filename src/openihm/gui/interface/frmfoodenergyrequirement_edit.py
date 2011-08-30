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

from data.foodenergyrequirement import FoodEnergyRequirement

# import the Create Add Food Energy Requirement Dialog design class
Ui_EditFoodEnergyRequirement, base_class = uic.loadUiType("gui/designs/ui_edit_foodenergyrequirement.ui")

from mixins import MDIDialogMixin

class FrmEditEnergyRequirement(QDialog, Ui_EditFoodEnergyRequirement, MDIDialogMixin):
    
    ''' Creates the edit food energy requirement form '''	

    def __init__(self,parent,selectedage,energyreqmale,energyreqfemale):
        
        ''' Set up the dialog box interface '''
        # self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.age = selectedage
        self.energyreqmale = energyreqmale
        self.energyreqfemale = energyreqfemale

        #set input validator and restrict input to numeric values,
        myAgeVal = QIntValidator(0, 130, self.txtAge)
        myEnergyVal = QIntValidator(0, 10000, self.txtEnergyRequirementMales)
                               
        self.txtAge.setValidator(myAgeVal)
        self.txtEnergyRequirementMales.setValidator(myEnergyVal)
        self.txtEnergyRequirementFemales.setValidator(myEnergyVal)

        #display energy requirements data
        self.showEnergyRequirementDetails()
 
        
    def showEnergyRequirementDetails(self):
        ''' Display energy requirements data '''
        self.txtAge.setText(self.age)
        self.txtEnergyRequirementMales.setText(self.energyreqmale)
        self.txtEnergyRequirementFemales.setText(self.energyreqfemale)


    def saveFoodEnergyRequirementDetails(self):
        ''' Saves newly created food energy requirement data to database '''

        # get the data entered by user
        myage                       = self.txtAge.text()
        malesenergyrequirement      = self.txtEnergyRequirementMales.text()
        femalesenergyrequirement    = self.txtEnergyRequirementFemales.text()
                      	
	# save data entered by user
	
	controller = FoodEnergyRequirement(myage,  malesenergyrequirement,  femalesenergyrequirement)
        controller.setData()      
        # close add food energy requirement window
        self.mdiClose()
