#-------------------------------------------------------------------    
#    Filename: frmmanageemployment.py
#
#    Class to create the Manage Employment Details form - FrmManageEmployment.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Manage Employment design class
from gui.designs.ui_manageemployment import Ui_ManageEmployment

class FrmManageEmployment(Ui_ManageEmployment):    
    ''' Creates the Manage Employment Details form. Uses the design class
        in gui.designs.ui_manageemploymant. '''    
    def setupUi(self, Form, Mdi):
        ''' Set up the dialog box interface '''
        Ui_ManageEmployment.setupUi(self, Form)
        self.parent = Mdi
        # connect relevant signals and slots
        QtCore.QObject.connect(self.btnManageEmploymentClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
    def mdiClose(self):
        self.parent.mdi.closeActiveSubWindow()
