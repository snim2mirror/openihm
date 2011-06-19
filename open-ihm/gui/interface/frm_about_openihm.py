#	Filename: frm_about_openihm.py
#
#	Display Information about Open-IHM under the help menu.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the About OpenIHM design class
from gui.designs.ui_about_openihm import Ui_AboutOpenIHM
from mixins import MDIDialogMixin

class FrmAboutOpenIHM(QDialog, Ui_AboutOpenIHM, MDIDialogMixin):
	''' Creates the About Open-IHM from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
