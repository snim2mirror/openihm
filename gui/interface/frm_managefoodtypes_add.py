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
from gui.designs.ui_managefoodtypes_add import Ui_AddFoodTypes

from mixins import MDIDialogMixin, MySQLMixin

class FrmAddFoodCropType(QDialog, Ui_AddFoodTypes, MySQLMixin, MDIDialogMixin):
    ''' Creates the add food/crop energy requirement form '''	

    def __init__(self, parent, mdi):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.mdi = mdi
        
        #set input validator and restrict input to numeric values,
        myIntVal = QIntValidator(0, 10000, self.txtKCalories)
        self.txtKCalories.setValidator(myIntVal);
        
    def saveDetails(self):
        ''' Saves newly created food/crop energy requirement data to database '''

        # get the data entered by user
        myfoodtype = self.txtFoodType.text()
        mycategory = self.cmbCategory.currentText()
	mymeasuringunit = self.cmbUnitOfMeasure.currentText()
        myenergyvalue  = self.txtKCalories.text()
        	
	# check if record exists
	query = '''SELECT name, energyvalueperunit, unitofmeasure
			FROM setup_foods_crops WHERE name='%s' ''' % (myfoodtype)    
		
        recordset = self.executeResultsQuery(query)

	numrows = 0		
	if myfoodtype!= '' and mycategory!='':
                if len(recordset) == 0:
                    query = '''INSERT INTO setup_foods_crops(name, category,energyvalueperunit, unitofmeasure) 
                     	    VALUES('%s','%s',%s,'%s')''' % (myfoodtype,mycategory, myenergyvalue, mymeasuringunit)
                    self.executeUpdateQuery(query)
                    self.txtFoodType.clear()
                    self.cmbCategory.setCurrentIndex(-1)
                    self.cmbUnitOfMeasure.setCurrentIndex(-1)
                    self.txtKCalories.clear()
                
                else:
                    QMessageBox.information(self,"Add Food/Crop Type","Food/Crop type already exists")
        else:
            QMessageBox.information(self,"Add Food/Crop Type","Name or Category should not be blank")

        
