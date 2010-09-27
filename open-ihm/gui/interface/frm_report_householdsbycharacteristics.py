#	Filename: frm_report_householdsbycharacteristics.py
#
#	Display dialog for Report households by characteristics.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the About OpenIHM design class
from gui.designs.ui_report_householdsbycharacteristics import Ui_HouseHoldReport
from data.report_settingsmanager import ReportsSettingsManager

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
        	
        	self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
        	self.connect(self.cmbProjectNames, SIGNAL("currentIndexChanged(int)"), self.getHouseholdCharacteristics)
        	self.connect(self.cmbProjectNames, SIGNAL("currentIndexChanged(int)"), self.getPersonalCharacteristics)
        	self.connect(self.cmdGenerateReport, SIGNAL("clicked()"), self.getHouseholdCharacteristicsQuery)
        	self.connect(self.cmdGenerateReport, SIGNAL("clicked()"), self.getPersonalCharacteristicsQuery)


        def getProjectNames(self):
                settingsmgr = ReportsSettingsManager()
                rows = settingsmgr.getProjectNames()

                for row in rows:
			project = row[0]
            		self.cmbProjectNames.addItem(project)

            	self.cmbProjectNames.setCurrentIndex(-1)
                self.cmbHouseholds.setCurrentIndex(-1)

        def getselectedProject(self):
                selectproject = self.cmbProjectNames.currentText()
                
        def getProjectID(self):
                selectedproject = self.cmbProjectNames.currentText()
                if selectedproject !="":
                        settingsmgr = ReportsSettingsManager()
                        selectedprojectid = settingsmgr.getSelectedProjectID(selectedproject)
                        return selectedprojectid
                else: return 0
                
        def getHouseholdCharacteristics(self):
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
                        if qtHCharacteristic.text() != 'hhid':
                                model.setItem( num, 0, qtHCharacteristic )
                                num = num + 1
                        		
                self.listViewHCharacteristics.setModel(model)
                self.listViewHCharacteristics.show()	

        def getPersonalCharacteristics(self):
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
                        
                        if ((qtPCharacteristic.text() != 'hhid')and(qtPCharacteristic.text() != 'personid')):
                                model.setItem( num, 0, qtPCharacteristic )
                                num = num + 1
                        		
                self.listViewPersonalCharacteristics.setModel(model)
                self.listViewPersonalCharacteristics.show()	

	def getSelectedHouseholdCharacteristics(self):
		
		selectedHChars = []
		selectedIndexes = self.listViewHCharacteristics.selectedIndexes()
		
		for indexVal in selectedIndexes:
                        currentitem = self.listViewHCharacteristics.model().item(indexVal.row(),0).text()
			if currentitem not in selectedHChars:
				selectedHChars.append(currentitem)
		print selectedHChars		
		return selectedHChars

	def getSelectedPersonalCharacteristics(self):
		
		selectedRows = []
		selectedIndexes = self.listViewPersonalCharacteristics.selectedIndexes()
		
		for indexVal in selectedIndexes:
                        currentitem = self.listViewPersonalCharacteristics.model().item(indexVal.row(),0).text()
			if currentitem not in selectedRows:
				selectedRows.append(currentitem)
		print selectedRows		
		return selectedRows
	 

        def getPersonalCharacteristicsQuery(self):
                selectedRows = []
                selectedRows = self.getSelectedPersonalCharacteristics()
                
                
        def getHouseholdCharacteristicsQuery(self):
                selectedHChars = []
                selectedHChars = self.getSelectedHouseholdCharacteristics()
                
        def getReportData(self):
                pass
        def writeReport(self):
                pass
