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

from data.simulation_standardofliving import EditStandardOfLivingModelPrice

# import the Create Add Food Energy Requirement Dialog design class
Ui_EditFoodEnergyRequirement, base_class = uic.loadUiType("gui/designs/ui_simulation_editstandardofliving.ui")

from mixins import MDIDialogMixin

class FrmStandardOfLivingModelPrice(QDialog, Ui_EditFoodEnergyRequirement, MDIDialogMixin):
    
    ''' Creates the Edit Simulation Model Price form '''	

    def __init__(self,parent,item,price,modelprice,pid):
        
        ''' Set up the dialog box interface '''
        # self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.item = item
        self.price = price
        self.modelprice = modelprice
        self.pid = pid

        #set input validator and restrict input to numeric values,
        myModelPriceVal = QDoubleValidator(0.0, 10000000.0, 2,self.txtModelprice)
                               
        self.txtModelprice.setValidator(myModelPriceVal)
        self.txtPrice.setValidator(myModelPriceVal)

        #display energy requirements data
        self.showStandardOfLivingDetails()
        
    def showStandardOfLivingDetails(self):
        ''' Display energy requirements data '''
        self.txtItem.setText(self.item)
        self.txtPrice.setText(str(self.price))
        self.txtModelprice.setText(str(self.modelprice))

    def saveStandardOfLivingDetails(self):
        ''' Saves newly created food energy requirement data to database '''

        # get the data entered by user
        mymodelprice = self.txtModelprice.text()
                      	
	# save data entered by user
	controller = EditStandardOfLivingModelPrice(mymodelprice, self.item,self.pid)
        controller.setData()      
