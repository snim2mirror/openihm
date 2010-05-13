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
		
		QtCore.QObject.connect(self.cmdManageFoodClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
		QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveFoodType)
		QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL("clicked()"), self.deleteFoodType)
		QtCore.QObject.connect(self.cmbFoodType, QtCore.SIGNAL("currentIndexChanged(int)"), self.populateForm)
		
	
	def getFoodTypes(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT foodtype FROM foodenergyvalue'''

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
			foodtype = row[0]
            		self.cmbFoodType.addItem(foodtype)
			
	
	def populateForm(self):
		'''
		populate form controls when user selects a particular food type	
		'''
		
		foodtype = self.cmbFoodType.currentText()
		self.cmbKCalories.clear()
		self.cmbUnitOfMeasure.clear()

        	# select query to retrieve Food Types and related information
        	query = '''SELECT foodtype, energyvalue, measuringunit FROM foodenergyvalue WHERE foodtype ='%s' ''' % (foodtype)
        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
       		
		for row in recordset:
			energyvalue = str(row[1])
			measuringunit = str(row[2])
			
			#populate the form controls
			self.cmbKCalories.addItem(energyvalue)
			self.cmbUnitOfMeasure.addItem(measuringunit)
	
	def saveFoodType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.cmbFoodType.currentText()
		mymeasuringunit = self.cmbUnitOfMeasure.currentText()
        	myenergyvalue  = self.cmbKCalories.currentText()
        	
		# check if record exists
		query = '''SELECT foodtype, energyvalue, measuringunit
				FROM foodenergyvalue WHERE foodtype='%s' ''' % (myfoodtype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO foodenergyvalue(foodtype, energyvalue, measuringunit) 
                     		VALUES('%s',%s,'%s')''' % (myfoodtype, myenergyvalue, mymeasuringunit)
		else:
			query = '''UPDATE foodenergyvalue SET foodtype='%s', energyvalue=%s, measuringunit='%s'
                     		WHERE foodtype='%s' ''' % (myfoodtype, myenergyvalue, mymeasuringunit, myfoodtype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()

	def deleteFoodType(self):
		''' Deletes record from database '''

        	# get user selection
        	myfoodtype = self.cmbFoodType.currentText()

		#check if record exists
		query = '''SELECT foodtype, energyvalue, measuringunit
				FROM foodenergyvalue WHERE foodtype='%s' ''' % (myfoodtype)  

      		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM foodenergyvalue WHERE foodtype='%s' ''' % (myfoodtype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			self.cmbFoodType.clear()
			self.cmbUnitOfMeasure.clear()
        		self.cmbKCalories.clear()
			
			#populate Food Types Combobox
			self.getFoodTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")

