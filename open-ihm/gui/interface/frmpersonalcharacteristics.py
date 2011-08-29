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

from data.GenericDBOP import GenericDBOP

# import the Create House Characteristics Dialog design class
from gui.designs.ui_personalcharacteristics import Ui_PersonalCharacteristics

from mixins import MDIDialogMixin

class FrmPersonalCharacteristics(QDialog, Ui_PersonalCharacteristics, MDIDialogMixin):
        def __init__(self, parent):
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)

		# get personal type
        	self.getPersonalCharacteristics()
        	self.setDatatypes()
		
	def getPersonalCharacteristics(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT characteristic FROM globalpersonalcharacteristics'''

        	p = GenericDBOP(query)
                recordset = p.runSelectQuery()
	      		
		for row in recordset:
			characteristic = row[0]
            		self.cmbCharacteristic.addItem(characteristic)

            	self.cmbCharacteristic.setCurrentIndex(-1)

        def setDatatypes(self):
                self.cmbDataType.addItem(' ')
		self.cmbDataType.addItem('boolean/Yes/No')
		self.cmbDataType.addItem('Integer')
		self.cmbDataType.addItem('String')
		self.cmbDataType.addItem('Double')
		self.cmbDataType.setCurrentIndex(-1)
			
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
#		print formdatatype
			
		#populate datatype combobox
		if formdatatype == 1:
                        dataIndex = 1
                elif formdatatype == 2:
                        dataIndex = 2
                elif formdatatype == 3:
                        dataIndex = 3
                elif formdatatype == 4:
                        dataIndex = 4

                else:
                        dataIndex = -1

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
                elif formdatatype == 'Double':
                        mydatatype = 4
                
        	
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
		self.cmbCharacteristic.clear()
		self.getPersonalCharacteristics()
		self.cmbDataType.setCurrentIndex(-1)


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
			
                        msg = "Are sure sure you want to delete this Characteristic?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

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

