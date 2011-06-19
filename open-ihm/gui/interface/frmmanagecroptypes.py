#-----------------------------------------------------------------------------------------------    
#    Filename: frmmanagecroptypes.py
#
#    Class to create the form for adding, editing, or deleting Crop Types - FrmManageCropTypes.
#------------------------------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
from gui.designs.ui_managecroptypes import Ui_CropTypes

from mixins import MDIDialogMixin

class FrmManageCropTypes(Ui_CropTypes, MDIDialogMixin):
    
    def setupUi(self,Form,Mdi):
        Ui_CropTypes.setupUi(self,Form)
        self.form = Form
        self.parent = Mdi
        
#        QtCore.QObject.connect(self.btnManageCropsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
