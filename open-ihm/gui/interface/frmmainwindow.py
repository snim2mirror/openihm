#-----------------------------------------------------------------------------------	
#	Filename: frmmainwindow.py
#
#	Inherits from Ui_MainWindow in gui.designs.ui_mainwindow module
#	to create a class FrmMainWindow which creates the main window
#	of the application.
#-----------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the main window design class
from gui.designs.ui_mainwindow import Ui_MainWindow

# import subwindows
from frmnewproject import FrmNewProject
from frmmanagefoodtypes import FrmManageFoodTypes
from frmhousehold_add import FrmAddHousehold

class FrmMainWindow(Ui_MainWindow):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_mainwindow module '''
    
    def __init__(self, parent=None):
        ''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
        self.mdi = QtGui.QMdiArea()
    
    def centerSubWindow(self, subWin):
        ''' Moves a subwindow to the center of the Mdi Area'''
        screen = self.mdi.geometry()
        size =  subWin.geometry()
        subWin.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    def newProject(self):
        ''' Creates and Shows the New Project form '''
        self.form = QtGui.QDialog()
        self.ui = FrmNewProject()
        self.ui.setupUi(self.form, self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()
        
    def addHousehold(self):
        ''' Creates and Shows the Add House Hold form '''
        self.form = QtGui.QDialog()
        self.ui = FrmAddHousehold()
        self.ui.setupUi(self.form, self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageFoodTypes(self):
        ''' Creates and Shows the Manage Food Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageFoodTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()
        
    def setupUi(self, MainWindow):
        ''' Sets up the main window adding signal and slot connections where necessary. '''
        Ui_MainWindow.setupUi(self, MainWindow) 		
        MainWindow.setCentralWidget(self.mdi)

        # connect relevant signals and slots
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionNew_Project, QtCore.SIGNAL("triggered()"), self.newProject)
        QtCore.QObject.connect(self.actionFood_Types, QtCore.SIGNAL("triggered()"), self.manageFoodTypes)
        QtCore.QObject.connect(self.actionAdd_Household, QtCore.SIGNAL("triggered()"), self.addHousehold)
