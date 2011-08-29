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


#from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

# import the Create House Characteristics Dialog design class
Ui_HouseCharacteristics, base_class = uic.loadUiType("gui/designs/ui_housecharacteristics.ui")

from mixins import MDIDialogMixin, MySQLMixin

class FrmHouseCharacteristics(QDialog, Ui_HouseCharacteristics, MySQLMixin, MDIDialogMixin):
        ''' Creates the Edit Project form. '''	
        def __init__(self, parent):
                
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)
		

		# get personal type
        	self.getHouseholdCharacteristics()
        	self.setDataTypes()

	def getHouseholdCharacteristics(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT characteristic FROM globalhouseholdcharacteristics'''

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
			characteristic = row[0]
            		self.cmbCharacteristic.addItem(characteristic)
		self.cmbCharacteristic.setCurrentIndex(-1)

        def setDataTypes(self):
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
        	query = '''SELECT characteristic, datatype, description FROM globalhouseholdcharacteristics WHERE characteristic ='%s' ''' % (mycharacteristic)

                recordset = self.executeResultsQuery(query)
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
                elif formdatatype == 4:
                        dataIndex = 4
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
                elif formdatatype == 'Double':
                        mydatatype = 4
                
        	
		# check if record exists
		query = '''SELECT characteristic, datatype, description
				FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO globalhouseholdcharacteristics(characteristic, datatype, description) 
                     		VALUES('%s',%i,'%s')''' % (mycharacteristic, mydatatype, mydescription)
		else:
			query = '''UPDATE globalhouseholdcharacteristics SET characteristic='%s', datatype=%i, description='%s'
                     		WHERE characteristic='%s' ''' % (mycharacteristic, mydatatype, mydescription, mycharacteristic)
    
        	# execute query and commit
		self.executeUpdateQuery(query)

                #refresh interface
                self.cmbCharacteristic.clear()
		self.txtDescription.clear()
                self.getHouseholdCharacteristics()
		self.cmbDataType.setCurrentIndex(-1)

	def deleteHouseholdCharacteristic(self):
		''' Deletes record from database '''

        	# get user selection
        	mycharacteristic = self.cmbCharacteristic.currentText()

		#check if record exists
		query = '''SELECT characteristic, datatype, description
				FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)  

                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:

                        msg = "Are sure sure you want to delete this Household Characteristic?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM globalhouseholdcharacteristics WHERE characteristic='%s' ''' % (mycharacteristic)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)

                                self.cmbCharacteristic.clear()
                                self.cmbDataType.clear()
                                self.txtDescription.clear()
			
                                #populate Food Types Combobox
                                self.getHouseholdCharacteristics()			
			
		else:
			QMessageBox.information(self, 'Household Characteristic', "Record not found")

