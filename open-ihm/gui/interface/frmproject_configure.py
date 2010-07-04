#---------------------------------------------------------------------------------	
#	Filename: frmproject_configure.py
#
#	Class to create the Configure Project form - FrmConfigureProject.
#---------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

# import the Create Project Dialog design class
from gui.designs.ui_projectconfiguration import Ui_ProjectConfiguration

class FrmConfigureProject(QDialog, Ui_ProjectConfiguration):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.parent = parent
        self.setupUi(self)
        
        controller = Controller()
        self.project = controller.getProject( self.parent.projectid )
        
        # show first tab first
        self.tabProject.setCurrentIndex(0)
        
        # display project name
        self.lblProjectName.setText(self.parent.projectname)
        
        # display Available and Selected Household Characteristics
        self.displayAvailableChars("household", self.lstHouseholdAvailableChars)
        self.displayAvailableChars("person", self.lstPersonalAvailableChars)
        self.displaySelectedChars("household", self.lstHouseholdSelectedChars)
        self.displaySelectedChars("person", self.lstPersonalSelectedChars)
        
        # connect relevant signals and slots
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdHouseholdMoveAll, SIGNAL("clicked()"), self.moveAllHouseholdChars)
        self.connect(self.cmdHouseholdRemoveAll, SIGNAL("clicked()"), self.removeAllHouseholdChars)
        self.connect(self.cmdHouseholdMoveSelected, SIGNAL("clicked()"), self.moveSelectedHouseholdChars)
        self.connect(self.cmdHouseholdRemoveSelected, SIGNAL("clicked()"), self.removeSelectedHouseholdChars)
        self.connect(self.cmdPersonalMoveAll, SIGNAL("clicked()"), self.moveAllPersonalChars)
        self.connect(self.cmdPersonalRemoveAll, SIGNAL("clicked()"), self.removeAllPersonalChars)
        self.connect(self.cmdPersonalMoveSelected, SIGNAL("clicked()"), self.moveSelectedPersonalChars)
        self.connect(self.cmdPersonalRemoveSelected, SIGNAL("clicked()"), self.removeSelectedPersonalChars)
        
    def countRowsSelected(self, lstVw):
        selectedRows = self.getSelectedRows(lstVw)
        return len(selectedRows)
        
    def getSelectedRows(self, lstVw):
        
        selectedRows = []
        selectedIndexes = lstVw.selectedIndexes()
        
        for indexVal in selectedIndexes:
            if indexVal.row() not in selectedRows:
                selectedRows.append(indexVal.row())
                
        return selectedRows
        
    def getProjectCharacteristics(self, lstVw):
        chars = []
        row = 0
        while (lstVw.model().item(row,0)):
            val = lstVw.model().item(row,0).text()
            chars.append(val)
            row = row + 1
            
        return chars
        
    def displayAvailableChars(self, chartype, lstAvailable):
        ''' Retrieve and display available Household Characteristics ''' 
        controller = Controller()
        chars = controller.getGlobalHouseholdCharacteristics() if chartype == "household" else controller.getGlobalPersonCharacteristics()
        
        model = QStandardItemModel(1,2)
        
        # set model headers
        model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
        model.setHorizontalHeaderItem(1,QStandardItem('Data Type'))
        
        # add  data rows
        num = 0
        
        for characteristic in chars:
            qtCharacteristic = QStandardItem( characteristic.getName() )
            qtDataType = QStandardItem( "%i" % characteristic.getDataType() )		
            model.setItem( num, 0, qtCharacteristic )
            model.setItem( num, 1, qtDataType )
            num = num + 1
        
        lstAvailable.setModel(model)
        lstAvailable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
    def displaySelectedChars(self, chartype, lstSelected):
        ''' Retrieve and display Project Characteristics (Household or Personal)'''
        # select query to retrieve selected characteristics
        if ( chartype == "household" ):
            chars = self.project.getHouseholdCharacteristics()
        else:
            chars = self.project.getPersonCharacteristics()

        model = QStandardItemModel(1,1)

        # set model headers
        model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))

        # add  data rows
        num = 0

        for characteristic in chars:
            qtCharacteristic = QStandardItem( characteristic.getName() )	
            model.setItem( num, 0, qtCharacteristic )
            num = num + 1

        lstSelected.setModel(model)
        lstSelected.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def removeCharacteristic(self, chartype , characteristic):
        ''' removes a characteristic from a project'''
        if ( chartype == "household" ):
            self.project.removeHouseholdCharacteristic( characteristic )
        else:
            self.project.removePersonCharacteristic( characteristic )
        
    def addCharacteristic(self, chartype, characteristic, datatype):
        ''' adds a characteristic to a project'''
        if ( chartype == "household" ):
            self.project.addHouseholdCharacteristic( characteristic,  datatype )
        else:
            self.project.addPersonCharacteristic( characteristic,  datatype )
        
    def moveAllChars(self, chartype, lstAvailable, lstSelected):
        ''' Add all available household or person characteristics to Project'''
        row = 0
        while(lstAvailable.model().item(row,0)):
            characteristic 		= lstAvailable.model().item(row,0).text()
            datatype 			= lstAvailable.model().item(row,1).text()
            currentProjectChars = self.getProjectCharacteristics(lstSelected)
            if characteristic not in currentProjectChars:
                self.addCharacteristic(chartype, characteristic, datatype)
            else:
                msg = "The characteristic labelled, %s, has already been selected" % (characteristic)
                QMessageBox.information(self,"Project Configuration",msg)
            row = row + 1
        
    def removeAllChars(self, chartype, lstSelected):
        ''' remove all listed household or person characteristics from Project'''
        msg = "Are you sure you want to remove all household characteristics from this project?"
        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
        # if deletion is rejected return without deleting
        if ret == QMessageBox.No:
            return
            
        row = 0
        while(lstSelected.model().item(row,0)):
            characteristic = lstSelected.model().item(row,0).text()
            self.removeCharacteristic(chartype,characteristic)
            row = row + 1
        
    def moveSelectedChars(self, chartype, lstAvailable, lstSelected):
        ''' Add selected available household or person characteristics to Project'''
        numSelected = self.countRowsSelected(lstAvailable)
        if  numSelected != 0:
            selectedRows = self.getSelectedRows(lstAvailable)
            for row in selectedRows:
                characteristic 		= lstAvailable.model().item(row,0).text()
                datatype 			= lstAvailable.model().item(row,1).text()
                currentProjectChars = self.getProjectCharacteristics(lstSelected)
                if characteristic not in currentProjectChars:
                    self.addCharacteristic(chartype, characteristic, datatype)
                else:
                    msg = "The characteristic labelled, %s, has already been selected" % (characteristic)
                    QMessageBox.information(self,"Project Configuration",msg)
        else:
            msg = "Please select the characteristics you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
    def removeSelectedChars(self, chartype, lstSelected):
        ''' remove selected household or person characteristics from Project'''
        numSelected = self.countRowsSelected(lstSelected)
        if  numSelected != 0:
            msg = "Are you sure you want to remove the selected household characteristic(s) from this project?"
            ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
            # if deletion is rejected return without deleting
            if ret == QMessageBox.No:
                return
            selectedRows = self.getSelectedRows(lstSelected)
            for row in selectedRows:
                characteristic = lstSelected.model().item(row,0).text()
                self.removeCharacteristic(chartype, characteristic)
        else:
            msg = "Please select the characteristics you want to remove."
            QMessageBox.information(self,"Project Configuration",msg) 
            
    #-----------------------------------------------------------------------------------------------------------
    # Household Characteristics methods
    #-----------------------------------------------------------------------------------------------------------

    def moveAllHouseholdChars(self):
        ''' Add all available personal characteristics to Project'''
        self.moveAllChars( "household", self.lstHouseholdAvailableChars, self.lstHouseholdSelectedChars )
        self.displaySelectedChars( "household", self.lstHouseholdSelectedChars )
        
    def removeAllHouseholdChars(self):
        ''' remove all listed personal characteristics from Project'''
        self.removeAllChars( "household", self.lstHouseholdSelectedChars )
        self.displaySelectedChars( "household", self.lstHouseholdSelectedChars )
        
    def moveSelectedHouseholdChars(self):
        ''' Add selected available household characteristics to Project'''
        self.moveSelectedChars( "household", self.lstHouseholdAvailableChars, self.lstHouseholdSelectedChars )
        self.displaySelectedChars( "household", self.lstHouseholdSelectedChars ) 
        
    def removeSelectedHouseholdChars(self):
        ''' remove selected household characteristics from Project'''
        self.removeSelectedChars( "household", self.lstHouseholdSelectedChars )
        self.displaySelectedChars( "household", self.lstHouseholdSelectedChars )
            
    #-----------------------------------------------------------------------------------------------------------
    # Personal Characteristics methods
    #-----------------------------------------------------------------------------------------------------------

    def moveAllPersonalChars(self):
        ''' Add all available personal characteristics to Project'''
        self.moveAllChars("person", self.lstPersonalAvailableChars, self.lstPersonalSelectedChars)
        self.displaySelectedChars( "person", self.lstPersonalSelectedChars )
        
    def removeAllPersonalChars(self):
        ''' remove all listed personal characteristics from Project'''
        self.removeAllChars("person", self.lstPersonalSelectedChars)
        self.displaySelectedChars( "person", self.lstPersonalSelectedChars )
        
    def moveSelectedPersonalChars(self):
        ''' Add selected available household characteristics to Project'''
        self.moveSelectedChars("person", self.lstPersonalAvailableChars, self.lstPersonalSelectedChars)
        self.displaySelectedChars( "person", self.lstPersonalSelectedChars ) 
        
    def removeSelectedPersonalChars(self):
        ''' remove selected household characteristics from Project'''
        self.removeSelectedChars("person", self.lstPersonalSelectedChars)
        self.displaySelectedChars( "person", self.lstPersonalSelectedChars )
