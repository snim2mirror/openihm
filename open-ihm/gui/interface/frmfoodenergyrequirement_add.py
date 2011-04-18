#------------------------------------------------------------------------------------------------	
#	Filename: frmfoodenergyrequirement_add.py
#
#	Class to create the Add Food Energy Requirement form - FrmAddFoodEnergyRequirement.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.foodenergyrequirement import FoodEnergyRequirement

# import the Create Add Food Energy Requirement Dialog design class
from gui.designs.ui_add_foodenergyrequirement import Ui_AddFoodEnergyRequirement

class FrmAddEnergyRequirement(QDialog, Ui_AddFoodEnergyRequirement):	
    ''' Creates the add food energy requirement form '''	

    def __init__(self,parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent

        #set input validator and restrict input to numeric values,
        myAgeVal = QIntValidator(0, 130, self.txtAge)
        myMEnergyVal = QIntValidator(0, 10000, self.txtEnergyRequirementMales)
        myFEnergyVal = QIntValidator(0, 10000, self.txtEnergyRequirementFemales)
                               
        self.txtAge.setValidator(myAgeVal)
        self.txtEnergyRequirementMales.setValidator(myMEnergyVal)
        self.txtEnergyRequirementFemales.setValidator(myFEnergyVal)
#        
 
        # connect relevant signals and slots   
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveFoodEnergyRequirementDetails)

        
    def reject(self):
	self.parent.closeActiveSubWindow()

        
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
        self.close
