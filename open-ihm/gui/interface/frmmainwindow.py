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
from frmmanagefoodtypes import FrmManageFoodTypes
from frmhousehold_add import FrmAddHousehold
from frmhousecharacteristics import FrmHouseCharacteristics
from frmpersonalcharacteristics import FrmPersonalCharacteristics
from frmassettypes import FrmAssetTypes
from frmincomesourcetypes import FrmIncomeSourcesTypes
from frmexpendituretypes import FrmExpenditureTypes
from frmmanagelandtypes import FrmManageLandTypes
from frmothertradablegoods import FrmOtherTradableGoods
from frmmanageassettrees import FrmManageAssetTrees
from frmmanagewildfoods import FrmManageWildFoods
from frmmanagelivestock import FrmManageLivestock
from frmmanagelivestockproducts import FrmManageLivestockProducts
from frmmanagehuntingfishing import FrmManageHuntingFishing
from frmmanageemployment import FrmManageEmployment

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

        QtCore.QObject.connect(self.actionFood_Types, QtCore.SIGNAL("triggered()"), self.manageFoodTypes)
        QtCore.QObject.connect(self.actionAdd_Household, QtCore.SIGNAL("triggered()"), self.addHousehold)
        QtCore.QObject.connect(self.actionHousehold_Characteristics_2, QtCore.SIGNAL("triggered()"), self.manageHouseholdCharacteristics)
        QtCore.QObject.connect(self.actionPersonal_Characteristics, QtCore.SIGNAL("triggered()"), self.managePersonalCharacteristics)
        QtCore.QObject.connect(self.actionAsset_Types, QtCore.SIGNAL("triggered()"), self.manageAssetTypes)
        QtCore.QObject.connect(self.actionIncome_Types, QtCore.SIGNAL("triggered()"), self.manageIncomeSourceTypes)
        QtCore.QObject.connect(self.actionExpenditure_Types, QtCore.SIGNAL("triggered()"), self.manageExpenditureTypes)
        QtCore.QObject.connect(self.actionLand_Types, QtCore.SIGNAL("triggered()"), self.manageLandTypes)
        QtCore.QObject.connect(self.actionOther_Tradable_Goods, QtCore.SIGNAL("triggered()"), self.manageOtherTradableGoods)
        QtCore.QObject.connect(self.actionTrees, QtCore.SIGNAL("triggered()"), self.manageAssetTrees)
        QtCore.QObject.connect(self.actionWild_Foods, QtCore.SIGNAL("triggered()"), self.manageWildFoods)
        QtCore.QObject.connect(self.actionLivestock, QtCore.SIGNAL("triggered()"), self.manageLivestock)
        QtCore.QObject.connect(self.actionLivestock_Products, QtCore.SIGNAL("triggered()"), self.manageLivestockproducts)
        QtCore.QObject.connect(self.actionHunting_and_Fishing, QtCore.SIGNAL("triggered()"), self.manageHuntingFishing)
        QtCore.QObject.connect(self.actionEmployment, QtCore.SIGNAL("triggered()"), self.manageEmployment)

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

    def manageAssetTypes(self):
        ''' Creates and Shows the Manage Asset Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmAssetTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageIncomeSourceTypes(self):
        ''' Creates and Shows the Manage Income Source Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmIncomeSourcesTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageExpenditureTypes(self):
        ''' Creates and Shows the Manage Expenditure Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmExpenditureTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageLandTypes(self):
        ''' Creates and Shows the Manage Expenditure Types form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageLandTypes()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageOtherTradableGoods(self):
        ''' Creates and Shows the Manage Other Tradable Goods form'''
        self.form = QtGui.QDialog()
        self.ui = FrmOtherTradableGoods()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageAssetTrees(self):
        ''' Creates and Shows the Manage Asset Trees form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageAssetTrees()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageWildFoods(self):
        ''' Creates and Shows the Manage Wild Foods form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageWildFoods()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()
        
    def manageLivestock(self):
        ''' Creates and Shows the Manage Livestock form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageLivestock()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageLivestockproducts(self):
        ''' Creates and Shows the Manage Livestock Products form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageLivestockProducts()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageHuntingFishing(self):
        ''' Creates and Shows the Manage Hunting and Fishing form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageHuntingFishing()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()

    def manageEmployment(self):
        ''' Creates and Shows the Manage Employment Details form'''
        self.form = QtGui.QDialog()
        self.ui = FrmManageEmployment()
        self.ui.setupUi(self.form,self.mdi)
        subWin = self.mdi.addSubWindow(self.form)
        self.centerSubWindow(subWin)
        self.form.show()
