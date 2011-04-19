#	Filename: frm_managefoodtypes_add.py
#
#	Class to create the Add Food Energy Requirement form - FrmAddFoodEnergyRequirement.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.foodenergyrequirement import FoodEnergyRequirement
from data.database import Database
from gui.designs.ui_managefoodtypes_add import Ui_AddFoodTypes

class FrmAddFoodCropType(QDialog, Ui_AddFoodTypes):	
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
 
    def mdiClose(self):
        self.close()

        
    def saveDetails(self):
        ''' Saves newly created food/crop energy requirement data to database '''

        # get the data entered by user
        myfoodtype = self.txtFoodType.text()
        mycategory = self.cmbCategory.currentText()
	mymeasuringunit = self.cmbUnitOfMeasure.currentText()
        myenergyvalue  = self.txtKCalories.text()
        print mycategory
        	
	# check if record exists
	query = '''SELECT name, energyvalueperunit, unitofmeasure
			FROM setup_foods_crops WHERE name='%s' ''' % (myfoodtype)    
		
	database = Database()
	database.open()
        recordset = database.execSelectQuery(query)

	numrows = 0		
	if myfoodtype!= '' and mycategory!='':
                if len(recordset) == 0:
                    query = '''INSERT INTO setup_foods_crops(name, category,energyvalueperunit, unitofmeasure) 
                     	    VALUES('%s','%s',%s,'%s')''' % (myfoodtype,mycategory, myenergyvalue, mymeasuringunit)
                    database.execUpdateQuery(query)
                    self.txtFoodType.clear()
                    self.cmbCategory.setCurrentIndex(-1)
                    self.cmbUnitOfMeasure.setCurrentIndex(-1)
                    self.txtKCalories.clear()
                
                else:
                    QMessageBox.information(self,"Add Food/Crop Type","Food/Crop type already exists")
        else:
            QMessageBox.information(self,"Add Food/Crop Type","Name or Category should not be blank")
		
        database.close()
        
