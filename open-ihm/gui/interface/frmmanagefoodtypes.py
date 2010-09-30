#-----------------------------------------------------------------------------------------------	
#	Filename: frmmanagefoodtypes.py
#
#	Class to create the form for adding, editing, or deleting Food Types - FrmManageFoodTypes.
#------------------------------------------------------------------------------------------------

#from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.designs.ui_managefoodtypes import Ui_FoodTypes

from data.GenericDBOP import GenericDBOP

class FrmManageFoodTypes(QDialog, Ui_FoodTypes):		
        ''' Creates the Edit Project form. '''	
        def __init__(self, parent):
                
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)
		
        	# get food type
        	self.getFoodTypes()

                #set input validator and restrict input to numeric values,
                myIntVal = QIntValidator(0, 10000, self.txtKCalories)
                self.txtKCalories.setValidator(myIntVal);

                #connect relevant signals
		self.connect(self.cmdManageFoodClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveFoodType)
		self.connect(self.cmdDelete, SIGNAL("clicked()"), self.deleteFoodType)
		self.connect(self.cmbFoodType, SIGNAL("currentIndexChanged(int)"), self.populateForm)
              
	
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
        	print myfoodtype

		#check if record exists
		query = '''SELECT foodtype, energyvalueperunit, measuringunit
				FROM setup_crops WHERE foodtype='%s' ''' % (myfoodtype)  

      		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this record?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
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

