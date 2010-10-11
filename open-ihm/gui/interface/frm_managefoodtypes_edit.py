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

    def __init__(self, parent, selectedcrop, measuringunit, energyvalue):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.croptype = selectedcrop
        self.measuringunit = measuringunit
        self.energyvalue = energyvalue
        
        #set input validator and restrict input to numeric values,
        myIntVal = QIntValidator(0, 10000, self.txtKCalories)
        self.txtKCalories.setValidator(myIntVal)

        self.showDetailsToEdit()
        # connect relevant signals and slots   
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveDetails)

    def showDetailsToEdit(self):
        ''' Display energy requirements data '''
        self.txtFoodType.setText(self.croptype)
        self.txtMeasuringUnit.setText(self.measuringunit)
        self.txtKCalories.setText(self.energyvalue)

    def saveDetails(self):
        ''' Saves newly created food energy requirement data to database '''

        # get the data entered by user
        myfoodtype = self.txtFoodType.text()
	mymeasuringunit = self.txtMeasuringUnit.text()
        myenergyvalue  = self.txtKCalories.text()
        database = Database()
	if myfoodtype!= '':
            
            query = '''UPDATE setup_crops SET foodtype='%s', energyvalueperunit=%s, measuringunit='%s'
                     	    WHERE foodtype='%s' ''' % (myfoodtype, myenergyvalue, mymeasuringunit, myfoodtype)
                    
            database.open()
            database.execUpdateQuery(query)
            database.close()
            self.txtFoodType.clear()
            self.txtMeasuringUnit.clear()
            self.txtKCalories.clear()

        else:
            QMessageBox.information(self,"Edit Food Type","Name should not be blank")

		
        
        
