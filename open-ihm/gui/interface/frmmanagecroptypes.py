#-----------------------------------------------------------------------------------------------    
#    Filename: frmmanagecroptypes.py
#
#    Class to create the form for adding, editing, or deleting Crop Types - FrmManageCropTypes.
#------------------------------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
from gui.designs.ui_managecroptypes import Ui_CropTypes

class FrmManageCropTypes(Ui_CropTypes):
    
    def setupUi(self,Form,Mdi):
        Ui_CropTypes.setupUi(self,Form)
        self.form = Form
        self.parent = Mdi
        
#        QtCore.QObject.connect(self.btnManageCropsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)

    def mdiClose(self):
        self.parent.mdi.closeActiveSubWindow()

