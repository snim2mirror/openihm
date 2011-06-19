#------------------------------------------------------------------------------------------------	
#	Filename: frmfoodenergyrequirement_edit.py
#
#	Class to create the Add Food Energy Requirement form - FrmAddFoodEnergyRequirement.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.foodenergyrequirement import FoodEnergyRequirement

# import the Create Add Food Energy Requirement Dialog design class
from gui.designs.ui_edit_foodenergyrequirement import Ui_EditFoodEnergyRequirement

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
