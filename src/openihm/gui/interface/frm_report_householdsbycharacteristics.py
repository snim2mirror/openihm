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
from PyQt4 import uic

# import packages
Ui_HouseHoldReport, base_class = uic.loadUiType("gui/designs/ui_report_householdsbycharacteristics.ui")


from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_households_by_characteristics import HouseholdsByCharacteristics
from frm_report_householdsbycharacteristics_display import HouseholdsByCharDisplay
from outputs.routines.report_households_by_characteristics_write import HouseholdsByCharacteristicsWrite

from mixins import MDIDialogMixin

class RepHouseholdsByCharacteristics(QDialog, Ui_HouseHoldReport, MDIDialogMixin):
        ''' Creates the Report Households by Characteristics from. Uses the design class
		in gui.designs.ui_report_householdsbycharacteristics. '''	
	
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
                
        def getHouseholdCharacteristics(self):
                ''' get household characteristics relevant to selected project'''
                
                projectid = self.getProjectID()
                settingsmgr = ReportsSettingsManager()
                rows = settingsmgr.getHouseholdCharacteristics(projectid)
                model = QStandardItemModel()
		num = 0
		#x=0

       		#if rows.count(x) != 0:
                for row in rows:
                        qtHCharacteristic = QStandardItem( "%s" % row[0])
                        qtHCharacteristic.setTextAlignment( Qt.AlignLeft )
                        if ((qtHCharacteristic.text() != 'hhid')and(qtHCharacteristic.text() != 'pid') ):
                                model.setItem( num, 0, qtHCharacteristic )
                                num = num + 1
                        		
                self.listViewHCharacteristics.setModel(model)
                self.listViewHCharacteristics.show()	

        def getPersonalCharacteristics(self):
                ''' get personal characteristics relevant to the selected project'''
                
                projectid = self.getProjectID()
                settingsmgr = ReportsSettingsManager()
                rows = settingsmgr.getPersonalCharacteristics(projectid)
                model = QStandardItemModel()
		num = 0
		#x=0

       		#if rows.count(x) != 0:
                for row in rows:
                        qtPCharacteristic = QStandardItem( "%s" % row[0])
                        qtPCharacteristic.setTextAlignment( Qt.AlignLeft )
                        
                        if ((qtPCharacteristic.text() != 'hhid')and(qtPCharacteristic.text() != 'personid') and (qtPCharacteristic.text() != 'pid')):
                                model.setItem( num, 0, qtPCharacteristic )
                                num = num + 1
                        		
                self.listViewPersonalCharacteristics.setModel(model)
                self.listViewPersonalCharacteristics.show()	

	def getSelectedHouseholdCharacteristics(self):
                ''' get list of user selected household characteristics as part of the criteria for report generation'''
		
		selectedHChars = []
		selectedIndexes = self.getSelectedHIndexes()
		
		for indexVal in selectedIndexes:
                        currentitem = self.listViewHCharacteristics.model().item(indexVal.row(),0).text()
			if currentitem not in selectedHChars:
				selectedHChars.append(str(currentitem))
		return selectedHChars

        def getSelectedHIndexes(self):
                return self.listViewHCharacteristics.selectedIndexes()

	def getSelectedPersonalCharacteristics(self):
                ''' get list of user selected househpersonal characteristics as part of the criteria for report generation'''
		
		selectedRows = []
		selectedIndexes = self.getSelectedPIndexes()
		
		for indexVal in selectedIndexes:
                        currentitem = self.listViewPersonalCharacteristics.model().item(indexVal.row(),0).text()
			if currentitem not in selectedRows:
				selectedRows.append(str(currentitem))
		return selectedRows

        def getSelectedPIndexes(self):
                return self.listViewPersonalCharacteristics.selectedIndexes()

        def getPersonalCharacteristicsQuery(self):
                ''' build query for selecting household that match the selected personal characteristics'''
                
                selectedRows = []
                selectedRows = self.getSelectedPersonalCharacteristics()
                projectid = self.getProjectID()
                pchars = ReportsSettingsManager ()
                tablename = pchars.setPCharacteristicsTableName(projectid)
                connector = HouseholdsByCharacteristics()
                pquery = connector.buildPCharacteristicsQuery(selectedRows,tablename,projectid)
                return pquery
                
        def getHouseholdCharacteristicsQuery(self):
                ''' build query for selecting household that match the selected household characteristics'''
                
                selectedHChars = []
                selectedHChars = self.getSelectedHouseholdCharacteristics()
                projectid = self.getProjectID()
                hchars = ReportsSettingsManager ()
                tablename = hchars.setHCharacteristicsTableName(projectid)
                connector = HouseholdsByCharacteristics()
                hquery = connector.buildHCharacteristicsQuery(selectedHChars,tablename,projectid)
                return hquery
                
        def getReportData(self):
                ''' get households that meet the combined criteria of household and personal characteristics'''
                
                pquery = self.getPersonalCharacteristicsQuery()
                hquery = self.getHouseholdCharacteristicsQuery()
                projectid = self.getProjectID()
                
                #check if any characteristics have been selected
                pcharselected = len(self.getSelectedPIndexes())
                hcharselected = len(self.getSelectedHIndexes())
                
                reporttable = []
                report = HouseholdsByCharacteristics()
                reporttable = report.getReportTable(projectid,pcharselected,hcharselected,pquery,hquery)
                return reporttable
                
        def writeSpreadsheet(self):
                ''' Creates a Spreadsheet showing hoseholds that fit selected criteria '''
                reportatble = self.getReportData()
                connector = HouseholdsByCharacteristicsWrite()
                connector.writeSpreadsheetReport(reportatble)
        
                
