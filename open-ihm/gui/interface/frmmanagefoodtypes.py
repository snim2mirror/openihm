from PyQt4 import QtGui, QtCore
from gui.designs.ui_managefoodtypes import Ui_foodTypes

class FrmManageFoodTypes(Ui_foodTypes):		
    def setupUi(self,Form,Mdi):
        Ui_foodTypes.setupUi(self,Form)
        QtCore.QObject.connect(self.btnManageFoodCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
