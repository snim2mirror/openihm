#-------------------------------------------------------------------	
#	Filename: frmhousehold_data.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from gui.designs.ui_households_all import Ui_AllHouseholds

class FrmHouseholds(QtGui.QDialog, Ui_AllHouseholds):	
    ''' Creates the household data (income, assets, expenditure, etc) form '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # connect relevant signals and slots
        self.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
