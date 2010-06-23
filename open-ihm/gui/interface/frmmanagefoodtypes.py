#-----------------------------------------------------------------------------------------------	
#	Filename: frmmanagefoodtypes.py
#
#	Class to create the form for adding, editing, or deleting Food Types - FrmManageFoodTypes.
#------------------------------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
from gui.designs.ui_managefoodtypes import Ui_FoodTypes

from data.GenericDBOP import GenericDBOP

class FrmManageFoodTypes(Ui_FoodTypes):		
	def setupUi(self,Form,Mdi):
		Ui_FoodTypes.setupUi(self,Form)
		
        	# get food type
        	self.getFoodTypes()

                #set input validator and restrict input to numeric values,
                myDblVal = QtGui.QDoubleValidator(-999.99, 999999.99, 2, self.txtKCalories)
                myDblVal.setNotation(QtGui.QDoubleValidator.StandardNotation)
                self.txtKCalories.setValidator(myDblVal);

                #connect relevant signals
		QtCore.QObject.connect(self.cmdManageFoodClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
		QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveFoodType)
		QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL("clicked()"), self.deleteFoodType)
		QtCore.QObject.connect(self.cmbFoodType, QtCore.SIGNAL("currentIndexChanged(int)"), self.populateForm)
              
	
	def getFoodTypes(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT foodtype FROM setup_crops'''

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
			foodtype = row[0]
            		self.cmbFoodType.addItem(foodtype)

            	self.cmbFoodType.setCurrentIndex(-1)

	
	def populateForm(self):
		'''
		populate form controls when user selects a particular food type	
		'''
		
		foodtype = self.cmbFoodType.currentText()
		self.txtKCalories.clear()
		self.cmbUnitOfMeasure.clear()

        	# select query to retrieve Food Types and related information
        	query = '''SELECT foodtype, energyvalueperunit, measuringunit FROM setup_crops WHERE foodtype ='%s' ''' % (foodtype)
        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
       		
		for row in recordset:
			energyvalue = str(row[1])
			measuringunit = str(row[2])
			
			#populate the form controls
			self.txtKCalories.setText(energyvalue)
			self.cmbUnitOfMeasure.addItem(measuringunit)
	
	def saveFoodType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.cmbFoodType.currentText()
		mymeasuringunit = self.cmbUnitOfMeasure.currentText()
        	myenergyvalue  = self.txtKCalories.text()
        	
		# check if record exists
		query = '''SELECT foodtype, energyvalueperunit, measuringunit
				FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_crops(foodtype, energyvalueperunit, measuringunit) 
                     		VALUES('%s',%s,'%s')''' % (myfoodtype, myenergyvalue, mymeasuringunit)
		else:
			query = '''UPDATE setup_crops SET foodtype='%s', energyvalueperunit=%s, measuringunit='%s'
                     		WHERE foodtype='%s' ''' % (myfoodtype, myenergyvalue, mymeasuringunit, myfoodtype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()

	def deleteFoodType(self):
		''' Deletes Food Type record from database '''

        	# get user selection
        	myfoodtype = self.cmbFoodType.currentText()

		#check if record exists
		query = '''SELECT foodtype, energyvalue, measuringunit
				FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)  

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

			self.cmbFoodType.clear()
			self.cmbUnitOfMeasure.clear()
        		self.txtKCalories.clear()
			
			#populate Food Types Combobox
			self.getFoodTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")

