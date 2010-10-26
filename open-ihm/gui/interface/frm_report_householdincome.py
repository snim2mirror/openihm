#	Filename: frm_report_householdincome.py
#
#	Display dialog for Report household income by income source.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import packages
from gui.designs.ui_report_householdincome import Ui_HouseholdIncomeReport
from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_householdsincome import HouseholdIncome
from outputs.routines.report_householdsincome_write import HouseholdsIncomeWrite
class HouseholdIncomeReport(QDialog, Ui_HouseholdIncomeReport):
    ''' Creates the Household Income Report by Source from. Uses the design class
		in gui.designs.ui_report_householdincome. '''	
	
    def __init__(self, parent):
        
	''' Set up the dialog box interface '''
	self.parent = parent
        QDialog.__init__(self)
       	self.setupUi(self)
        self.parent = parent

        self.getProjectNames()
        self.putMainIncomeCategories()
        self.insertHouseholdsHeader()
        self.insertPCharsHeader()
        	
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.updateDialogData)
        self.connect(self.cmdShowReport, SIGNAL("clicked()"), self.writeTable)
        self.connect(self.cmdSaveDataTable, SIGNAL("clicked()"), self.writeTable)

    def updateDialogData(self):
        '''Update Income Sources list to those relevant for the current project'''
        self.putCropIncomeSources()
        self.getHouseholdCharacteristics()
        self.getPersonalCharacteristics()
        self.putHouseholdNames()
        self.putEmploymentIncomeSources()
        self.putLivestockIncomeSources()
        #self.putLoanSources()
        self.putTransferIncomeSources()
        self.putwildFoodIncomeSources()

    def getProjectNames(self):
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


    def putMainIncomeCategories(self):
        ''' Insert Income categories in the Income sources treeview'''

        categories = ['Crops','Employment','Livestock','Loans','Transfers','Wild Foods']
        num = 0
        model = QStandardItemModel()
        parent = QModelIndex()
        child = QModelIndex()

        parent = model.index( 0, 0 )
        model.insertColumn(0, parent ) #one column for children
        model.insertRows( 0, 6, parent )
        model.setHorizontalHeaderItem(0,QStandardItem('Income Sources'))
        
        for row in categories:
            child = model.index( num, 0, parent )
            model.setData(child, row)
            num = num + 1
                        		
        self.treeView.setModel(model)
        self.treeView.show()

    def getCropsIndex(self):
        '''Get index of Crops Category form the Dialog's TreeView'''
        cropsindex = self.treeView.model().index(0, 0)
        return cropsindex
    
    def putCropIncomeSources(self):
        '''Insert Crop Income Sources into the Household Income Dialog's TreeView'''
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getCropIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getCropsIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getEmploymentIndex(self):
        '''Get index of Employment Category form the Dialog's TreeView'''
        parentindex = self.treeView.model().index(1, 0)
        return parentindex

    def putEmploymentIncomeSources(self):
        '''Insert Employment Income Sources into the Household Income Dialog's TreeView'''
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getEmploymentIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getEmploymentIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getLivestockIndex(self):
        '''Get index of Livestock Category form the Dialog's TreeView'''
        parentindex = self.treeView.model().index(2, 0)
        return parentindex


    def putLivestockIncomeSources(self):
        '''Insert Livestock Income Sources into the Household Income Dialog's TreeView'''
        
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getLivestockIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getLivestockIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getLoansIndex(self):
        '''Get index of Loans Category form the Dialog's TreeView'''
        parentindex = self.treeView.model().index(3, 0)
        return parentindex

    def putLoanSources(self):
        '''Insert Loan Income Sources into the Household Income Dialog's TreeView'''
        
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getLoanIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getLoansIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getTransferIncomeIndex(self):
        '''Get index of Transfers Category form the Dialog's TreeView'''
        parentindex = self.treeView.model().index(4, 0)
        return parentindex

    def putTransferIncomeSources(self):
        '''Insert Transfer Income Sources into the Household Income Dialog's TreeView'''
        
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getTransferIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getTransferIncomeIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getWildFoodsIncomeIndex(self):
        '''Get index of Wild Foods Category form the Dialog's TreeView'''
        
        parentindex = self.treeView.model().index(5, 0)
        return parentindex

    def putwildFoodIncomeSources(self):
        '''Insert Wild Food Income Sources into the Household Income Dialog's TreeView'''
        
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getWildfoodsIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getWildFoodsIncomeIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getHouseholdNames(self):
        '''Get Names of Households selected by the User on the Interface'''
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getProjectHouseholds(projectid)
        return rows

    def insertHouseholdsHeader(self):
        '''Insert Title for treeViewHouseholds'''
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Select Household Names'))
        self.treeViewHouseholds.setModel(model)
        self.treeViewHouseholds.show()	

    def insertPCharsHeader(self):
        '''Insert Title for listViewHCharacteristics'''
        
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Personal Characteristics'))
        self.listViewHCharacteristics.setModel(model)
        self.listViewHCharacteristics.show()	


    def putHouseholdNames(self):
        ''' Insert household names for the selected Project'''

        hholdnames = self.getHouseholdNames()
        model = QStandardItemModel()
        parent = QModelIndex()
        name = 'All Households'
        numberofrows = len(hholdnames)

        model.insertRow(0,parent )
        model.insertColumn(0, parent ) #one column for children
        parent = model.index( 0, 0 )
        model.setData( parent, name )

        #Insert project-specific household names as childred of the node 'All Households'
        parent = model.index(0, 0, QModelIndex())
        model.insertColumn(0, parent )
        model.insertRows( 0, numberofrows, parent )
        num = 0
        for row in hholdnames:
 
            child = model.index( num, 0, parent )
            model.setData(child, row[0])
            num = num + 1
                        		
        model.setHorizontalHeaderItem(0,QStandardItem('Select Household Names'))
        self.treeViewHouseholds.setModel(model)
        self.treeViewHouseholds.show()	

    def getHouseholdCharacteristics(self):
        
        ''' get household characteristics relevant to selected project'''
                
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getHouseholdCharacteristics(projectid)
        model = QStandardItemModel()
	num = 0

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
        '''Get indexes of selected Personal characteristics'''
        return self.listViewPersonalCharacteristics.selectedIndexes()

    def getSelectedHouseholdsIndexes(self):
        '''Get indexes of selected Household characteristics'''
        return self.treeViewHouseholds.selectedIndexes()
        
    def getReportHouseholdIDs (self):
        '''Get a list of households that match a users selection criteria -i.e Household names + Personal Characteristics and Household Characteristics'''
        
        selectedids = []
        householdIDsQuery =self.getHouseholdIDsQuery()
        connector = HouseholdIncome()
        householdIDs = connector.getReportHouseholdIDs(householdIDsQuery)
        for hid in householdIDs:
            selectedids.append(str(hid[0]))
        return selectedids

    def getHouseholdIDsQuery(self):
        '''Get query for generating a list of households that match a users selection criteria'''

        projectid = self.getProjectID()
        selectedHChars = self.getSelectedHouseholdCharacteristics()
        selectedPChars = self.getSelectedPersonalCharacteristics()
        selectedhouseholds = self.getHouseholdsSelection()
        connector = HouseholdIncome()
        householdIDsQuery = connector.buildReportHouseholdIDsQuery(projectid,selectedhouseholds,selectedPChars,selectedHChars)
        return householdIDsQuery

    def getHouseholdsSelection(self):
        '''Get names of households selected by the user for charting'''
        
        selectedIndexes = self.getSelectedHouseholdsIndexes()
        parentIndex = self.treeViewHouseholds.model().index(0, 0, QModelIndex())
        hholdnames = []
        
        if len(selectedIndexes) != 0:
            if parentIndex in selectedIndexes:
                houses = self.getHouseholdNames()
                for house in houses:
                    hholdnames.append(str(house[0]))
            else:
                for indexVal in selectedIndexes:
                    currentitem = self.treeViewHouseholds.model().data(indexVal, Qt.DisplayRole).toString()
                    hholdnames.append(str(currentitem))
        else:
            QMessageBox.information(self,"Households By Income Source","No Households Selected")
        return hholdnames

    def getCropReportDetails(self):
        '''Get list of crops selected by the user for charting'''
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getCropsIndex()
            selectedIndexes = self.getSelectedCropCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedCropCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        cropsroot = self.getCropsIndex()
        cropincomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == cropsroot) or (indexVal.parent() == cropsroot):
                if indexVal not in cropincomeIndexes:
                    cropincomeIndexes.append(indexVal)
        return cropincomeIndexes

    def getEmploymentReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getEmploymentIndex()
            selectedIndexes = self.getSelectedEmploymentCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedEmploymentCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getEmploymentIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)
        return incomeIndexes

    def getLivestockReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getLivestockIndex()
            selectedIndexes = self.getSelectedLivestockCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedLivestockCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getLivestockIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)
        return incomeIndexes

    def getLoansReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getLoansIndex()
            selectedIndexes = self.getSelectedLoansCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedLoansCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getLoansIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)
        return incomeIndexes

    def getTransfersDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getTransferIncomeIndex()
            selectedIndexes = self.getSelectedTransfersCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedTransfersCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getTransferIncomeIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)
        return incomeIndexes

    def getWildFoodDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getWildFoodsIncomeIndex()
            selectedIndexes = self.getSelectedWildFoodsCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        requiredDetailType.append(str(currentitem))
        return requiredDetailType
        
    def getSelectedWildFoodsCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getWildFoodsIncomeIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)
        return incomeIndexes

    def getReportTable (self):
        
        reportQuery =self.getFinalReportTableQuery()
        connector = HouseholdIncome()
        reportTable = connector.getReportTable(reportQuery)
        return reportTable

    def getFinalReportTableQuery(self):

        projectid = self.getProjectID()
        householdIDs = self.getReportHouseholdIDs()
        cropdetails = self.getCropReportDetails()
        employmentdetails = self.getEmploymentReportDetails()
        livestockdetails = self.getLivestockReportDetails()
        loandetails = self.getLoansReportDetails()
        transferdetails = self.getTransfersDetails()
        wildfoodsdetails = self.getWildFoodDetails()

        connector = HouseholdIncome()
        householdIDsQuery = connector.getFinalIncomeReportTableQuery(projectid,householdIDs,cropdetails,employmentdetails, livestockdetails,loandetails,transferdetails,wildfoodsdetails )
        return householdIDsQuery

    def writeTable(self):
        reporttable= self.getReportTable()
        writer = HouseholdsIncomeWrite()
        writer.writeSpreadsheetReport(reporttable)
        
