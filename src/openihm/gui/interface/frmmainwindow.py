#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""

# pylint: disable=W0312
# pylint: disable=W0511
# pylint: disable=W0703

import os
import logging
import stat
import tempfile

from PyQt4 import QtGui, QtCore, uic

# import the main window design class
Ui_MainWindow, base_class = uic.loadUiType("gui/designs/ui_mainwindow.ui")

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
from frm_report_householdbudgets import RepHouseholdBudget

#import dialog for transfering data from access db
from frmimportfromaccessdb import FrmImportFromAccessDB


# Import modules used by the automatic software updator.
from mercurial import commands, hg, ui, error
from distutils.dir_util import copy_tree
import shutil
import sys
import traceback

# FIXME: Edit this value in Brown's innosetup script, take it from an .ini file.
REPO_DIR = os.path.expanduser(os.path.join('~', '.openihmrepo'))

# FIXME: Can we get INSTALL_DIR from an .ini file or similar?
INSTALL_DIR = os.path.normpath(os.path.dirname(__file__) + '../../../')
#INSTALL_DIR = '/home/snim2/site-packages' # Just for testing

# FIXME: Refactor this out to its own file.
class OpenIhmUpdator(QtCore.QThread):
    """This class automatically updates open-ihm from the Google Code repository.

    Requires Mercurial to be installed.
    """

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.logger = logging.getLogger('__main__')
        self.info = lambda msg : self.logger.info(msg)
        self.debug = lambda msg : self.logger.debug(msg)        
        self.ui = ui.ui()
        self.url = 'https://open-ihm.googlecode.com/hg/'
        try:
            self.repo = hg.repository(self.ui, REPO_DIR)
        except Exception:
            self.repo = hg.repository(self.ui, REPO_DIR, create=True)
        return

    def chmod(self):
        """Fix a Windows bug which marks files / folders in REPO_DIR read-only.
        """
        if not (sys.platform == 'win32' or sys.platform == 'cygwin'):
            return
        for root, dirs, files in os.walk(REPO_DIR):
            for name in files:
                os.chmod(os.path.join(root, name), stat.S_IWRITE)
            for name in dirs:
                os.chmod(os.path.join(root, name), stat.S_IWRITE)                

    def fail(self):
        """Called if an error occurs.

        Take the traceback, log it and notify the MainWindow.
        """
        ty, value, tback = sys.exc_info()
        msg = ''.join(traceback.format_exception(ty, value, tback))
        self.debug(msg)
        self.updateFail(msg)
        return

    def run(self):
        # Redirect stdin and stdout to tempfiles. 
        # This fixes a Windows bug which causes a Bad File Descriptor error.
        sys.stdout = tempfile.TemporaryFile()
        sys.stderr = tempfile.TemporaryFile()
        try:
            self.pullAndMerge()
        except Exception:
            self.fail()
            return
        try:
            self.install()
        except Exception:
            self.fail()
            return
        self.emit(QtCore.SIGNAL("updateSuccess()"))
        return

    def clone(self):
        """If we don't have a copy of the open-ihm repository on disk
        clone one now.
        """
        try:
            self.chmod()
            commands.clone(self.ui, self.url, dest=REPO_DIR, insecure=True)
        except Exception:
            self.fail()
        return

    def pullAndMerge(self):
        """Run an hg pull and update.
        Overwrite all local changes by default.
        If anything goes wrong with the pull or update, clone instead.
        """
        try:
            self.chmod()
            commands.pull(self.ui, self.repo, source=self.url)
            self.chmod()
            commands.update(self.ui, self.repo, clean=True)
        except error.RepoError:
            if os.path.exists(REPO_DIR):
                shutil.rmtree(REPO_DIR)
                self.clone()
        return
    
    def install(self):
        """Copy code to site-packages.

        FIXME: Do this with setuptools or distutils or similar. May need runpy.
        """
        copy_tree(os.path.join(REPO_DIR, 'src/openihm'), INSTALL_DIR)
        return

    def updateFail(self, message):
        """If checking for updates times out (for example, if there
        is no current network connection) then fail silently.
        """
        self.emit(QtCore.SIGNAL("updateFailure(QString)"), QtCore.QString(message))
        return


class PicturedMDIArea(QtGui.QMdiArea):
    """This class creates an MDI area with a centred background image.

    Code is adapted from here:
    
    http://www.diotavelli.net/PyQtWiki/Adding%20a%20background%20image%20to%20an%20MDI%20area

    Thanks to David Boddie on the PyQt mailing list.
    """
    
    def __init__(self, background_pixmap, parent = None):
        QtGui.QMdiArea.__init__(self, parent)
        self.background_pixmap = background_pixmap
        self.display_pixmap = None
    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self.viewport())
        painter.setBrush(QtGui.QColor(220, 220, 220))
        painter.drawRect(0, 0, self.width(), self.height())
        x = (self.width() - self.background_pixmap.width())/2
        y = (self.height() - self.background_pixmap.height())/2
        painter.drawPixmap(x, y, self.background_pixmap)
        painter.end()
    
    def resizeEvent(self, event):
        """
        Ensure that the logo stays in the centre of the screen on resize.
        """
        self.display_pixmap = self.background_pixmap.scaled(event.size(), QtCore.Qt.KeepAspectRatio)


class FrmMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_mainwindow module '''
    
    def __init__(self, parent=None):
        ''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.projectid = -1
        self.projectname = ""

        pixmap = QtGui.QPixmap('resources/images/EfDUnimaChancoComposite.jpg')
        self.mdi = PicturedMDIArea(pixmap)
        
        self.setCentralWidget(self.mdi)

        self.actionClose_Project.setDisabled(True)

        self.assistant = None # Help assistant

        self.thread = OpenIhmUpdator() # For updating software
        self.updateSuccessful = True
        
	### FIXME: Replace absolute paths to images with Qt resources
        self.setWindowIcon(QtGui.QIcon('resources/images/openihm.png'))

        ### FIXME: Should do this in Qt4Deisgner
        self.actionOpen_Project.setIcon(QtGui.QIcon('resources/images/projectOpen.png'))
        self.actionCreate_Project.setIcon(QtGui.QIcon('resources/images/projectNew.png'))
        self.actionFind_Project.setIcon(QtGui.QIcon('resources/images/projectFind.png'))
        self.actionClose_Project.setIcon(QtGui.QIcon('resources/images/projectClose.png'))
        
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
        ''' Creates and Shows the dialog for listing households that match selected personal and houshold characteristics'''
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
            
    def importFromAccessDB(self):
        """Imports projects from the old access based IHM software"""
        form = FrmImportFromAccessDB()
        form.exec_()
                
    def reportHouseholdDisposableIncome(self,reporttype):
        """Creates and Shows the Report: Household Disposable Income form"""
        form = HouseholdDisposableIncome(self,reporttype)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

    def initialiseFoodRequirementTable(self):
        """Create Initial Kcal values for certain crops/foods"""
        initialiser = FoodRequirementValues()
        initialiser.insertSartUpValues()
             
    def setReporttypeAsLivingThreshold(self):
        """set report type for Living Threshold report"""
        reporttype = 'LivingThreshold'
        self.reportHouseholdDisposableIncome(reporttype)
                
    def setReporttypeDI(self):
        """set report type for Household Disposable Income report"""
        reporttype = 'DI'
        self.reportHouseholdDisposableIncome(reporttype)

    def updateOpenIhm(self):
        """Automatically fetch and install latest software from Google Code repo.
        """
        msg = ("Software update starting. \n" +
               "This may take some time.\n" +
               "Please make sure you have a working Internet connection" +
               "and do not close open-ihm until you see a message " +
               "saying that the update has finished.")
        QtGui.QMessageBox.information(self, "Software update notice", msg)

        self.connect(self.thread, QtCore.SIGNAL("updateSuccess()"), self.updateSuccess)
        self.connect(self.thread, QtCore.SIGNAL("updateFailure(QString)"), self.updateFailed)
        self.connect(self.thread, QtCore.SIGNAL("noChanges()"), self.updateNoChanges)
        self.thread.start()
        return

    def updateNoChanges(self):
        """No changes to pull.

        FIXME: Could remove this if it the updator never signals.
        """
        msg = ("There are no software updates currently available.")
        QtGui.QMessageBox.information(self, "Software update notice", msg)
        return
    
    def updateFailed(self, message):
        """Report to the user that a software update has failed.
        """
        msg = ("Software update failed.\n" +
               "Please report this error to the mailing list" +
               str(message))
        QtGui.QMessageBox.critical(self, "Software update notice", msg)
        return

    def updateSuccess(self):
        """Report to the user that a software update has been successful.
        open-ihm now needs to be restarted.
        """
        msg = ("Software update was successful.\n" +
               "Please close open-ihm and restart for changes to take effect.")
        QtGui.QMessageBox.information(self, "Software update notice", msg)
        return
        
    def openHelpContents(self):
        """Open online help.
        Triggered when the user presses F1 or selects Contents from
        the Help menu.
        """
        return

    def reportHouseholdbudget(self):
        ''' Creates and Shows the dialog for Household Budget Reports'''
        form = RepHouseholdBudget(self)
        subWin = self.mdi.addSubWindow(form)
        self.centerSubWindow(subWin)
        form.show()

#        if not self.assistant or not self.assistant.poll()==None:
#            helpcoll = 'help/collection.qhc'        
#            cmd = "assistant-qt4 -enableRemoteControl -collectionFile %s" % helpcoll
#            self.assistant = subprocess.Popen(cmd,
#                                              shell = True,
#                                              stdin = subprocess.PIPE)
#            self.assistant.stdin.write("SetSource qthelp://urssus/doc/handbook.html\n")
                
    # def reportLivingThreshold(self):
    #     form = LivingThreshold(self)
    #     subWin = self.mdi.addSubWindow(form)
    #     self.centerSubWindow(subWin)
    #     form.show()


