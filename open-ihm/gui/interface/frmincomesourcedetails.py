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

		# connect relevant signals and slots
		#self.connect(self.btnManageIncomeClose, SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
		#signals for managing food types
		self.connect(self.cropListView, SIGNAL("clicked(QModelIndex)"), self.pickselectedCropItem)
		self.connect(self.btnCropSave, SIGNAL("clicked()"), self.saveCropType)
		self.connect(self.btnCropDelete, SIGNAL("clicked()"), self.deleteCropType)


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
		#self.getCategories()
                                
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
			self.getAssetCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Food Stocks
