#-------------------------------------------------------------------	
#	Filename: frmfoodenergy_requirements.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_foodenergy_requirements import Ui_FrmFoodEnergyRequirements
#from frmhouseholds_add import FrmAddHousehold
#from frmhouseholds_edit import FrmEditHousehold
#from frmhousehold_data import FrmHouseholdData

class FrmFoodEnergyRequirements(QDialog, Ui_FrmFoodEnergyRequirements):	
	''' Creates the view food energy requirements form '''	
	def __init__(self, parent):
	    ''' Set up the dialog box interface '''
	    self.parent = parent
	    QDialog.__init__(self)
	    self.setupUi(self)
	    self.parent = parent
	    self.config = Config.dbinfo().copy()
	    
	    # get food energy requirement details by sex and age
	    #self.getFoodEnergyRequirements()
	    
	    # connect relevant signals and slots
	    self.connect(self.cmdFERequirementsClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
	
