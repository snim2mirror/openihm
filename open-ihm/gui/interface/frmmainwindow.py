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
from frmhousehold_delete import FrmDelHousehold
from frmhousehold_data import FrmHouseholdData
from frmhouseholds import FrmHouseholds
from frmmanagefoodtypes import FrmManageFoodTypes
from frmhousehold_add import FrmAddHousehold
from frmhousecharacteristics import FrmHouseCharacteristics
from frmpersonalcharacteristics import FrmPersonalCharacteristics
#from frmexpendituretypes import FrmExpenditureTypes
from frmmanageassets import FrmManageAssetDetails
from frmincomesourcedetails import FrmIncomeSourceDetails
from frmfindproject import FrmFindProject
from frmfindhousehold import FrmFindHousehold
from frmfindhouseholdresults import FrmFindHouseholdResults
from frmproject_open import FrmOpenProject
from frm_about_openihm import FrmAboutOpenIHM
from frmfoodenergy_requirements import  FrmFoodEnergyRequirements
from frm_report_householdsbycharacteristics import RepHouseholdsByCharacteristics

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
		self.connect(self.actionCreate_Project, QtCore.SIGNAL("triggered()"), self.newProject)
		self.connect(self.actionAsset_Details, QtCore.SIGNAL("triggered()"), self.manageAssetDetails)
		self.connect(self.actionIncome_Source_Details, QtCore.SIGNAL("triggered()"), self.manageIncomeDetails)
		self.connect(self.actionExpenditure_Types, QtCore.SIGNAL("triggered()"), self.manageBaseExpenditureDetails)		
		self.connect(self.actionEdit_Project, QtCore.SIGNAL("triggered()"), self.editProject)
		self.connect(self.actionConfigure_Project, QtCore.SIGNAL("triggered()"), self.configureProject)
		self.connect(self.actionEdit_Household, QtCore.SIGNAL("triggered()"), self.editProjectHousehold)
		self.connect(self.actionEnter_Household_Data, QtCore.SIGNAL("triggered()"), self.viewHouseholdData)
		self.connect(self.actionFind_Household, QtCore.SIGNAL("triggered()"), self.findHousehold)
		self.connect(self.actionView_All_Households_2, QtCore.SIGNAL("triggered()"), self.viewAllHouseholds)
		self.connect(self.actionFind_Project, QtCore.SIGNAL("triggered()"), self.findProject)
		self.connect(self.actionOpen_Project, QtCore.SIGNAL("triggered()"), self.openProject)
		self.connect(self.actionClose_Project, QtCore.SIGNAL("triggered()"), self.closeProject)
		
		self.connect(self.actionFood_Types, QtCore.SIGNAL("triggered()"), self.manageFoodTypes)
		self.connect(self.actionAdd_Household, QtCore.SIGNAL("triggered()"), self.addHousehold)
		self.connect(self.actionDelete_Household, QtCore.SIGNAL("triggered()"), self.delHousehold)
		self.connect(self.actionHousehold_Characteristics_2, QtCore.SIGNAL("triggered()"), self.manageHouseholdCharacteristics)
		self.connect(self.actionPersonal_Characteristics, QtCore.SIGNAL("triggered()"), self.managePersonalCharacteristics)
		
		self.actionOpen_Project.setIcon(QtGui.QIcon('resources/images/projectOpen.png'))
		self.actionCreate_Project.setIcon(QtGui.QIcon('resources/images/projectNew.png'))
		self.actionFind_Project.setIcon(QtGui.QIcon('resources/images/projectFind.png'))
		self.actionClose_Project.setIcon(QtGui.QIcon('resources/images/projectClose.png'))
		self.toolbar = self.addToolBar('Open')
		self.toolbar.addAction(self.actionCreate_Project)
		self.toolbar.addAction(self.actionOpen_Project)
		self.toolbar.addAction(self.actionFind_Project)
		self.toolbar.addAction(self.actionClose_Project)
		self.actionClose_Project.setDisabled(True)
		self.setWindowIcon(QtGui.QIcon('resources/images/openihm.png'))

		self.connect(self.actionAboutOpenIHM, QtCore.SIGNAL("triggered()"), self.aboutOpenIHM)
		self.connect(self.actionEnergy_Requirements, QtCore.SIGNAL("triggered()"), self.viewFoodEnergyRequirements)

		#signals and slots for repoerts
		self.connect(self.actionHousehold_by_Characteristics, QtCore.SIGNAL("triggered()"), self.reportHouholdsByCharacteristics)
	
	
	def centerSubWindow(self, subWin):
	    ''' Moves a subwindow to the center of the Mdi Area'''
	    screen = self.mdi.geometry()
	    size =  subWin.geometry()
	    subWin.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	    
	def newProject(self):
		''' Creates and Shows the New Project form '''
		if ( self.projectid != -1 ):
			msg = "Creating a new project will close the current project. Are you sure you want to create a new project?"
			ret = QtGui.QMessageBox.question(self,"Confirm Project Creation", msg, QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
			if ( ret == QtGui.QMessageBox.No ):
				return
		self.mdi.closeAllSubWindows()
		form = FrmNewProject(self)
		subWin = self.mdi.addSubWindow(form)
		self.centerSubWindow(subWin)
		form.show()
	    
	def openProject(self):
		''' Creates and Shows the Open Project form '''
		if ( self.projectid != -1 ):
			msg = "Opening another project will close the current project. Are you sure you want to open another project?"
			ret = QtGui.QMessageBox.question(self,"Confirm Opening", msg, QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
			# if opening is rejected return
			if ( ret == QtGui.QMessageBox.No ):
				return
		self.mdi.closeAllSubWindows()
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
	    self.actionClose_Project.setDisabled(True)
	    
	def editProject(self):
	    ''' Creates and Shows the Edit Project form '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
	        form = FrmEditProject(self)
	        subWin = self.mdi.addSubWindow(form)
	        self.centerSubWindow(subWin)
	        form.show()
	    
	def configureProject(self):
	    ''' Creates and Shows the Configure Project form '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
	        form = FrmConfigureProject(self)
	        subWin = self.mdi.addSubWindow(form)
	        self.centerSubWindow(subWin)
	        form.show()
	    
	def addHousehold(self):
	    ''' Creates and Shows the Add House Hold form '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
	        form = FrmAddHousehold(self)
	        subWin = self.mdi.addSubWindow(form)
	        self.centerSubWindow(subWin)
	        form.show()
	    
	def editProjectHousehold(self):
	    ''' Creates and Shows the Edit Household GetID form '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
		    form = FrmEditHouseholdGetID(self)
		    subWin = self.mdi.addSubWindow(form)
		    self.centerSubWindow(subWin)
		    form.show()
	
	def delHousehold(self):
	    ''' Creates and Shows the Delete House Hold form '''
	    if self.projectid == -1:
			msg = "No project is active. First open a project under which the household to be deleted belongs."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
	        form = FrmDelHousehold(self)
	        form.exec_()
	    
	def viewHouseholdData(self):
	    ''' shows household data (expenditure, income, assets, etc) '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
		    form = FrmHouseholdData(self)
		    subWin = self.mdi.addSubWindow(form)
		    self.centerSubWindow(subWin)
		    form.show()
	    
	def findHousehold(self):
	    ''' Creates and Shows the Find Household form '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
	        form = FrmFindHousehold(self)
	        subWin = self.mdi.addSubWindow(form)
	        self.centerSubWindow(subWin)
	        form.show()
	    
	def viewAllHouseholds(self):
	    ''' shows all households '''
	    if self.projectid == -1:
			msg = "No project is active. First create a new project or open an existing project."
			QtGui.QMessageBox.information(self,"Notice",msg)
	    else:
		    form = FrmFindHouseholdResults(self)
		    subWin = self.mdi.addSubWindow(form)
		    self.centerSubWindow(subWin)
		    form.show()
	
	def manageFoodTypes(self):
	    ''' Creates and Shows the Manage Crop Types form'''
	    self.form = QtGui.QDialog()
	    self.ui = FrmManageFoodTypes()
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

	def manageBaseExpenditureDetails(self):
	    ''' Creates and Shows the Manage Expenditure Details form '''
	    form = FrmExpenditureTypes(self.mdi)
	    subWin = self.mdi.addSubWindow(form)
	    self.centerSubWindow(subWin)
	    form.show()

	def findProject(self):
	    ''' Creates and Shows the Find Project form '''
	    form = FrmFindProject(self)
	    subWin = self.mdi.addSubWindow(form)
	    self.centerSubWindow(subWin)
	    form.show()

	    
        def aboutOpenIHM(self):
	    ''' Creates and Shows the About OpenIHM form '''
	    form = FrmAboutOpenIHM(self.mdi)
	    subWin = self.mdi.addSubWindow(form)
	    self.centerSubWindow(subWin)
	    form.show()
	    

        def viewFoodEnergyRequirements(self):
	    ''' Creates and Shows the View Food Energy Requirements form '''
	    form = FrmFoodEnergyRequirements(self.mdi)
	    subWin = self.mdi.addSubWindow(form)
	    self.centerSubWindow(subWin)
	    form.show()

        def reportHouholdsByCharacteristics(self):
	    ''' Creates and Shows the View Food Energy Requirements form '''
	    form = RepHouseholdsByCharacteristics(self.mdi)
	    subWin = self.mdi.addSubWindow(form)
	    self.centerSubWindow(subWin)
	    form.show()
