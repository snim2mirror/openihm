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

class FrmAddCropType(QDialog, Ui_AddFoodTypes):	
    ''' Creates the add food energy requirement form '''	

    def __init__(self,parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent

        #set input validator and restrict input to numeric values,
        myIntVal = QIntValidator(0, 10000, self.txtKCalories)
        self.txtKCalories.setValidator(myIntVal);
        
 
        # connect relevant signals and slots   
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveDetails)
        
    def saveDetails(self):
        ''' Saves newly created food energy requirement data to database '''

        # get the data entered by user
        myfoodtype = self.txtFoodType.text()
	mymeasuringunit = self.cmbUnitOfMeasure.currentText()
        myenergyvalue  = self.txtKCalories.text()
        	
	# check if record exists
	query = '''SELECT foodtype, energyvalueperunit, measuringunit
			FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
	database = Database()
	database.open()
        recordset = database.execSelectQuery(query)

	numrows = 0		
	if myfoodtype!= '':
                if len(recordset) == 0:
                    query = '''INSERT INTO setup_crops(foodtype, energyvalueperunit, measuringunit) 
                     	    VALUES('%s',%s,'%s')''' % (myfoodtype, myenergyvalue, mymeasuringunit)
                    database.execUpdateQuery(query)
                    self.txtFoodType.clear()
                    self.cmbUnitOfMeasure.setCurrentIndex(-1)
                    self.txtKCalories.clear()
                
                else:
                    QMessageBox.information(self,"Add Food Type","Food type already exists")
        else:
            QMessageBox.information(self,"Add Food Type","Name should not be blank")
		
        database.close()
        
