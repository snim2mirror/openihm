#-------------------------------------------------------------------	
#	Filename: frmmainwindow.py
#
#	Inherits from Ui_MainWindow in gui.designs.ui_mainwindow module
#	to create a class FrmMainWindow which creates the main window
#	of the application.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the main window design class
from gui.designs.ui_mainwindow import Ui_MainWindow

# import subwindows
from frmnewproject import FrmNewProject
from frmmanagecroptypes import FrmManageCropTypes
from frmproject_edit import FrmEditProject
from frmproject_configure import FrmConfigureProject
from frmmanagefoodtypes import FrmManageFoodTypes
from frmhousehold_add import FrmAddHousehold
from frmhousecharacteristics import FrmHouseCharacteristics
from frmpersonalcharacteristics import FrmPersonalCharacteristics
from frmexpendituretypes import FrmExpenditureTypes
from frmmanageassets import FrmManageAssetDetails
from frmincomesourcedetails import FrmIncomeSourceDetails

class FrmMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_mainwindow module '''

    def __init__(self, parent=None):
        ''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.mdi = QtGui.QMdiArea()
        self.setCentralWidget(self.mdi)

        # connect relevant signals and slots
        self.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.actionNew_Project, QtCore.SIGNAL("triggered()"), self.newProject)
	self.connect(self.actionAsset_Details, QtCore.SIGNAL("triggered()"), self.manageAssetDetails)
	self.connect(self.actionIncome_Source_Details, QtCore.SIGNAL("triggered()"), self.manageIncomeDetails)
        self.connect(self.actionNew_Project, QtCore.SIGNAL("triggered()"), self.newProject)
        self.connect(self.actionEdit_Project, QtCore.SIGNAL("triggered()"), self.editProject)
        self.connect(self.actionConfigure_Project, QtCore.SIGNAL("triggered()"), self.configureProject)


        QtCore.QObject.connect(self.actionCrop_Types, QtCore.SIGNAL("triggered()"), self.manageCropTypes)
        QtCore.QObject.connect(self.actionAdd_Household, QtCore.SIGNAL("triggered()"), self.addHousehold)
        QtCore.QObject.connect(self.actionHousehold_Characteristics_2, QtCore.SIGNAL("triggered()"), self.manageHouseholdCharacteristics)
        QtCore.QObject.connect(self.actionPersonal_Characteristics, QtCore.SIGNAL("triggered()"), self.managePersonalCharacteristics)


    def centerSubWindow(self, subWin):
        ''' Moves a subwindow to the center of the Mdi Area'''
        screen = self.mdi.geometry()
        size =  subWin.geometry()
        subWin.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    def newProject(self):
        ''' Creates and Shows the New Project form '''
        form = FrmNewProject(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def editProject(self):
        ''' Creates and Shows the Edit Project form '''
        form = FrmEditProject(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def configureProject(self):
        ''' Creates and Shows the Edit Project form '''
        form = FrmConfigureProject(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def addHousehold(self):
        ''' Creates and Shows the Add House Hold form '''
        self.form = QtGui.QDialog()
        self.ui = FrmAddHousehold()
        self.ui.setupUi(self.form, self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageCropTypes(self):
        ''' Creates and Shows the Manage Crop Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageCropTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageHouseholdCharacteristics(self):
        ''' Creates and Shows the Household Characteristics form'''
        self.form = QtGui.QDialog()
        self.ui = FrmHouseCharacteristics()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()
       
    def managePersonalCharacteristics(self):
        ''' Creates and Shows the Personal Characteristics form'''
        self.form = QtGui.QDialog()
        self.ui = FrmPersonalCharacteristics()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageAssetDetails(self):
        ''' Creates and Shows the Manage Asset Details form '''
        form = FrmManageAssetDetails(self.mdi)
        subWin = self.mdi.addSubWindow(form)
       	self.centerSubWindow(subWin)
        form.show()

    def manageIncomeDetails(self):
        ''' Creates and Shows the Manage Income Details form '''
        form = FrmIncomeSourceDetails(self.mdi)
        subWin = self.mdi.addSubWindow(form)
       	self.centerSubWindow(subWin)
        form.show()
    
