#-------------------------------------------------------------------	
#	Filename: frmincomesourcedetails.py
#
#	Class to create the Manage Income Types form - FrmIncomeSourceDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Manage Income Dialog design class
from gui.designs.ui_manageincomedetails import Ui_ManageIncome

#import GenericDBOP which has methods for managing database operations
from data.GenericDBOP import GenericDBOP

class FrmIncomeSourceDetails(QDialog, Ui_ManageIncome):	
	''' Creates the Manage Income Source Details from. Uses the design class
		in gui.designs.ui_manageincomedetails. '''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

		self.getCropTypes()
		self.getEmploymentCategories()
		self.getWildFoodTypes()
		self.getLivestockTypes()
		self.getTransferSourceCategories()
		self.getTransferTypes()

		# connect relevant signals and slots
		self.connect(self.btnManageIncomeClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		#signals for managing food types
		self.connect(self.cropListView, SIGNAL("clicked(QModelIndex)"), self.pickselectedCropItem)
		self.connect(self.btnCropSave, SIGNAL("clicked()"), self.saveCropType)
		self.connect(self.btnCropDelete, SIGNAL("clicked()"), self.deleteCropType)

		#signals for managing employment types
		self.connect(self.employmentListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedEmployment)
		self.connect(self.btnEmplomentTypeSave, SIGNAL("clicked()"), self.saveEmploymentType)
		self.connect(self.btnEmplomentTypeDelete, SIGNAL("clicked()"), self.deleteEmploymentType)

		#signals for managing wild foods
		self.connect(self.wildFoodsListView, SIGNAL("clicked(QModelIndex)"), self.pickselectedWildFoodItem)
		self.connect(self.btnWildFoodSave, SIGNAL("clicked()"), self.saveWildFoodType)
		self.connect(self.btnWildFoodDelete, SIGNAL("clicked()"), self.deleteWildFoodType)

		#signals for managing Livestock
		self.connect(self.livestockListView, SIGNAL("clicked(QModelIndex)"), self.pickselectedLivestockItem)
		self.connect(self.btnLivestockSave, SIGNAL("clicked()"), self.saveLivestockType)
		self.connect(self.btnLivestockDelete, SIGNAL("clicked()"), self.deleteLivestockType)

		#signals for managing trasfer Sources
		self.connect(self.transferSourcesListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedTransferSource)
		self.connect(self.btnTransferSourcesSave, SIGNAL("clicked()"), self.saveTransferSourceType)
		self.connect(self.btnTransferSourcesDelete, SIGNAL("clicked()"), self.deleteTransferSourceType)

		#signals for managing assistance types
		self.connect(self.transferTypesListView, SIGNAL("clicked(QModelIndex)"), self.pickSelectedTransfer)
		self.connect(self.btnTransferTypeSave, SIGNAL("clicked()"), self.saveTransferType)
		self.connect(self.btnTransferTypeDelete, SIGNAL("clicked()"), self.deleteTransferType)


        #Begin block of methods for managing Foodstock details 
	def getCropTypes(self):
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
                        		
        	self.cropListView.setModel(model)
		self.cropListView.show()	

        def pickselectedCropItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedCropItem = self.cropListView.model().item(index.row(),0).text()
                self.txtCropTypeName.setText(selectedCropItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, measuringunit FROM setup_crops WHERE foodtype='%s' ''' % (selectedCropItem)

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtEnergyValue.setText(str(kcalValue))
                self.txtMeasuringUnit.setText(unitOfMeasure)

        def saveCropType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.txtCropTypeName.text()
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
		self.getCropTypes()
                                
	def deleteCropType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myfoodtype = self.txtCropTypeName.text()		
        	
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
			self.getCropTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Crop Types

	#Begin block of methods for managing Employment Categories 	
	def getEmploymentCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT incomesource FROM setup_employment'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtEmploymentType = QStandardItem( "%s" % row[0])
            		qtEmploymentType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtEmploymentType )
            		num = num + 1
                        		
        	self.employmentListView.setModel(model)
		self.employmentListView.show()

        def pickSelectedEmployment(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.employmentListView.model().item(index.row(),0).text()
                self.txtEmploymentType.setText(selectedItem)
                
        def saveEmploymentType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	employment = self.txtEmploymentType.text()		
        	
		# check if record exists
		query = '''SELECT incomesource FROM setup_employment WHERE incomesource='%s' ''' % (employment)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_employment(incomesource) 
                     		VALUES('%s')''' % (employment)
		else:
			query = '''UPDATE setup_employment SET incomesource='%s'	WHERE incomesource='%s' ''' % (employment, employment)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		self.getEmploymentCategories()               
                
	def deleteEmploymentType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	employment = self.txtEmploymentType.text()		
        	
		# check if record exists
		query = '''SELECT incomesource FROM setup_employment WHERE incomesource='%s' ''' % (employment)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_employment WHERE incomesource='%s' ''' % (employment)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getEmploymentCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Employment Categories


        #Begin block of methods for managing Wild Foods details 
	def getWildFoodTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT incomesource FROM setup_wildfoods'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.wildFoodsListView.setModel(model)
		self.wildFoodsListView.show()	

        def pickselectedWildFoodItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedWildFoodItem = self.wildFoodsListView.model().item(index.row(),0).text()
                self.txtWildFoodType.setText(selectedWildFoodItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_wildfoods WHERE incomesource='%s' ''' % (selectedWildFoodItem)

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtWildFoodEnergyValue.setText(str(kcalValue))
                self.txtWildFoodUnit.setText(unitOfMeasure)

        def saveWildFoodType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myincomesource = self.txtWildFoodType.text()
        	myenergyvalue = self.txtWildFoodEnergyValue.text()
        	unitofmeasure = self.txtWildFoodUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_wildfoods WHERE incomesource='%s' ''' % (myincomesource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_wildfoods(incomesource, energyvalueperunit, unitofmeasure) 
                     		VALUES('%s',%s,'%s')''' % (myincomesource, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_wildfoods SET incomesource='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     		WHERE incomesource='%s' ''' % (myincomesource, myenergyvalue, unitofmeasure, myincomesource)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		self.getWildFoodTypes()
                                
	def deleteWildFoodType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myincomesource = self.txtWildFoodType.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_wildfoods WHERE incomesource='%s' ''' % (myincomesource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_wildfoods WHERE incomesource='%s' ''' % (myincomesource)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getWildFoodTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing WildFood Types
			

        #Begin block of methods for managing Livestock details 
	def getLivestockTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT incomesource FROM setup_livestock'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.livestockListView.setModel(model)
		self.livestockListView.show()	

        def pickselectedLivestockItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedLivestockItem = self.livestockListView.model().item(index.row(),0).text()
                self.txtLivestockPType.setText(selectedLivestockItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (selectedLivestockItem)

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtLivestockEnergyValue.setText(str(kcalValue))
                self.txtLivestockUnit.setText(unitOfMeasure)

        def saveLivestockType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()
        	myenergyvalue = self.txtLivestockEnergyValue.text()
        	unitofmeasure = self.txtLivestockUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_livestock(incomesource, energyvalueperunit, unitofmeasure) 
                     		VALUES('%s',%s,'%s')''' % (myincomesource, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_livestock SET incomesource='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     		WHERE incomesource='%s' ''' % (myincomesource, myenergyvalue, unitofmeasure, myincomesource)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		self.getLivestockTypes()
                                
	def deleteLivestockType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_livestock WHERE incomesource='%s' ''' % (myincomesource)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getLivestockTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Livestock Types

	#Begin block of methods for managing Transfer Source Categories	
	def getTransferSourceCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT sourcetype FROM setup_transfersources'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtTransferSourceType = QStandardItem( "%s" % row[0])
            		qtTransferSourceType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtTransferSourceType )
            		num = num + 1
                        		
        	self.transferSourcesListView.setModel(model)
		self.transferSourcesListView.show()

        def pickSelectedTransferSource(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.transferSourcesListView.model().item(index.row(),0).text()
                self.txtTransferSources.setText(selectedItem)
                
        def saveTransferSourceType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	mytransfersource = self.txtTransferSources.text()		
        	
		# check if record exists
		query = '''SELECT sourcetype FROM setup_transfersources WHERE sourcetype='%s' ''' % (mytransfersource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_transfersources(sourcetype) 
                     		VALUES('%s')''' % (mytransfersource)
		else:
			query = '''UPDATE setup_transfersources SET sourcetype='%s'	WHERE sourcetype='%s' ''' % (mytransfersource, mytransfersource)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
                self.txtTransferSources.clear()
		#refresh categories list
		self.getTransferSourceCategories()               
                
	def deleteTransferSourceType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mytransfersource = self.txtTransferSources.text()		
        	
		# check if record exists
		query = '''SELECT sourcetype FROM setup_transfersources WHERE sourcetype='%s' ''' % (mytransfersource)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_transfersources WHERE sourcetype='%s' ''' % (mytransfersource)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		self.txtTransferSources.clear()
			
			#refresh categories list
			self.getTransferSourceCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Transfer Source', "Record not found")
        #End block of methods for managing Transfer Source Categories

	#Begin block of methods for managing Transfer Types	
	def getTransferTypes(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT assistancetype FROM setup_transfers'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtTransferType = QStandardItem( "%s" % row[0])
            		qtTransferType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtTransferType )
            		num = num + 1
                        		
        	self.transferTypesListView.setModel(model)
		self.transferTypesListView.show()

        def pickSelectedTransfer(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.transferTypesListView.model().item(index.row(),0).text()
                self.txtTransferType.setText(selectedItem)

                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT unitofmeasure FROM setup_transfers WHERE assistancetype='%s' ''' % (selectedItem)

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
                        unitOfMeasure = row[0]

		self.txtTransferUnitofMeasure.setText(unitOfMeasure)
                
                
        def saveTransferType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	mytransfertype = self.txtTransferType.text()
        	mymeasuringUnit = self.txtTransferUnitofMeasure.text()
        	
		# check if record exists
		query = '''SELECT assistancetype FROM setup_transfers WHERE assistancetype='%s' ''' % (mytransfertype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_transfers(assistancetype, unitofmeasure) 
                     		VALUES('%s', '%s')''' % (mytransfertype,mymeasuringUnit)
		else:
			query = '''UPDATE setup_transfers SET assistancetype='%s', unitofmeasure='%s' 	WHERE assistancetype='%s' ''' % (mytransfertype, mymeasuringUnit,mytransfertype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
                self.txtTransferType.clear()
        	self.txtTransferUnitofMeasure.clear()
                        
		#refresh categories list
		self.getTransferTypes()               
                
	def deleteTransferType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mytransfertype = self.txtTransferType.text()		
        	
		# check if record exists
		query = '''SELECT assistancetype FROM setup_transfers WHERE assistancetype='%s' ''' % (mytransfertype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM setup_transfers WHERE assistancetype='%s' ''' % (mytransfertype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getTransferTypes()
                        self.txtTransferType.clear()
                        self.txtTransferUnitofMeasure.clear()
			
			
		else:
			QMessageBox.information(self, 'Delete Transfer Type', "Record not found")
        #End block of methods for managing Transfer Types
