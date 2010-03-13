#------------------------------------------------------------------------------------------------	
#	Filename: frmhousehold_add.py
#
#	Class to create the Add Household form - FrmAddHousehold.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_addhousehold import Ui_AddHousehold

class FrmAddHousehold(QtGui.QDialog, Ui_AddHousehold):	
    ''' Creates the Create (New) Project from. Uses the design class
    in gui.designs.ui_addhousehold. '''	

    def __init__(self, Mdi):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
