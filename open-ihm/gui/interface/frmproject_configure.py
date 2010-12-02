#---------------------------------------------------------------------------------	
#	Filename: frmproject_configure.py
#
#	Class to create the Configure Project form - FrmConfigureProject.
#---------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 
from data.controller import Controller

# import the Create Project Dialog design class
from gui.designs.ui_projectconfiguration import Ui_ProjectConfiguration

class FrmConfigureProject(QDialog, Ui_ProjectConfiguration):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.parent = parent
        self.dietid = 0
        self.setupUi(self)
        
        self.config = Config.dbinfo().copy()
        
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
        self.listDiets()
        self.getCropTypes()
        
        # connect relevant signals and slots
        self.connect(self.tblDiets, SIGNAL("clicked(QModelIndex)"), self.showSelectedDiet)
        self.connect(self.cmbFoodItem, SIGNAL("currentIndexChanged(int)"), self.displayUnitOfMeasure)
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdHouseholdMoveAll, SIGNAL("clicked()"), self.moveAllHouseholdChars)
        self.connect(self.cmdHouseholdRemoveAll, SIGNAL("clicked()"), self.removeAllHouseholdChars)
        self.connect(self.cmdHouseholdMoveSelected, SIGNAL("clicked()"), self.moveSelectedHouseholdChars)
        self.connect(self.cmdHouseholdRemoveSelected, SIGNAL("clicked()"), self.removeSelectedHouseholdChars)
        self.connect(self.cmdPersonalMoveAll, SIGNAL("clicked()"), self.moveAllPersonalChars)
        self.connect(self.cmdPersonalRemoveAll, SIGNAL("clicked()"), self.removeAllPersonalChars)
        self.connect(self.cmdPersonalMoveSelected, SIGNAL("clicked()"), self.moveSelectedPersonalChars)
        self.connect(self.cmdPersonalRemoveSelected, SIGNAL("clicked()"), self.removeSelectedPersonalChars)
        self.connect(self.cmdSaveDiet, SIGNAL("clicked()"), self.saveDiet)
        self.connect(self.cmdDelDiet, SIGNAL("clicked()"), self.delDiets)
     
    def getCurrentRow(self, tblVw):
         indexVal = tblVw.currentIndex()
         return indexVal.row()
         
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
        
    #--------------------------------------------------------------------------------------------------------------------------
    #  Standard of Living
    #-------------------------------------------------------------------------------------------------------------------------
         
    def getExpenseItems(self):
         ''' Retrieve Expense Items and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT foodtype, measuringunit FROM setup_crops'''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             croptype = row[0]
             measuringunit = row[1]
             self.cmbFoodItem.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cmbFoodItem.itemData( self.cmbFoodItem.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
    
    def displayStandardOfLiving(self):
         ''' List available currencies '''
         # select query to retrieve currencies
         query = '''SELECT id, fooditem, unitofmeasure, percentage, priceperunit FROM diet '''
         
         # retrieve and display members
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()
         
         cursor.execute(query)
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Id.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Food Item'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit Of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Percentage'))
         model.setHorizontalHeaderItem(4,QStandardItem('Price per Unit'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
             qtID = QStandardItem("%i" % row[0])
             qtID.setTextAlignment( Qt.AlignCenter )
             qtFoodItem = QStandardItem( row[1] )	
             qtUnit = QStandardItem(row[2] )
             
             qtPercentage = QStandardItem( "%.2f" %   row[3] )
             qtPrice = QStandardItem( "%.2f" %   row[4] )
             			
             model.setItem( num, 0, qtID )
             model.setItem( num, 1, qtFoodItem )
             model.setItem( num, 2, qtUnit )
             model.setItem( num, 3, qtPercentage )
             model.setItem( num, 4, qtPrice )
             num = num + 1
             
         cursor.close()   
         db.close()
         
         self.tblDiets.setModel(model)
         self.tblDiets.resizeColumnsToContents()
         self.tblDiets.hideColumn(0)
         self.tblDiets.show()
         
    def showStandardOfLivingItem(self, index):
         ''' show details of a selected currency for editing '''
         self.dietid = self.tblDiets.model().item(index.row(),0).text()
         fooditem = self.tblDiets.model().item(index.row(),1).text()
         unitofmeasure = self.tblDiets.model().item(index.row(),2).text()
         percentage = self.tblDiets.model().item(index.row(),3).text()
         priceperunit = self.tblDiets.model().item(index.row(),4).text()
         
         self.cmbFoodItem.setCurrentIndex(self.cmbFoodItem.findText( fooditem ))
         self.txtUnitOfMeasure.setText(unitofmeasure)
         self.txtPercentage.setText(percentage)
         self.txtUnitPrice.setText(priceperunit)
         
    def saveStandardOfLivingItem(self):
         ''' Save the currency details of a currency being added or edited '''
         pid = self.parent.projectid
         fooditem = self.cmbFoodItem.currentText()
         unitofmeasure = self.txtUnitOfMeasure.text()
         percentage = self.txtPercentage.text()
         priceperunit = self.txtUnitPrice.text()
         
         db = data.mysql.connector.Connect(**self.config)
         
         # create INSERT or UPDATE query
         if (self.dietid == 0):
             query = '''INSERT INTO diet (pid, fooditem,unitofmeasure,percentage, priceperunit )
                         VALUES(%s,'%s','%s',%s,%s) ''' % ( pid, fooditem,unitofmeasure,percentage, priceperunit  )
         else:
             query = ''' UPDATE diet SET fooditem='%s', unitofmeasure='%s', percentage=%s, priceperunit=%s
                         WHERE id=%s AND pid=%s ''' % ( fooditem,unitofmeasure,percentage, priceperunit, self.dietid, pid)
         
         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()
         
         # close database connection
         cursor.close()
         db.close()
         
         # clear text boxes and refresh list
         self.txtPercentage.setText("")
         self.txtUnitPrice.setText("")
         self.dietid = 0
         self.listDiets()
         
    def delStandardOfLivingItems(self):
         ''' Delete a selected currencies '''
         numSelected = self.countRowsSelected(self.tblDiets)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected diet item?"
             else:
                 msg = "Are you sure you want to delete the selected diet items?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected currencies
             selectedRows = self.getSelectedRows(self.tblDiets)
             selectedIds = []
             for row in selectedRows:
                 selectedIds.append( self.tblDiets.model().item(row,0).text() )
             # delete selected currencies
             
             db = data.mysql.connector.Connect(**self.config)
             cursor =  db.cursor()
             
             for dietid in selectedIds:
                 query = '''DELETE FROM diet WHERE id='%s' ''' % (dietid)	
                 cursor.execute(query)
                 db.commit()
    
             # close database connection
             cursor.close()
             db.close()
             
             self.dietid = 0
             self.listDiets()

         else:
             QMessageBox.information(self,"Delete Diet Items","Please select the rows containing diet items to be deleted.")
       
        
    #--------------------------------------------------------------------------------------------------------------------------
    #  Diets
    #-------------------------------------------------------------------------------------------------------------------------
    
    def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cmbFoodItem.itemData( self.cmbFoodItem.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
         
    def getCropTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT foodtype, measuringunit FROM setup_crops'''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             croptype = row[0]
             measuringunit = row[1]
             self.cmbFoodItem.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cmbFoodItem.itemData( self.cmbFoodItem.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
    
    def listDiets(self):
         ''' List available currencies '''
         # select query to retrieve currencies
         query = '''SELECT id, fooditem, unitofmeasure, percentage, priceperunit FROM diet '''
         
         # retrieve and display members
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()
         
         cursor.execute(query)
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Id.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Food Item'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit Of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Percentage'))
         model.setHorizontalHeaderItem(4,QStandardItem('Price per Unit'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
             qtID = QStandardItem("%i" % row[0])
             qtID.setTextAlignment( Qt.AlignCenter )
             qtFoodItem = QStandardItem( row[1] )	
             qtUnit = QStandardItem(row[2] )
             
             qtPercentage = QStandardItem( "%.2f" %   row[3] )
             qtPrice = QStandardItem( "%.2f" %   row[4] )
             			
             model.setItem( num, 0, qtID )
             model.setItem( num, 1, qtFoodItem )
             model.setItem( num, 2, qtUnit )
             model.setItem( num, 3, qtPercentage )
             model.setItem( num, 4, qtPrice )
             num = num + 1
             
         cursor.close()   
         db.close()
         
         self.tblDiets.setModel(model)
         self.tblDiets.resizeColumnsToContents()
         self.tblDiets.hideColumn(0)
         self.tblDiets.show()
         
    def showSelectedDiet(self, index):
         ''' show details of a selected currency for editing '''
         self.dietid = self.tblDiets.model().item(index.row(),0).text()
         fooditem = self.tblDiets.model().item(index.row(),1).text()
         unitofmeasure = self.tblDiets.model().item(index.row(),2).text()
         percentage = self.tblDiets.model().item(index.row(),3).text()
         priceperunit = self.tblDiets.model().item(index.row(),4).text()
         
         self.cmbFoodItem.setCurrentIndex(self.cmbFoodItem.findText( fooditem ))
         self.txtUnitOfMeasure.setText(unitofmeasure)
         self.txtPercentage.setText(percentage)
         self.txtUnitPrice.setText(priceperunit)
         
    def saveDiet(self):
         ''' Save the currency details of a currency being added or edited '''
         pid = self.parent.projectid
         fooditem = self.cmbFoodItem.currentText()
         unitofmeasure = self.txtUnitOfMeasure.text()
         percentage = self.txtPercentage.text()
         priceperunit = self.txtUnitPrice.text()
         
         db = data.mysql.connector.Connect(**self.config)
         
         # create INSERT or UPDATE query
         if (self.dietid == 0):
             query = '''INSERT INTO diet (pid, fooditem,unitofmeasure,percentage, priceperunit )
                         VALUES(%s,'%s','%s',%s,%s) ''' % ( pid, fooditem,unitofmeasure,percentage, priceperunit  )
         else:
             query = ''' UPDATE diet SET fooditem='%s', unitofmeasure='%s', percentage=%s, priceperunit=%s
                         WHERE id=%s AND pid=%s ''' % ( fooditem,unitofmeasure,percentage, priceperunit, self.dietid, pid)
         
         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()
         
         # close database connection
         cursor.close()
         db.close()
         
         # clear text boxes and refresh list
         self.txtPercentage.setText("")
         self.txtUnitPrice.setText("")
         self.dietid = 0
         self.listDiets()
         
    def delDiets(self):
         ''' Delete a selected currencies '''
         numSelected = self.countRowsSelected(self.tblDiets)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected diet item?"
             else:
                 msg = "Are you sure you want to delete the selected diet items?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected currencies
             selectedRows = self.getSelectedRows(self.tblDiets)
             selectedIds = []
             for row in selectedRows:
                 selectedIds.append( self.tblDiets.model().item(row,0).text() )
             # delete selected currencies
             
             db = data.mysql.connector.Connect(**self.config)
             cursor =  db.cursor()
             
             for dietid in selectedIds:
                 query = '''DELETE FROM diet WHERE id='%s' ''' % (dietid)	
                 cursor.execute(query)
                 db.commit()
    
             # close database connection
             cursor.close()
             db.close()
             
             self.dietid = 0
             self.listDiets()

         else:
             QMessageBox.information(self,"Delete Diet Items","Please select the rows containing diet items to be deleted.")
         
    #--------------------------------------------------------------------------------------------------------------------------
    #  Characteristics
    #-------------------------------------------------------------------------------------------------------------------------
        
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
