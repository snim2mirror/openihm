#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_getid.py
#
#	form that gets the ID of a household to be editted.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import forms required to edit household
from gui.designs.ui_edithousehold_getid import Ui_EditHouseholdGetID
from frmhousehold_edit_details import FrmEditHouseholdDetails

class FrmEditHouseholdGetID(QtGui.QDialog, Ui_EditHouseholdGetID):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdOk, QtCore.SIGNAL("clicked()"), self.showDetails)
    
    def showDetails(self):
        ''' Show Household Details '''
        form = FrmEditHouseholdDetails(self.parent.mdi)
        subWin = self.parent.mdi.addSubWindow(form)
        self.parent.centerSubWindow(subWin)
        # close this form
        self.parent.mdi.closeActiveSubWindow()
        # show the details form
        form.show()
