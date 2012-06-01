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
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from data.config import Config
from control.controller import Controller
from mixins import MDIDialogMixin, TableViewMixin
from data.report_settingsmanager import ReportsSettingsManager
from frm_simulation_standardofliving_edit import FrmStandardOfLivingModelPrice
from frm_simulation_diet_edit import FrmDietModelPrice 
from frm_report_disposableincome import HouseholdDisposableIncome
from outputs.routines.report_disposable_income import DisposableHouseholdIncome
from outputs.routines.report_disposable_income_simulation import SimulationDisposableHouseholdIncome
from outputs.routines.report_disposableincome_simulation_write import HouseholdsIncomeWrite
from frm_simulation_incomesources_edit import FrmIncomeSourceModelDetails
from frm_simulation_employment_edit import FrmEmploymentModelDetails
from data.simulation import EditIncomesourcesReferenceData

Ui_HouseholdData, base_class = uic.loadUiType("gui/designs/ui_simulation.ui")

class FrmRunIncomeSimulation(QDialog, Ui_HouseholdData,MDIDialogMixin,TableViewMixin):
    
    ''' Creates the run simulations form '''	
    def __init__(self, parent, hhid=0):
        
	''' Set up the dialog box interface '''
	QDialog.__init__(self)
	self.setupUi(self)
	self.parent = parent
	self.stlitem = ""
	self.stlmodelprice = 0
	self.stlprice = 0
	
	self.connector = ReportsSettingsManager()
	myReferenceVal = QDoubleValidator(0, 100000000,2, self.txtIncomeDefaultValues)
        self.txtIncomeDefaultValues.setValidator(myReferenceVal)

	self.getPorjects()
	self.insertDietHeader()
	self.insertStandardOfLivingHeader()
	self.insertIncomeSourcesHeader()
	
    def resetIncomeReferenceValues(self):
        incomesource = self.getActiveIcomeSourceCategory()
        activeprojectid =self.getProjectID()
        referencevalue = self.txtIncomeDefaultValues.text()
        if referencevalue == "" or activeprojectid =="":
            completionmessage = '''Please make sure that you have selected a project and specified a value to which model values should be set'''
            QMessageBox.information(None, 'Set Reference Values', completionmessage)
        else:
            myconnector = EditIncomesourcesReferenceData()
            myconnector.setIncomeData(incomesource,referencevalue, referencevalue,activeprojectid)
            self.determineIncomeToGet()

    def resetDietReferenceValues(self):
        activeprojectid =self.getProjectID()
        myconnector = EditIncomesourcesReferenceData()
        myconnector.restDietModelData(activeprojectid)
        self.getProjectDiet()

    def resetSTLReferenceValues(self):
        activeprojectid =self.getProjectID()
        myconnector = EditIncomesourcesReferenceData()
        myconnector.resetStandardOfLivingModelData(activeprojectid)
        self.getProjectStandardOfLiving()

    def getPorjects(self):
        ''' populate projects combobox with available projects'''
                
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getProjectNames()

        for row in rows:
		project = row[0]
            	self.cmbProjects.addItem(project)

        self.cmbProjects.setCurrentIndex(-1)

    def getselectedProject(self):
        ''' get name of project selected by user'''
                
        selectedproject = self.cmbProjects.currentText()
        return selectedproject
                
    def getProjectID(self):

        ''' get ID for the selected project'''
                
        selectedproject = self.getselectedProject()
        if selectedproject !="":
                settingsmgr = ReportsSettingsManager()
                selectedprojectid = settingsmgr.getSelectedProjectID(selectedproject)
                return selectedprojectid
        else: return 0

    def insertDietHeader(self):
        '''Insert Title for tblDiets'''
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Food Type'))
        model.setHorizontalHeaderItem(1,QStandardItem('% in Diet'))
	model.setHorizontalHeaderItem(2,QStandardItem('Price'))
	model.setHorizontalHeaderItem(3,QStandardItem('Model Price'))

        self.tblDiets.setModel(model)
        self.tblDiets.show()	

    def insertStandardOfLivingHeader(self):
        '''Insert Title for tblStandardofLiving'''
        
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Expense Type'))
	model.setHorizontalHeaderItem(1,QStandardItem('Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('Model Price'))
        
        self.tblStandardofLiving.setModel(model)
        self.tblStandardofLiving.show()	

    def insertIncomeSourcesHeader(self):
        '''Insert Title for tblIncome'''
        
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
	model.setHorizontalHeaderItem(1,QStandardItem('% Ref Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('% Ref Production'))
        
        self.tblIncome.setModel(model)
        self.tblIncome.show()	

    def getFoodEnergyRequirements(self):
        query = '''SELECT age, kCalNeedM, kCalNeedF FROM lookup_energy_needs'''
	recordset = self.executeResultsQuery(query)
	model = QStandardItemModel(1,2)
				
    def getProjectDiet(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        recordset = settingsmgr.getProjectDiet(projectid)
	model = QStandardItemModel(1,4)

	#set headers
	model.setHorizontalHeaderItem(0,QStandardItem('Food Type'))
        model.setHorizontalHeaderItem(1,QStandardItem('% in Diet'))
	model.setHorizontalHeaderItem(2,QStandardItem('Price'))
	model.setHorizontalHeaderItem(3,QStandardItem('Model Price'))
				
	# add  data rows
	num = 0
		    
	for row in recordset:
	    qtFood = QStandardItem( "%s" % row[0])
	    qtFood.setTextAlignment( Qt.AlignCenter )
		    
	    qtPercentage = QStandardItem( "%i" % row[1] )
	    qtPercentage.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    qtPricePerUnit = QStandardItem( "%i" % row[2] )
	    qtPricePerUnit.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    qtModelPrice = QStandardItem( "%i" % row[3] )
	    qtModelPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    model.setItem( num, 0, qtFood )
	    model.setItem( num, 1, qtPercentage )
	    model.setItem( num, 2, qtPricePerUnit )
	    model.setItem( num, 3, qtModelPrice )
	    num = num + 1
	    
	self.tblDiets.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblDiets.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblDiets.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblDiets.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblDiets.horizontalHeader().setResizeMode(3, QHeaderView.ResizeToContents)
	self.tblDiets.show()

    def getProjectStandardOfLiving(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        recordset = settingsmgr.getProjectStandardofLiving(projectid)
	model = QStandardItemModel(1,3)

	#set headers
        model.setHorizontalHeaderItem(0,QStandardItem('Expense Type'))
	model.setHorizontalHeaderItem(1,QStandardItem('Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('Model Price'))
				
	# add  data rows
	num = 0
	for row in recordset:
	    qtItem = QStandardItem( "%s" % row[0])
	    qtItem.setTextAlignment( Qt.AlignCenter )
		    
	    qtPrice = QStandardItem( "%d" % row[1] )
	    qtPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    qtModelPrice = QStandardItem( "%d" % row[2] )
	    qtModelPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    model.setItem( num, 0, qtItem )
	    model.setItem( num, 1, qtPrice )
	    model.setItem( num, 2, qtModelPrice )
	    num = num + 1
	    
	self.tblStandardofLiving.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblStandardofLiving.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblStandardofLiving.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblStandardofLiving.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblStandardofLiving.show()

    def determineIncomeToGet(self):
        currentincomecategory = self.getActiveIcomeSourceCategory()
        if currentincomecategory =='Crops':
            self.getProjectIncomeSources()
        elif currentincomecategory =='Formal Transfers':
            self.getProjectIncomeSources()
        elif currentincomecategory =='Informal Tansfers':
            self.getProjectIncomeSources()
        elif currentincomecategory =='Livestock':
            self.getProjectIncomeSources()
        elif currentincomecategory =='WildFoods':
            self.getProjectIncomeSources()
        elif currentincomecategory =='Employment':
            self.getProjectEmploymentIncomeSources()
            
    def determineIncomeToEdit(self):
        currentincomecategory = self.getActiveIcomeSourceCategory()
        if currentincomecategory =='Crops':
            self.editIncomeSourceReferenceValues()
        elif currentincomecategory =='Formal Transfers':
            self.editIncomeSourceReferenceValues()
        elif currentincomecategory =='Informal Tansfers':
            self.editIncomeSourceReferenceValues()
        elif currentincomecategory =='Livestock':
            self.editIncomeSourceReferenceValues()
        elif currentincomecategory =='WildFoods':
            self.editIncomeSourceReferenceValues()
        elif currentincomecategory =='Employment':
            self.editEmploymentReferenceValues()

    def getProjectIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        currentincomecategory = self.getActiveIcomeSourceCategory()
        if currentincomecategory =='Crops':
            recordset = settingsmgr.getSimulationCropIncomeSources(projectid)
        elif currentincomecategory =='Formal Transfers':
            recordset = settingsmgr.getSimulationFormalTransferIncomeSources(projectid)
        elif currentincomecategory =='Informal Tansfers':
            recordset = settingsmgr.getSimulationInformalTransferIncomeSources(projectid)
        elif currentincomecategory =='Livestock':
            recordset = settingsmgr.getSimulationLivestockIncomeSources(projectid)
        elif currentincomecategory =='WildFoods':
            recordset = settingsmgr.getSimulationWildfoodsIncomeSources(projectid)
        
	model = QStandardItemModel(1,3)

	#set headers
        model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
	model.setHorizontalHeaderItem(1,QStandardItem('% Ref Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('% Ref Production'))
				
	# add  data rows
	num = 0
	for row in recordset:
	    qtItem = QStandardItem( "%s" % row[0])
	    qtItem.setTextAlignment( Qt.AlignCenter )
		    
	    qtRefPrice = QStandardItem( "%d" % row[1] )
	    qtRefPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    qtRefProduction = QStandardItem( "%d" % row[2] )
	    qtRefProduction.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    model.setItem( num, 0, qtItem )
	    model.setItem( num, 1, qtRefPrice )
	    model.setItem( num, 2, qtRefProduction )
	    num = num + 1
	    
	self.tblIncome.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblIncome.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblIncome.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblIncome.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblIncome.show()


    def getProjectEmploymentIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        recordset = settingsmgr.getSimulationEmploymentIncomeSources(projectid)
        
	model = QStandardItemModel(1,2)

	#set headers
        model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
	model.setHorizontalHeaderItem(1,QStandardItem('% Ref Income'))
				
	# add  data rows
	num = 0
	for row in recordset:
	    qtItem = QStandardItem( "%s" % row[0])
	    qtItem.setTextAlignment( Qt.AlignCenter )
		    
	    qtRefIncome = QStandardItem( "%d" % row[1] )
	    qtRefIncome.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    model.setItem( num, 0, qtItem )
	    model.setItem( num, 1, qtRefIncome )
	    num = num + 1
	    
	self.tblIncome.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblIncome.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblIncome.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblIncome.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblIncome.show()

    def getActiveIcomeSourceCategory(self):
        category = self.cmbIncomeSources.currentText()
        return category

    def editIncomeSourceReferenceValues(self):
	if self.countRowsSelected(self.tblIncome) != 0:
	    # get the age of the selected record
	    selectedRow = self.getCurrentRow(self.tblIncome)
	    incomesource = self.tblIncome.model().item(selectedRow,0).text()
	    preferenceprice = self.tblIncome.model().item(selectedRow,1).text()
	    preferenceproduction = self.tblIncome.model().item(selectedRow,2).text()
	    projectid = self.getProjectID()
	    currentincomecategory = self.getActiveIcomeSourceCategory()

	    # show edit food energy requirement form
	    form = FrmIncomeSourceModelDetails(self.parent,currentincomecategory,incomesource,preferenceprice,preferenceproduction,projectid)
	    form.setWindowIcon(QIcon('resources/images/openihm.png'))
	    form.exec_()
	    self.getProjectIncomeSources()
			
	else:
            
	    QMessageBox.information(self,"Edit Income Sources Model Values","Please select the row containing the model values to be edited.")

    def editEmploymentReferenceValues(self):
	if self.countRowsSelected(self.tblIncome) != 0:
	    # get the age of the selected record
	    selectedRow = self.getCurrentRow(self.tblIncome)
	    incomesource = self.tblIncome.model().item(selectedRow,0).text()
	    preferenceincome = self.tblIncome.model().item(selectedRow,1).text()
	    projectid = self.getProjectID()

	    # show edit food energy requirement form
	    form = FrmEmploymentModelDetails(self.parent,incomesource,preferenceincome,projectid)
	    form.setWindowIcon(QIcon('resources/images/openihm.png'))
	    form.exec_()
	    self.getProjectEmploymentIncomeSources()
			
	else:
            
	    QMessageBox.information(self,"Edit Income Sources Model Values","Please select the row containing the model values to be edited.")


    def editDietPrice(self):
	if self.countRowsSelected(self.tblDiets) != 0:
	    # get the age of the selected record
	    selectedRow = self.getCurrentRow(self.tblDiets)
	    foodname = self.tblDiets.model().item(selectedRow,0).text()
	    percentageindiet = self.tblDiets.model().item(selectedRow,1).text()
	    unitprice = self.tblDiets.model().item(selectedRow,2).text()
	    modelprice = self.tblDiets.model().item(selectedRow,3).text()
	    projectid = self.getProjectID()

	    # show edit food energy requirement form
	    form = FrmDietModelPrice(self.parent,foodname,percentageindiet,unitprice,modelprice,projectid)
	    form.setWindowIcon(QIcon('resources/images/openihm.png'))
	    form.exec_()
	    self.getProjectDiet()
			
	else:
            
	    QMessageBox.information(self,"Edit Diet Model Value","Please select the row containing the model price to be edited.")

    def editStandardOfLiving(self):
	# get the age of the selected record
	if self.countRowsSelected(self.tblStandardofLiving) != 0:
            selectedRow = self.getCurrentRow(self.tblStandardofLiving)
            projectid = self.getProjectID()
            stlitem = self.tblStandardofLiving.model().item(selectedRow,0).text()
            stlprice = self.tblStandardofLiving.model().item(selectedRow,1).text()
            stlmodelprice = self.tblStandardofLiving.model().item(selectedRow,2).text()

            # show edit food energy requirement form
            form = FrmStandardOfLivingModelPrice(self.parent,stlitem, stlprice,stlmodelprice,projectid)
            form.setWindowIcon(QIcon('resources/images/openihm.png'))
            form.exec_()
            self.getProjectStandardOfLiving()
			
	else:
            
	    QMessageBox.information(self,"Edit Standard of Living Model Values","Please select the row containing the model price to be edited.")

    def getReportTables(self):
        reporttype = 'Simulation'
        connector = HouseholdDisposableIncome(reporttype,self.parent)
        normaldisposableincome = connector.getReportTable()
        
    def getNormalDIReportTable (self):
        '''Get report table'''

        pid = self.getProjectID()
        householdIDs = self.getReportHouseholdIDs()
        reporttype = 'Simulation'
        connector = DisposableHouseholdIncome()
        simconnector = SimulationDisposableHouseholdIncome()
        writeconnector = HouseholdsIncomeWrite()
        normalDIreportTable = connector.householdDisposableIncome(reporttype,pid,householdIDs)
        simulationDIreportTable = simconnector.householdDisposableIncome(reporttype,pid,householdIDs)
        writeconnector.writeSpreadsheetReport(normalDIreportTable,simulationDIreportTable)
        return simulationDIreportTable
    
    def getReportHouseholdIDs(self):
        householdnumbers = []
        projectid = self.getProjectID()
        connector = ReportsSettingsManager()
        recordset = connector.getHouseholdIDs(projectid)
        for row in recordset:
            householdnumbers.append(str(row[0]))
        return householdnumbers
