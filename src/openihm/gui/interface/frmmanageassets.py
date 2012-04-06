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

# import the Manage Asset Types Dialog design class
Ui_ManageAssetDetails, base_class = uic.loadUiType("gui/designs/ui_manageassets.ui")


from mixins import MDIDialogMixin, MySQLMixin

class FrmManageAssetDetails(QDialog, Ui_ManageAssetDetails, MySQLMixin, MDIDialogMixin):	
	''' Creates the Manage Asset Details from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent
        			
		# populate tab list controls
        	self.getSavingsCategories()
        	self.getFoodTypes()
        	self.getLandTypes()
        	self.getTreeTypes()
        	self.getTradableGoodTypes()
        	self.getLivestockTypes()
        	
                #set input validator and restrict input to numeric values,
                #myIntVal = QIntValidator(0, 10000, self.txtEnergyValue)
                #self.txtEnergyValue.setValidator(myIntVal);
                #self.txtLivestockEnergyValue.setValidator(myIntVal)

	#Begin block of methods for managing Savings Categories 
	def getSavingsCategories(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Savings Categories
        	query = '''SELECT savingscategory FROM savingscategories'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtSavingType = QStandardItem( "%s" % row[0])
            		qtSavingType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtSavingType )
            		num = num + 1
                        		
        	self.savingsListView.setModel(model)
		self.savingsListView.show()	

        def pickSelectedSaving(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.savingsListView.model().item(index.row(),0).text()
                self.txtSavingCategories.setText(selectedItem)

        def saveSavingsType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	categorytype = self.txtSavingCategories.text()		
        	
		# check if record exists
		query = '''SELECT savingscategory FROM savingscategories WHERE savingscategory='%s' ''' % (categorytype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO savingscategories(savingscategory) 
                     		VALUES('%s')''' % (categorytype)
		else:
			query = '''UPDATE savingscategories SET savingscategory='%s'	WHERE assettype='%s' ''' % (categorytype, categorytype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
                self.txtSavingCategories.clear()
                self.getSavingsCategories()
                                
	def deleteSavingsType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	categorytype = self.txtSavingCategories.text()		
        	
		# check if record exists
		query = '''SELECT savingscategory FROM savingscategories WHERE savingscategory='%s' ''' % (categorytype)    
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Savings Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
                                
                                query = '''DELETE FROM savingscategories WHERE savingscategory='%s' ''' % (categorytype)

                                # execute query and commit changes
				self.executeUpdateQuery(query)

                                self.txtSavingCategories.clear()		
                                #refresh categories list
                                self.getSavingsCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
		
        #End block of methods for managing Savings Categories

        #Begin block of methods for managing Foodstock details 
	def getFoodTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT foodtype FROM setup_crops'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.foodListView.setModel(model)
		self.foodListView.show()	

        def pickSelectedFoodItem(self,index):
                '''get selected item and populate categories textbox'''
                #self.txtEnergyValue.setText("")
                self.txtMeasuringUnit.setText("")
                
                selectedFoodItem = self.foodListView.model().item(index.row(),0).text()
                self.txtFoodStockType.setText(selectedFoodItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT measuringunit FROM setup_crops WHERE foodtype='%s' ''' % (selectedFoodItem)

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
                        #kcalValue = row[0]
			unitOfMeasure = row[0]

		'''if kcalValue:
                        self.txtEnergyValue.setText(str(kcalValue))'''
                if unitOfMeasure:
                        self.txtMeasuringUnit.setText(unitOfMeasure)

        def saveFoodStockType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.txtFoodStockType.text()
        	#myenergyvalue = self.txtEnergyValue.text()
        	unitofmeasure = self.txtMeasuringUnit.text()
                        	
		# check if record exists
		query = '''SELECT * FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_crops(foodtype, measuringunit) 
                     		VALUES('%s','%s')''' % (myfoodtype, unitofmeasure)
		else:
			query = '''UPDATE setup_crops SET foodtype='%s', measuringunit='%s'
                     		WHERE foodtype='%s' ''' % (myfoodtype, unitofmeasure, myfoodtype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
                self.getFoodTypes()
                self.txtFoodStockType.clear()
                self.txtMeasuringUnit.clear()
                                
	def deleteFoodStockType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myfoodtype = self.txtFoodStockType.text()		
        	
		# check if record exists
		query = '''SELECT * FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Food Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)

                                # execute query and commit changes
				self.executeUpdateQuery(query)

                                self.txtFoodStockType.clear()
                                #self.txtEnergyValue.clear()
                                self.txtMeasuringUnit.clear()
                                #refresh foodtype list
                                self.getFoodTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
		
        #End block of methods for managing Food Stocks

        #Begin block of methods for managing Land details 
	def getLandTypes(self):
                '''Get pre-existing land types from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT landtype FROM setup_landtypes'''
        	
                recordset = self.executeResultsQuery(query)

		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtLandType = QStandardItem( "%s" % row[0])
            		qtLandType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtLandType )
            		num = num + 1
                        		
        	self.landListView.setModel(model)
		self.landListView.show()	

        def pickSelectedLandType(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedLandType = self.landListView.model().item(index.row(),0).text()
                self.txtLandType.setText(selectedLandType)
                #select query to retrieve measuring unit for selected land type
        	query = '''SELECT unitofmeasure FROM setup_landtypes WHERE landtype='%s' ''' % (selectedLandType)

                recordset = self.executeResultsQuery(query)
		for row in recordset:
                        unitOfMeasure = row[0]

		self.txtLandMeasuringUnit.setText(unitOfMeasure)

        def saveLandType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	mylandtype = self.txtLandType.text()
        	myunitofmeasure = self.txtLandMeasuringUnit.text()
                        	
		# check if record exists
		query = '''SELECT landtype, unitofmeasure FROM setup_landtypes WHERE landtype='%s' ''' % (mylandtype)    
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_landtypes(landtype, unitofmeasure) 
                     		VALUES('%s','%s')''' % (mylandtype, myunitofmeasure)
		else:
			query = '''UPDATE setup_landtypes SET landtype='%s', unitofmeasure='%s'
                     		WHERE landtype='%s' ''' % (mylandtype, myunitofmeasure, mylandtype)
    
		self.executeUpdateQuery(query)
		self.txtLandType.clear()
                self.txtLandMeasuringUnit.clear()
                self.getLandTypes()
		#refresh categories list
		#self.getCategories()
                                
	def deleteLandType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mylandtype = self.txtLandType.text()		
        	
		# check if record exists
		query = '''SELECT landtype, unitofmeasure FROM setup_landtypes WHERE landtype='%s' ''' % (mylandtype)
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Land Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_landtypes WHERE landtype='%s' ''' % (mylandtype)

                                # execute query and commit changes
				self.executeUpdateQuery(query)
                                self.txtLandType.clear()
                                self.txtLandMeasuringUnit.clear()

                                self.getLandTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Land Type', "Record not found")
		
        #End block of methods for managing Land details


        #Begin block of methods for managing Tree details 
	def getTreeTypes(self):
                '''Get pre-existing tree types from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT treetype FROM setup_treetypes'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtTreeType = QStandardItem( "%s" % row[0])
            		qtTreeType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtTreeType )
            		num = num + 1
                        		
        	self.treeListView.setModel(model)
		self.treeListView.show()	

        def pickSelectedTreeType(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedTreeType = self.treeListView.model().item(index.row(),0).text()
                self.txtTreeType.setText(selectedTreeType)
                #select query to retrieve measuring unit for selected tree type
        	query = '''SELECT measuringunit FROM setup_treetypes WHERE treetype='%s' ''' % (selectedTreeType)

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
                        unitOfMeasure = row[0]

		self.txtTreeMeasuringUnit.setText(unitOfMeasure)

        def saveTreeType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	mytreetype = self.txtTreeType.text()
        	mymeasuringunit = self.txtTreeMeasuringUnit.text()
                        	
		# check if record exists
		query = '''SELECT treetype, measuringunit FROM setup_treetypes WHERE treetype='%s' ''' % (mytreetype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_treetypes(treetype, measuringunit) 
                     		VALUES('%s','%s')''' % (mytreetype, mymeasuringunit)
		else:
			query = '''UPDATE setup_treetypes SET treetype='%s', measuringunit='%s'
                     		WHERE treetype='%s' ''' % (mytreetype, mymeasuringunit, mytreetype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
                self.txtTreeType.clear()
                self.txtTreeMeasuringUnit.clear()
                self.getTreeTypes()
                                
	def deleteTreeType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mytreetype = self.txtTreeType.text()		
        	
		# check if record exists
		query = '''SELECT treetype, measuringunit FROM setup_treetypes WHERE treetype='%s' ''' % (mytreetype)
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Tree Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_treetypes WHERE treetype='%s' ''' % (mytreetype)

                                # execute query and commit changes
				self.executeUpdateQuery(query)

                                self.txtTreeType.clear()
                                self.txtTreeMeasuringUnit.clear()
                                #refresh categories list
                                self.getTreeTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Tree Type', "Record not found")
		
        #End block of methods for managing Tree details

        #Begin block of methods for managing TradableGood details 
        def getTradableGoodTypes(self):
                       
                '''Get pre-existing tree types from database and populate categories list'''
                # select query to retrieve Food types
                query = '''SELECT tradablegoodtype FROM setup_tradablegoods'''
        	
                recordset = self.executeResultsQuery(query)
				
                model = QStandardItemModel()
                num = 0

                for row in recordset:
                        qtTradableGoodType = QStandardItem( "%s" % row[0])
                        qtTradableGoodType.setTextAlignment( Qt.AlignLeft )
                        model.setItem( num, 0, qtTradableGoodType )
                        num = num + 1
                        		
                self.tradableGoodsListView.setModel(model)
                self.tradableGoodsListView.show()	

        def pickSelectedTradableGoodType(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedTradableGoodType = self.tradableGoodsListView.model().item(index.row(),0).text()
                self.txtTradableGoodType.setText(selectedTradableGoodType)
                #select query to retrieve measuring unit for selected tree type
                query = '''SELECT unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (selectedTradableGoodType)

                recordset = self.executeResultsQuery(query)
                for row in recordset:
                    unitOfMeasure = row[0]

                self.txtTradableGoodMeasuringUnit.setText(unitOfMeasure)

        def saveTradableGoodType(self):
                ''' Saves newly created data to database '''

                # get the data entered by user
                mytradablegood = self.txtTradableGoodType.text()
                mymeasuringunit = self.txtTradableGoodMeasuringUnit.text()
                        	
                # check if record exists
                query = '''SELECT tradablegoodtype, unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)    
		
                recordset = self.executeResultsQuery(query)

                numrows = 0		
                for row in recordset:
                    numrows = numrows + 1
				      	
                if numrows == 0:
			
                        query = '''INSERT INTO setup_tradablegoods(tradablegoodtype, unitofmeasure) 
                     		VALUES('%s','%s')''' % (mytradablegood, mymeasuringunit)
                else:
                        query = '''UPDATE setup_tradablegoods SET tradablegoodtype='%s', unitofmeasure='%s'
                     		WHERE tradablegoodtype='%s' ''' % (mytradablegood, mymeasuringunit, mytradablegood)
    
                # execute query and commit changes
		self.executeUpdateQuery(query)
		self.txtTradableGoodType.clear()
                self.txtTradableGoodMeasuringUnit.clear()
                self.getTradableGoodTypes()
                                
        def deleteTradableGoodType(self):
                ''' Deletes record from database '''

                # get the data entered by user
                mytradablegood = self.txtTradableGoodType.text()		
        	
                # check if record exists
                query = '''SELECT tradablegoodtype, unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)
		
                recordset = self.executeResultsQuery(query)
                numrows = 0		
                for row in recordset:
                        numrows = numrows + 1

                if numrows <> 0:
			msg = "Are sure sure you want to delete this Tradable Good Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
                                query = '''DELETE FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)

                                # execute query and commit changes
				self.executeUpdateQuery(query)
			
                                self.txtTradableGoodType.clear()
                                self.txtTradableGoodMeasuringUnit.clear()
			
                                #refresh categories list
                                self.getTradableGoodTypes()			
			
                else:
                        QMessageBox.information(self, 'Delete TradableGood Type', "Record not found")
                
                #End block of methods for managing TradableGood details

        #Begin block of methods for managing Livestock details 
	def getLivestockTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT incomesource FROM setup_livestock'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.livestockListView.setModel(model)
		self.livestockListView.show()	

        def pickSelectedLivestockItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedLivestockItem = self.livestockListView.model().item(index.row(),0).text()
                self.txtLivestockPType.setText(selectedLivestockItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (selectedLivestockItem)

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		#self.txtLivestockEnergyValue.setText(str(kcalValue))
                self.txtLivestockUnit.setText(unitOfMeasure)

        def saveLivestockType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()
        	#myenergyvalue = self.txtLivestockEnergyValue.text()
        	unitofmeasure = self.txtLivestockUnit.text()
                        	
		# check if record exists
		query = '''SELECT unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)    
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_livestock(incomesource, unitofmeasure) 
                     		VALUES('%s','%s')''' % (myincomesource, unitofmeasure)
		else:
			query = '''UPDATE setup_livestock SET incomesource='%s', unitofmeasure='%s'
                     		WHERE incomesource='%s' ''' % (myincomesource, unitofmeasure, myincomesource)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
		#refresh categories list
                self.txtLivestockPType.clear()
                self.txtLivestockUnit.clear()
		self.getLivestockTypes()
                                
	def deleteLivestockType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()		
        	
		# check if record exists
		query = '''SELECT unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)    
		
                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Livestock Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)

                                # execute query and commit changes
				self.executeUpdateQuery(query)
				self.txtLivestockPType.clear()
                                self.txtLivestockUnit.clear()
                                #refresh categories list
                                self.getLivestockTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Livestock Types


    
