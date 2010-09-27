#	Filename: frm_currencymanager.py
#
#	Form for adding and deleting currencies
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Currency Manager design class
from gui.designs.ui_currencymanager import Ui_CurrencyManager

class FrmCurrencyManager(QDialog, Ui_CurrencyManager):	
     ''' Creates the Currency Manager from. '''	

     def __init__(self, parent):
         ''' Set up the dialog box interface '''
         self.parent = parent
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent = parent
         self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
