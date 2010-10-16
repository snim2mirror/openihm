#---------------------------------------------------------------------------------------------------------------------	
#	Filename: frmhousecharacteristics.py
#
#	Class to create the form for adding, editing, or deleting Household characteristics - FrmHouseCharacteristics.
#----------------------------------------------------------------------------------------------------------------------

#from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Create House Characteristics Dialog design class
from gui.designs.ui_housecharacteristics import Ui_HouseCharacteristics

#Import class with persistence management methods
from data.GenericDBOP import GenericDBOP

class FrmHouseCharacteristics(QDialog, Ui_HouseCharacteristics):		
        ''' Creates the Edit Project form. '''	
        def __init__(self, parent):
                
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)
		

		# get personal type
        	self.getHouseholdCharacteristics()
		
		self.connect(self.btnCharacteristicSave, SIGNAL("clicked()"), self.saveHouseholdCharacteristic)
		self.connect(self.btnCharacteristicDelete, SIGNAL("clicked()"), self.deleteHouseholdCharacteristic)
		self.connect(self.cmbCharacteristic, SIGNAL("currentIndexChanged(int)"), self.populateForm)
		self.connect(self.btnHouseClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
	
	def getHouseholdCharacteristics(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT characteristic FROM globalhouseholdcharacteristics'''

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
			characteristic = row[0]
            		self.cmbCharacteristic.addItem(characteristic)

            	self.cmbDataType.addItem(' ')
		self.cmbDataType.addItem('boolean/Yes/No')
		self.cmbDataType.addItem('Integer')
		self.cmbDataType.addItem('String')
		self.cmbDataType.setCurrentIndex(-1)
		self.cmbCharacteristic.setCurrentIndex(-1)
			
	def populateForm(self):
		'''
		populate form controls when user selects a particular food type	
		'''
		
		mycharacteristic = self.cmbCharacteristic.currentText()
		#self.cmbDataType.clear()
		self.txtDescription.clear()

        	# select query to retrieve Food Types and related information
        	query = '''SELECT characteristic, datatype, description FROM globalhouseholdcharacteristics WHERE characteristic ='%s' ''' % (mycharacteristic)
        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
                formdatatype = 0
       		description = ''
		for row in recordset:
			formdatatype = row[1]
			description = str(row[2])
					
		#populate datatype combobox
		if formdatatype == 1:
                        dataIndex = 1
                elif formdatatype == 2:
                        dataIndex = 2
                elif formdatatype == 3:
                        dataIndex = 3
                else:
                        dataIndex = -1

		self.cmbDataType.setCurrentIndex(dataIndex)
		self.txtDescription.setText(description)
	
	def saveHouseholdCharacteristic(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	mycharacteristic = self.cmbCharacteristic.currentText()
		mydescription = self.txtDescription.text()
		formdatatype = self.cmbDataType.currentText()
		if formdatatype == 'boolean/Yes/No':
                        mydatatype  = 1
                elif formdatatype == 'Integer':
                        mydatatype = 2
                elif formdatatype == 'String':
                        mydatatype = 3
                
        	
		# check if record exists
		query = '''SELECT characteristic, datatype, description
				FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO globalhouseholdcharacteristics(characteristic, datatype, description) 
                     		VALUES('%s',%i,'%s')''' % (mycharacteristic, mydatatype, mydescription)
		else:
			query = '''UPDATE globalhouseholdcharacteristics SET characteristic='%s', datatype=%i, description='%s'
                     		WHERE characteristic='%s' ''' % (mycharacteristic, mydatatype, mydescription, mycharacteristic)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()

                #refresh interface
                self.cmbCharacteristic.clear()
		self.txtDescription.clear()
		self.cmbDataType.clear()
                self.getHouseholdCharacteristics()
                

	def deleteHouseholdCharacteristic(self):
		''' Deletes record from database '''

        	# get user selection
        	mycharacteristic = self.cmbCharacteristic.currentText()

		#check if record exists
		query = '''SELECT characteristic, datatype, description
				FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)  

      		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:

                        msg = "Are sure sure you want to delete this Household Characteristic?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)

                                # execute query and commit changes
                                temp = GenericDBOP(query)
                                recordset = temp.runUpdateQuery()

                                self.cmbCharacteristic.clear()
                                self.cmbDataType.clear()
                                self.txtDescription.clear()
			
                                #populate Food Types Combobox
                                self.getHouseholdCharacteristics()			
			
		else:
			QMessageBox.information(self, 'Household Characteristic', "Record not found")

