#------------------------------------------------------------------------------------------------	
#	Filename: frmhousehold_add.py
#
#	Class to create the Add Household form - FrmAddHousehold.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_addhousehold import Ui_AddHousehold

class FrmAddHousehold(Ui_AddHousehold):	
    ''' Creates the Create (New) Project from. Uses the design class
    in gui.designs.ui_addhousehold. '''	

    def setupUi(self, Form, Mdi):
        ''' Set up the dialog box interface '''
        Ui_AddHousehold.setupUi(self, Form)
        
        # connect relevant signals and slots
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
