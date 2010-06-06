#---------------------------------------------------------------------------------------------------------------------	
#	Filename: frmpersonalcharacteristics.py
#
#	Class to create the form for adding, editing, or deleting Personal characteristics - FrmPersonalCharacteristics.
#----------------------------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from data.GenericDBOP import GenericDBOP

# import the Create House Characteristics Dialog design class
from gui.designs.ui_personalcharacteristics import Ui_PersonalCharacteristics

class FrmPersonalCharacteristics(Ui_PersonalCharacteristics):		
	def setupUi(self,Form,Mdi):
		Ui_PersonalCharacteristics.setupUi(self,Form)

		# get personal type
        	self.getPersonalCharacteristics()
		
		QtCore.QObject.connect(self.btnCharacteristicSave, QtCore.SIGNAL("clicked()"), self.savePersonalCharacteristic)
		QtCore.QObject.connect(self.btnCharacteristicDelete, QtCore.SIGNAL("clicked()"), self.deletePersonalCharacteristic)
		QtCore.QObject.connect(self.cmbCharacteristic, QtCore.SIGNAL("currentIndexChanged(int)"), self.populateForm)
		QtCore.QObject.connect(self.btnPCharsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
	
	def getPersonalCharacteristics(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT characteristic FROM globalpersonalcharacteristics'''

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
        	query = '''SELECT characteristic, datatype, description FROM globalpersonalcharacteristics WHERE characteristic ='%s' ''' % (mycharacteristic)
        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
                formdatatype = 0
                description = ''
       		
		for row in recordset:
			formdatatype = row[1]
			description = str(row[2])
		print formdatatype
			
		#populate datatype combobox
		if formdatatype == 1:
                        dataIndex = 1
                elif formdatatype == 2:
                        dataIndex = 2
                elif formdatatype == 3:
                        dataIndex = 3
                else:
                        dataIndex = -1

                print dataIndex
		self.cmbDataType.setCurrentIndex(dataIndex)
		self.txtDescription.setText(description)
	
	def savePersonalCharacteristic(self):
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
				FROM globalpersonalcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO globalpersonalcharacteristics(characteristic, datatype, description) 
                     		VALUES('%s',%i,'%s')''' % (mycharacteristic, mydatatype, mydescription)
		else:
			query = '''UPDATE globalpersonalcharacteristics SET characteristic='%s', datatype=%i, description='%s'
                     		WHERE characteristic='%s' ''' % (mycharacteristic, mydatatype, mydescription, mycharacteristic)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#populate Food Types Combobox
		self.getPersonalCharacteristics()                

	def deletePersonalCharacteristic(self):
		''' Deletes record from database '''

        	# get user selection
        	mycharacteristic = self.cmbCharacteristic.currentText()

		#check if record exists
		query = '''SELECT characteristic, datatype, description
				FROM globalpersonalcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)  

      		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM globalpersonalcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			self.cmbCharacteristic.clear()
			self.cmbDataType.clear()
        		self.txtDescription.clear()
			
			#populate Food Types Combobox
			self.getPersonalCharacteristics()			
			
		else:
			QMessageBox.information(self, 'Delete Personal characteristic', "Record not found")

