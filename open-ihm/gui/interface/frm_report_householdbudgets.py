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
from gui.designs.ui_report_householdbudget import Ui_HouseholdBudget
from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_householdbudget import HouseholdBudget
from outputs.routines.report_householdbudget_write import HouseholdBudgetWrite

from mixins import MDIDialogMixin

class RepHouseholdBudget(QDialog, Ui_HouseholdBudget, MDIDialogMixin):
        ''' Creates a Report for Household budgets. Uses the design class
		in gui.designs.ui_report_householdbudget. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

        	self.getProjectNames()

        def getProjectNames(self):
                ''' populate projects combobox with available projects'''
                
                settingsmgr = ReportsSettingsManager()
                rows = settingsmgr.getProjectNames()

                for row in rows:
			project = row[0]
            		self.cmbProjectNames.addItem(project)

            	self.cmbProjectNames.setCurrentIndex(-1)
                self.cmbHouseholds.setCurrentIndex(-1)

        def getselectedProject(self):
                ''' get name of project selected by user'''
                
                selectproject = self.cmbProjectNames.currentText()
                
        def getProjectID(self):

                ''' get ID for the selected project'''
                
                selectedproject = self.cmbProjectNames.currentText()
                if selectedproject !="":
                        settingsmgr = ReportsSettingsManager()
                        selectedprojectid = settingsmgr.getSelectedProjectID(selectedproject)
                        return selectedprojectid
                else: return 0
                

        def getHouseholds(self):
                ''' get households (numbers and names) for selected project & populate dialog lists'''
                
                projectid = self.getProjectID()
                settingsmgr = ReportsSettingsManager()
                rows = settingsmgr.getHouseholds(projectid)
                model = QStandardItemModel()
                model1 = QStandardItemModel()
		num = 0

                for row in rows:
                        
                        qtHNumber = QStandardItem( "%s" % row[0])
                        qtHNumber.setTextAlignment( Qt.AlignLeft )
                        qtHName = QStandardItem( "%s" % row[1])
                        qtHName.setTextAlignment( Qt.AlignLeft )
                        model.setItem( num, 0, qtHNumber )
                        model1.setItem( num, 0, qtHName )
                        num = num + 1
                        		
                self.listViewHNumbers.setModel(model)
                self.listViewHNames.setModel(model1)
                self.listViewHNumbers.show()
                self.listViewHNames.show()

	def getSelectedHouseholdNumbers(self):
                ''' get list of user selected household numbers as part of the criteria for report generation'''
		
		selectedHNumbers = []
		selectedIndexes = self.getSelectedHIndexes()
		
		for indexVal in selectedIndexes:
                        currentitem = self.listViewHNumbers.model().item(indexVal.row(),0).text()
			if currentitem not in selectedHNumbers:
				selectedHNumbers.append(str(currentitem))
		return selectedHNumbers

        def getSelectedHIndexes(self):
                return self.listViewHNumbers.selectedIndexes()

        def getHouseholdMembership(self,projectid,selectedHNumbers):
                ''' get lists of household members for selected households'''
                
                householdMembersip = []
                connector = HouseholdBudget()
                householdMembersip = connector.getHouseholdMembership(projectid,selectedHNumbers)
                return householdMembersip

        def getHouseholdAssets(self,projectid,selectedHNumbers):
                ''' get lists of household members for selected households'''
                
                householdAssets = []
                connector = HouseholdBudget()
                householdAssets = connector.getHouseholdMembership(projectid,selectedHNumbers)
                return householdAssets
                
        def getReportData(self):
                ''' get households that meet the combined criteria of household and personal characteristics'''
                
                projectid = self.getProjectID()
                if self.cmbHouseholds.currentText() =='All Households':
                        allhid = []
                        row = 0
                        while (self.listViewHNumbers.model().item(row,0)):
                            val = self.listViewHNumbers.model().item(row,0).text()
                            allhid.append(str(val))
                            row = row + 1
                        selectedHNumbers = allhid
                else:
                        selectedHNumbers = self.getSelectedHouseholdNumbers()
                        
                connector = HouseholdBudget()
                householdMembership  = connector.getHouseholdMembership(projectid,selectedHNumbers)
                householdAssets     = connector.getAssets(projectid,selectedHNumbers)
                householdFoodIncome = connector.getFoodIncome(projectid,selectedHNumbers)
                householdCashIncome = connector.getCashIncome(projectid,selectedHNumbers)
                householdBudgetSummary = connector.householdBudgetSummaries(projectid,selectedHNumbers)
                
                return (selectedHNumbers,householdMembership,householdAssets,householdCashIncome,householdFoodIncome,householdBudgetSummary)
                
        def writeSpreadsheet(self):
                ''' Creates a Spreadsheet showing hoseholds that fit selected criteria '''
                connector = HouseholdBudgetWrite()
                selectedHouseholds,householdMembership,householdAssets,householdCashIncome,householdFoodIncome,householdBudgetSummary = self.getReportData()
                connector.writeSpreadsheetReport(selectedHouseholds,householdMembership,householdAssets,householdCashIncome,householdFoodIncome,householdBudgetSummary)
        
                
