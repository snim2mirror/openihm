#	Filename: frm_managefoodtypes_edit.py
#
#	Class to create the Edit Food Type form - 
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.foodenergyrequirement import FoodEnergyRequirement
from data.database import Database
from gui.designs.ui_managefoodtypes_edit import Ui_EditFoodTypes

class FrmEditCropType(QDialog, Ui_EditFoodTypes):
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
        database = Database()
	if mytype!= '' and mycategory!='':
            
            query = '''UPDATE setup_foods_crops SET name='%s', category='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     	    WHERE name='%s' ''' % (mytype, mycategory, myenergyvalue, mymeasuringunit, mytype)
                    
            database.open()
            database.execUpdateQuery(query)
            database.close()
            self.txtFoodType.clear()
            self.txtMeasuringUnit.clear()
            self.txtKCalories.clear()

        else:
            QMessageBox.information(self,"Edit Food Type","Name or Category should not be blank")

		
        
        
