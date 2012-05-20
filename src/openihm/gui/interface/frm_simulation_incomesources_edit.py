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

from data.simulation_incomesources import EditIncomeSourcesModelPrice

# import the Create Add Food Energy Requirement Dialog design class
Ui_EditIncomeSourceModelDetails, base_class = uic.loadUiType("gui/designs/ui_setincomesimulationvalues.ui")

from mixins import MDIDialogMixin

class FrmIncomeSourceModelDetails(QDialog, Ui_EditIncomeSourceModelDetails, MDIDialogMixin):
    
    ''' Creates the Edit Simulation Model Price form '''	

    def __init__(self,parent,incomesourcecategory,incomesource,percentageprice,percentageproduction,projectid):
        
        ''' Set up the dialog box interface '''
        # self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.incomesourcecategory = incomesourcecategory
        self.incomesource = incomesource
        self.percentageprice = percentageprice
        self.percentageproduction = percentageproduction
        self.projectid = projectid

        #set input validator and restrict input to numeric values,
        myPriceVal = QDoubleValidator(0, 100000000000.0,2, self.txtPercentReferencePrice)
                               
        self.txtPercentReferencePrice.setValidator(myPriceVal)
        self.txtPercentReferenceProduction.setValidator(myPriceVal)

        #display energy requirements data
        self.showIncomeSourceDetails()
 
    def showIncomeSourceDetails(self):
        ''' Display energy requirements data '''
        self.txtIncomeSource.setText(self.incomesource)
        self.txtPercentReferencePrice.setText(self.percentageprice)
        self.txtPercentReferenceProduction.setText(self.percentageproduction)

    def saveIncomeSourceDetails(self):
        ''' Saves income source model data to database '''

        # get the data entered by user
        mpercentageprice = self.txtPercentReferencePrice.text()
        mpercentageproduction = self.txtPercentReferenceProduction.text()
                      	
	# save data entered by user
	controller = EditIncomeSourcesModelPrice(self.incomesourcecategory,self.incomesource,mpercentageprice, mpercentageproduction, self.projectid)
        controller.setData()      
