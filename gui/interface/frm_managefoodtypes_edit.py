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

from data.foodenergyrequirement import FoodEnergyRequirement
from gui.designs.ui_managefoodtypes_edit import Ui_EditFoodTypes

from mixins import MDIDialogMixin, MySQLMixin

class FrmEditCropType(QDialog, Ui_EditFoodTypes, MDIDialogMixin, MySQLMixin):
    ''' Creates the edit food type form '''	

    def __init__(self, parent, selectedtype,category, measuringunit, energyvalue):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent

        self.name = selectedtype
        self.categoryname = category
        self.measuringunit = measuringunit
        self.energyvalue = energyvalue
        
        #set input validator and restrict input to numeric values,
        myIntVal = QIntValidator(0, 10000, self.txtKCalories)
        self.txtKCalories.setValidator(myIntVal)

        self.showDetailsToEdit()

    def showDetailsToEdit(self):
        ''' Display energy requirements data '''
        self.txtFoodType.setText(self.name)
        self.txtMeasuringUnit.setText(self.measuringunit)
        self.txtKCalories.setText(self.energyvalue)
        if self.categoryname =='crops':
            self.cmbCategory.setCurrentIndex(0)
        elif self.categoryname =='livestock':
            self.cmbCategory.setCurrentIndex(1)
        if self.categoryname =='wildfoods':
            self.cmbCategory.setCurrentIndex(2)            

    def saveDetails(self):
        ''' Saves newly created food energy requirement data to database '''

        # get the data entered by user
        mytype = self.txtFoodType.text()
	mymeasuringunit = self.txtMeasuringUnit.text()
        myenergyvalue  = self.txtKCalories.text()
        mycategory = self.cmbCategory.currentText()  
	if mytype!= '' and mycategory!='':
            
            query = '''UPDATE setup_foods_crops SET name='%s', category='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     	    WHERE name='%s' ''' % (mytype, mycategory, myenergyvalue, mymeasuringunit, mytype)
                    
            self.executeUpdateQuery(query)
            self.txtFoodType.clear()
            self.txtMeasuringUnit.clear()
            self.txtKCalories.clear()

        else:
            QMessageBox.information(self,"Edit Food Type","Name or Category should not be blank")

		
        
        
