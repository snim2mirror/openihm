#-------------------------------------------------------------------    
#    Filename: frmmainwindow.py
#
#    Inherits from Ui_MainWindow in gui.designs.ui_mainwindow module
#    to create a class FrmMainWindow which creates the main window
#    of the application.
#-------------------------------------------------------------------

# pylint: disable=W0312
# pylint: disable=W0511

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
#from frmmanagefoodtypes import FrmManageFoodTypes
from frmmanage_foods_crops import FrmManageTypes

from frmhousehold_add import FrmAddHousehold
from frmhousecharacteristics import FrmHouseCharacteristics
from frmpersonalcharacteristics import FrmPersonalCharacteristics
from frmexpendituretypes import FrmExpenditureTypes
from frmmanageassets import FrmManageAssetDetails
from frmincomesourcedetails import FrmIncomeSourceDetails
from frmfindproject import FrmFindProject
from frmfindhousehold import FrmFindHousehold
from frmfindhouseholdresults import FrmFindHouseholdResults
from frmproject_open import FrmOpenProject
from frm_about_openihm import FrmAboutOpenIHM
from frmfoodenergy_requirements import  FrmFoodEnergyRequirements
from frm_report_householdsbycharacteristics import RepHouseholdsByCharacteristics
from frmcurrencymanager import FrmCurrencyManager
from frm_report_householdincome import HouseholdIncomeReport
from frmstandardoflivingmanager import FrmStandardOfLivingManager
from data.setup_crops_startupvalues import FoodValuesStartup
from outputs.routines.generate_data_entry_sheet import DataEntrySheets
from inputs.read_data_entry_sheets import ReadDataEntrySheets
from frm_report_disposableincome import HouseholdDisposableIncome
from data.setup_foodrequirement_startupvalues import FoodRequirementValues
#from frm_report_livingthreshold import LivingThreshold



class FrmMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_mainwindow module '''
    
    def __init__(self, parent=None):
        ''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
        QtGui.QMainWindow.__init__(self)
	self.setupUi(self)

#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)

        self.projectid = -1
        self.projectname = ""

        self.mdi = QtGui.QMdiArea()
        self.setCentralWidget(self.mdi)

        self.actionClose_Project.setDisabled(True)

	### FIXME: Replace absolute paths to images with Qt resources
        self.setWindowIcon(QtGui.QIcon('resources/images/openihm.png'))

        ### FIXME: Should do this in Qt4Deisgner
        self.actionOpen_Project.setIcon(QtGui.QIcon('resources/images/projectOpen.png'))
        self.actionCreate_Project.setIcon(QtGui.QIcon('resources/images/projectNew.png'))
        self.actionFind_Project.setIcon(QtGui.QIcon('resources/images/projectFind.png'))
        self.actionClose_Project.setIcon(QtGui.QIcon('resources/images/projectClose.png'))

        ### FIXME: This is intended to style the MDI area, but it doesn't work!

	### ATTEMPT 1: Style sheets.
	#        self.mdi.setStyleSheet("#centralwidget { background : white; background-image : url(:/images/images/EfDChancoComposite.jpg); background-repeat : no-repeat; }")

	### ATTEMPT 2: Brushes.
        ### Advice from the PyQt mailing list
        ### Results in image being tiled.
#        self.brush = QtGui.QBrush(QtGui.QPixmap("resources/images/EfDChancoCompositeIcon.jpg"))
#        self.mdi.setBackground(self.brush)        

	### ATTEMPT 3: Toolbar hack.
        ### Add a spacer and icon to the toolbar with the logo.
        ### FIXME: decide whether this should be done as a background image.
        # self.actionDo_Nothing = QtGui.QAction(self)
        # self.connect(self.actionDo_Nothing, QtCore.SIGNAL("triggered()"), self.doNothing)
        # self.actionDo_Nothing.setIcon(QtGui.QIcon("resources/images/EfDChancoCompositeIcon.jpg"))
        # self.toolbar.addAction(self.actionDo_Nothing)

        
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
	print "flibble"
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
        #form = FrmManageFoodTypes(self.mdi)
        form = FrmManageTypes(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def manageHouseholdCharacteristics(self):
        ''' Creates and Shows the Household Characteristics form'''
        form = FrmHouseCharacteristics(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
       
    def managePersonalCharacteristics(self):
        ''' Creates and Shows the Personal Characteristics form'''
        form = FrmPersonalCharacteristics(self.mdi)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()
    
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

    def manageCurrencies(self):
        ''' open the Currency Manager '''
        form = FrmCurrencyManager(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def manageStandardOfLiving(self):
        ''' open the Standard Of Living Manager '''
        form = FrmStandardOfLivingManager(self)
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
        form = FrmFoodEnergyRequirements(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def reportHouseholdsByCharacteristics(self):
        ''' Creates and Shows the View Food Energy Requirements form '''
        form = RepHouseholdsByCharacteristics(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def reportHouseholdsByIncomeSource(self):
        ''' Creates and Shows the Report: Households by Income Source form '''
        form = HouseholdIncomeReport(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def initialiseFoodEnergyLookupTable(self):
        '''Create Initial Kcal values for certain crops/foods'''
        initialiser = FoodValuesStartup()
        initialiser.insertSartUpValues()
                
                
    def createDataEntrySheets(self):
        ''' Creates Spreadsheets for data entry'''
        if self.projectid == -1:
            msg = "No project is active. First create a new project or open an existing project."
            QtGui.QMessageBox.information(self,"Notice",msg)
        else:
            datasheet = DataEntrySheets(self.projectid)
            datasheet.writeDataSheets()

    def importData(self):
        ''' Import data from Spreadsheets'''
        if self.projectid == -1:
            msg = "No project is active. First create a new project or open an existing project."
            QtGui.QMessageBox.information(self,"Notice",msg)
        else:
            datasheet = ReadDataEntrySheets(self.projectid)
            datasheet.readdata()
                
    def reportHouseholdDisposableIncome(self,reporttype):
        ''' Creates and Shows the Report: Household Disposable Income form '''
        form = HouseholdDisposableIncome(self,reporttype)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def initialiseFoodRequirementTable(self):
        '''Create Initial Kcal values for certain crops/foods'''
        initialiser = FoodRequirementValues()
        initialiser.insertSartUpValues()
             
    def setReporttypeAsLivingThreshold(self):
        '''set report type for Living Threshold report'''
        reporttype = 'LivingThreshold'
        self.reportHouseholdDisposableIncome(reporttype)
                
    def setReporttypeDI(self):
        '''set report type for Household Disposable Income report'''
        reporttype = 'DI'
        self.reportHouseholdDisposableIncome(reporttype)
                
    # def reportLivingThreshold(self):
    #     form = LivingThreshold(self)
    #     subWin = self.mdi.addSubWindow(form)
    #     self.centerSubWindow(subWin)
    #     form.show()

    # def doNothing(self):
    #     """Do nothing -- for the logo on the toolbar.
    #     """
    #     return

