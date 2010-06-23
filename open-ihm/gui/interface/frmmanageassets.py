#-------------------------------------------------------------------	
#	Filename: frmmanageassets.py
#
#	Class to create the Manage Asset Details form - FrmManageAssetDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Manage Asset Types Dialog design class
from gui.designs.ui_manageassets import Ui_ManageAssetDetails

#import GenericDBOP which has methods for managing database operations
from data.GenericDBOP import GenericDBOP

class FrmManageAssetDetails(QDialog, Ui_ManageAssetDetails):	
	''' Creates the Manage Asset Details from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent
        			
		# populate tab list controls
        	self.getAssetCategories()
        	self.getSavingsCategories()
        	self.getFoodTypes()
        	self.getLandTypes()
        	self.getTreeTypes()
        	self.getTradableGoodTypes()
        	
                #set input validator and restrict input to numeric values,
                myDblVal = QDoubleValidator(-999.99, 999999.99, 2, self.txtEnergyValue)
                myDblVal.setNotation(QDoubleValidator.StandardNotation)
                self.txtEnergyValue.setValidator(myDblVal);
      	

		self.connect(self.btnAssetsClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		#self.connect(self.listView.selectionModel(), SIGNAL("currentChanged(QModelIndex,QModelIndex)"), self.manageCategories)
                #signals for managing asset category types
		self.connect(self.btnCatSave, SIGNAL("clicked()"), self.saveCategoryType)
		self.connect(self.btnCatDelete, SIGNAL("clicked()"), self.deleteCategoryType)
		self.connect(self.categoriesListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedCategory)

		#signals for managing savings types
		self.connect(self.savingsListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedSaving)
		self.connect(self.btnCashSave, SIGNAL("clicked()"), self.saveSavingsType)
		self.connect(self.btnCashDelete, SIGNAL("clicked()"), self.deleteSavingsType)

		#signals for managing food types
		self.connect(self.foodListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedFoodItem)
		self.connect(self.btnFoodStockSave, SIGNAL("clicked()"), self.saveFoodStockType)
		self.connect(self.btnFoodStockDelete, SIGNAL("clicked()"), self.deleteFoodStockType)

		#signals for managing Land types
		self.connect(self.landListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedLandType)
		self.connect(self.btnLandSave, SIGNAL("clicked()"), self.saveLandType)
		self.connect(self.btnLandDelete, SIGNAL("clicked()"), self.deleteLandType)

		#signals for managing Land types
		self.connect(self.treeListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedTreeType)
		self.connect(self.btnTreeSave, SIGNAL("clicked()"), self.saveTreeType)
		self.connect(self.btnTreeDelete, SIGNAL("clicked()"), self.deleteTreeType)

		#signals for managing Tradable Goods types
		self.connect(self.tradableGoodsListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedTradableGoodType)
		self.connect(self.btnTGoodSave, SIGNAL("clicked()"), self.saveTradableGoodType)
		self.connect(self.btnTGoodDelete, SIGNAL("clicked()"), self.deleteTradableGoodType)
		

		
	#Begin block of methods for managing Asset Categories 	
	def getAssetCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT assettype FROM assettypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtAssetType = QStandardItem( "%s" % row[0])
            		qtAssetType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtAssetType )
            		num = num + 1
                        		
        	self.categoriesListView.setModel(model)
		self.categoriesListView.show()

        def pickSelectedCategory(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.categoriesListView.model().item(index.row(),0).text()
                self.txtAssetCategories.setText(selectedItem)
                
        def saveCategoryType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	categorytype = self.txtAssetCategories.text()		
        	
		# check if record exists
		query = '''SELECT assettype FROM assettypes WHERE assettype='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO assettypes(assettype) 
                     		VALUES('%s')''' % (categorytype)
		else:
			query = '''UPDATE assettypes SET assettype='%s'	WHERE assettype='%s' ''' % (categorytype, categorytype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()                
                
	def deleteCategoryType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	categorytype = self.txtAssetCategories.text()		
        	
		# check if record exists
		query = '''SELECT assettype FROM assettypes WHERE assettype='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM assettypes WHERE assettype='%s' ''' % (categorytype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Asset Categories


	#Begin block of methods for managing Savings Categories 
	def getSavingsCategories(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Savings Categories
        	query = '''SELECT savingscategory FROM savingscategories'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO savingscategories(savingscategory) 
                     		VALUES('%s')''' % (categorytype)
		else:
			query = '''UPDATE savingscategories SET savingscategory='%s'	WHERE assettype='%s' ''' % (categorytype, categorytype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()
                                
	def deleteSavingsType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	categorytype = self.txtSavingCategories.text()		
        	
		# check if record exists
		query = '''SELECT savingscategory FROM savingscategories WHERE savingscategory='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM savingscategories WHERE savingscategory='%s' ''' % (categorytype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Savings Categories

        #Begin block of methods for managing Foodstock details 
	def getFoodTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT foodtype FROM setup_crops'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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
                
                selectedFoodItem = self.foodListView.model().item(index.row(),0).text()
                self.txtFoodStockType.setText(selectedFoodItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, measuringunit FROM setup_crops WHERE foodtype='%s' ''' % (selectedFoodItem)

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtEnergyValue.setText(str(kcalValue))
                self.txtMeasuringUnit.setText(unitOfMeasure)

        def saveFoodStockType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.txtFoodStockType.text()
        	myenergyvalue = self.txtEnergyValue.text()
        	unitofmeasure = self.txtMeasuringUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, measuringunit FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_crops(foodtype, energyvalueperunit, measuringunit) 
                     		VALUES('%s',%s,'%s')''' % (myfoodtype, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_crops SET foodtype='%s', energyvalueperunit=%s, measuringunit='%s'
                     		WHERE foodtype='%s' ''' % (myfoodtype, myenergyvalue, unitofmeasure, myfoodtype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()
                                
	def deleteFoodStockType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myfoodtype = self.txtFoodStockType.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, measuringunit FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Food Stocks

        #Begin block of methods for managing Land details 
	def getLandTypes(self):
                '''Get pre-existing land types from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT landtype FROM setup_landtypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
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
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_landtypes(landtype, unitofmeasure) 
                     		VALUES('%s','%s')''' % (mylandtype, myunitofmeasure)
		else:
			query = '''UPDATE setup_landtypes SET landtype='%s', unitofmeasure='%s'
                     		WHERE landtype='%s' ''' % (mylandtype, myunitofmeasure, mylandtype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()
                                
	def deleteLandType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mylandtype = self.txtLandType.text()		
        	
		# check if record exists
		query = '''SELECT landtype, unitofmeasure FROM setup_landtypes WHERE landtype='%s' ''' % (mylandtype)
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_landtypes WHERE landtype='%s' ''' % (mylandtype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Land Type', "Record not found")
        #End block of methods for managing Land details


        #Begin block of methods for managing Tree details 
	def getTreeTypes(self):
                '''Get pre-existing tree types from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT treetype FROM setup_treetypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
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
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

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
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()
                                
	def deleteTreeType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mytreetype = self.txtTreeType.text()		
        	
		# check if record exists
		query = '''SELECT treetype, measuringunit FROM setup_treetypes WHERE treetype='%s' ''' % (mytreetype)
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_treetypes WHERE treetype='%s' ''' % (mytreetype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Tree Type', "Record not found")
        #End block of methods for managing Tree details

        #Begin block of methods for managing TradableGood details 
        def getTradableGoodTypes(self):
                       
                '''Get pre-existing tree types from database and populate categories list'''
                # select query to retrieve Food types
                query = '''SELECT tradablegoodtype FROM setup_tradablegoods'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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

                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
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
		
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()

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
                temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
                #refresh categories list
                #self.getCategories()
                                
        def deleteTradableGoodType(self):
                ''' Deletes record from database '''

                # get the data entered by user
                mytradablegood = self.txtTradableGoodType.text()		
        	
                # check if record exists
                query = '''SELECT tradablegoodtype, unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)
		
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
                numrows = 0		
                for row in recordset:
                        numrows = numrows + 1

                if numrows <> 0:
			
                        query = '''DELETE FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)

                        # execute query and commit changes
                        temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
                        #self.cmbKCalories.clear()
			
                        #refresh categories list
                        self.getAssetCategories()			
			
                else:
                        QMessageBox.information(self, 'Delete TradableGood Type', "Record not found")
                #End block of methods for managing TradableGood details


    
