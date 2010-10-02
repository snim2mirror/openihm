#	Filename: frm_report_householdsbycharacteristics.py
#
#	Display dialog for Report households by characteristics.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import packages
from gui.designs.ui_report_householdsbycharacteristics import Ui_HouseHoldReport
from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_households_by_characteristics import HouseholdsByCharacteristics
from frm_report_householdsbycharacteristics_display import HouseholdsByCharDisplay

class RepHouseholdsByCharacteristics(QDialog, Ui_HouseHoldReport):	
	''' Creates the Report Households by Characteristics from. Uses the design class
		in gui.designs.ui_report_householdsbycharacteristics. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

        	self.getProjectNames()
        	
        	self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        	self.connect(self.cmbProjectNames, SIGNAL("currentIndexChanged(int)"), self.getHouseholdCharacteristics)
        	self.connect(self.cmbProjectNames, SIGNAL("currentIndexChanged(int)"), self.getPersonalCharacteristics)
        	self.connect(self.cmdGenerateReport, SIGNAL("clicked()"), self.displayReport)



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
                households = HouseholdsByCharacteristics()
                pquery = households.buildPCharacteristicsQuery(selectedRows,tablename)
                return pquery
                
        def getHouseholdCharacteristicsQuery(self):
                ''' build query for selecting household that match the selected household characteristics'''
                
                selectedHChars = []
                selectedHChars = self.getSelectedHouseholdCharacteristics()
                projectid = self.getProjectID()
                hchars = ReportsSettingsManager ()
                tablename = hchars.setHCharacteristicsTableName(projectid)
                households = HouseholdsByCharacteristics()
                hquery = households.buildHCharacteristicsQuery(selectedHChars,tablename)
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
                
        def displayReport(self):
            ''' Creates and Shows the Report: Households by characteristics form '''
            freporttable = self.getReportData()
	    form = HouseholdsByCharDisplay(self.parent,freporttable)
	    subWin = self.parent.mdi.addSubWindow(form)
	    self.parent.centerSubWindow(subWin)
	    form.show()

                
