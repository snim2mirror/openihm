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
from frmhousehold_edit_getid import FrmEditHouseholdGetID
from frmhousehold_data import FrmHouseholdData
from frmhouseholds import FrmHouseholds
from frmmanagefoodtypes import FrmManageFoodTypes
from frmhousehold_add import FrmAddHousehold
from frmhousecharacteristics import FrmHouseCharacteristics
from frmpersonalcharacteristics import FrmPersonalCharacteristics
from frmexpendituretypes import FrmExpenditureTypes
from frmmanageassets import FrmManageAssetDetails
from frmincomesourcedetails import FrmIncomeSourceDetails
from frmfindproject import FrmFindProject
from frmproject_open import FrmOpenProject

class FrmMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_mainwindow module '''

    def __init__(self, parent=None):
        ''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.projectid = -1
        self.projectname = ""
        
        self.mdi = QtGui.QMdiArea()
        self.setCentralWidget(self.mdi)

        # connect relevant signals and slots
        self.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.actionNew_Project, QtCore.SIGNAL("triggered()"), self.newProject)
        self.connect(self.actionAsset_Details, QtCore.SIGNAL("triggered()"), self.manageAssetDetails)
        self.connect(self.actionIncome_Source_Details, QtCore.SIGNAL("triggered()"), self.manageIncomeDetails)
        self.connect(self.actionEdit_Project, QtCore.SIGNAL("triggered()"), self.editProject)
        self.connect(self.actionConfigure_Project, QtCore.SIGNAL("triggered()"), self.configureProject)
        self.connect(self.actionOpen_Household, QtCore.SIGNAL("triggered()"), self.editProjectHousehold)
        self.connect(self.actionHousehold_Data, QtCore.SIGNAL("triggered()"), self.viewHouseholdData)
        self.connect(self.actionView_All_Households, QtCore.SIGNAL("triggered()"), self.viewAllHouseholds)
        self.connect(self.actionFind_Project, QtCore.SIGNAL("triggered()"), self.findProject)
        self.connect(self.actionOpen_Project, QtCore.SIGNAL("triggered()"), self.openProject)
        self.connect(self.actionClose_Project, QtCore.SIGNAL("triggered()"), self.closeProject)

        self.connect(self.actionCrop_Types, QtCore.SIGNAL("triggered()"), self.manageCropTypes)
        self.connect(self.actionAdd_Household, QtCore.SIGNAL("triggered()"), self.addHousehold)
        self.connect(self.actionHousehold_Characteristics_2, QtCore.SIGNAL("triggered()"), self.manageHouseholdCharacteristics)
        self.connect(self.actionPersonal_Characteristics, QtCore.SIGNAL("triggered()"), self.managePersonalCharacteristics)


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
        
    def openProject(self):
        ''' Creates and Shows the Open Project form '''
        form = FrmOpenProject(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def closeProject(self):
        ''' Creates and Shows the Open Project form '''
        # close all open project sub windows
        self.mdi.closeAllSubWindows()
        # change the main window title bar caption
        self.setWindowTitle("Open IHM")
        # indicate that no project is active
        self.projectid = -1
        self.projectname = ""
        
    def editProject(self):
        ''' Creates and Shows the Edit Project form '''
        if self.projectid == -1:
            QtGui.QMessageBox.information(self,"Notice","No project is active. First create a new project or open an existing project.")
        else:
            form = FrmEditProject(self)
            subWin = self.mdi.addSubWindow(form)
            self.centerSubWindow(subWin)
            form.show()
        
    def configureProject(self):
        ''' Creates and Shows the Configure Project form '''
        form = FrmConfigureProject(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def addHousehold(self):
        ''' Creates and Shows the Add House Hold form '''
        form = FrmAddHousehold(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def editProjectHousehold(self):
        ''' Creates and Shows the Edit Household GetID form '''
        form = FrmEditHouseholdGetID(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def viewHouseholdData(self):
        ''' shows household data (expenditure, income, assets, etc) '''
        form = FrmHouseholdData(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
        
    def viewAllHouseholds(self):
        ''' shows all households '''
        form = FrmHouseholds(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

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

    def findProject(self):
        ''' Creates and Shows the Find Project form '''
        form = FrmFindProject(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
