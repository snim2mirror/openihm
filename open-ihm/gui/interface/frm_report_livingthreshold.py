# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import packages
from gui.designs.ui_report_householddisposableincome import Ui_HouseholdDisposableIncome
from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_livingthreshold import LivingThreshhold
from outputs.routines.report_disposableincome_write import HouseholdsIncomeWrite
from frm_report_disposableincome import HouseholdDisposableIncome

from mixins import MDIDialogMixin

#
# FIXME: Are we using this file?
#


class LivingThreshold(QDialog, Ui_HouseholdDisposableIncome, MDIDialogMixin):
    ''' Creates the Household Disposable Income/Living Threshold Report form. Uses the design class
		in gui.designs.ui_report_householddisposableincome. '''	
	
    def __init__(self, parent):
        
	''' Set up the dialog box interface '''
	self.parent = parent
        QDialog.__init__(self)
       	self.setupUi(self)
        self.parent = parent
        self.reporttype = self.cmbReportType.currentText()
        self.connector = HouseholdDisposableIncome(self.parent.parent)

        self.setReportInterface()
        	
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.updateDialogData)
        self.connect(self.cmdShowReport, SIGNAL("clicked()"), self.writeTable)
        self.connect(self.cmdSaveDataTable, SIGNAL("clicked()"), self.writeTable)
        self.connect(self.cmbReportType, SIGNAL("currentIndexChanged(int)"), self.setReportType)
        
    def updateDialogData(self):
        self.connector.updateDialogData()
        
    def setReportInterface(self):
        self.connector.getProjectNames()
        self.connector.insertHouseholdsHeader()
        self.connector.insertPCharsHeader()
        self.cmbReportType.setCurrentIndex(2)

    def getReportTable (self):
        '''Get report table'''

        pid = self.connector.getProjectID()
        householdIDs = connector.getReportHouseholdIDs()
        reporttype = self.setReportType()
        reportconnector = LivingThreshhold()
        reportTable = reportconnector.determineLThresholdPosition(reporttype,pid,householdIDs)
        return reportTable

    def writeTable(self):
        '''Write report output to a spreadsheet'''
        
        reporttable= self.getReportTable()
        writer = HouseholdsIncomeWrite()
        reporttype = self.setReportType()
        writer.writeSpreadsheetReport(reporttable,reporttype)

    def setReportType(self):
        '''Set report type'''
        reporttype = self.cmbReportType.currentText()
        return reporttype
    

