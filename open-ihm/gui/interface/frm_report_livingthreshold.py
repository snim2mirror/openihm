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
    

