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

# import the Manage Asset Types Dialog design class
from gui.designs.ui_expendituretypes import Ui_ExpenditureTypes

from mixins import MDIDialogMixin, MySQLMixin

class FrmExpenditureTypes(QDialog, Ui_ExpenditureTypes, MDIDialogMixin, MySQLMixin):	
	''' Creates the Manage Expenditure Types from. Uses the design class
		in gui.designs.ui_expendituretypes. '''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

#        	self.getExpenditureCategories()
        	self.getExpenditureTypes()

	### FIXME: Can we just delete this?
		
	#Begin block of methods for managing Expenditure Categories 	
 	# def getExpenditureCategories(self):
        #         '''Get pre-existing assets categories from database and populate categories list'''
        #        	# select query to retrieve Asset Categories
        # 	query = '''SELECT expenditurecategory FROM setup_expenditurecategories'''
        	
        #         recordset = self.executeResultsQuery()
				
	# 	model = QStandardItemModel()
	# 	num = 0

       	# 	for row in recordset:
	# 		qtExpenditureType = QStandardItem( "%s" % row[0])
        #     		qtExpenditureType.setTextAlignment( Qt.AlignLeft )
        #     		model.setItem( num, 0, qtExpenditureType )
        #     		num = num + 1
                        		
        # 	self.expenditureCategorylistView.setModel(model)
	# 	self.expenditureCategorylistView.show()

        # def pickSelectedCategory(self,index):
        #         '''get selected item and populate categories textbox'''
        #         selectedItem = self.expenditureCategorylistView.model().item(index.row(),0).text()
        #         self.txtCategory.setText(selectedItem)
                
        # def saveCategoryType(self):
        # 	''' Saves newly created data to database '''

        # 	# get the data entered by user
        # 	categorytype = self.txtCategory.text()		
        	
	# 	# check if record exists
	# 	query = '''SELECT expenditurecategory FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)    
		
        #         recordset = self.executeResultsQuery()

	# 	numrows = 0		
	# 	for row in recordset:
	# 		numrows = numrows + 1
				      	
	# 	if numrows == 0:
			
	# 		query = '''INSERT INTO setup_expenditurecategories(expenditurecategory) 
        #              		VALUES('%s')''' % (categorytype)
	# 	else:
	# 		query = '''UPDATE setup_expenditurecategories SET expenditurecategory='%s'	WHERE expenditurecategory='%s' ''' % (categorytype, categorytype)
    
        # 	# execute query and commit changes
        #       self.executeUpdateQuery(query)
	# 	#refresh categories list
	# 	self.getExpenditureCategories()                
                
	# def deleteCategoryType(self):
	# 	''' Deletes record from database '''

        # 	# get the data entered by user
        # 	categorytype = self.txtCategory.text()		
        	
	# 	# check if record exists
	# 	query = '''SELECT expenditurecategory FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)    
		
        #       recordset = self.executeResultsQuery(query)
	# 	numrows = 0		
	# 	for row in recordset:
	# 		numrows = numrows + 1

	# 	if numrows <> 0:
        #                 msg = "Are sure sure you want to delete this Expenditure Category Type?"
        #                 ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
        #                 if ret == QMessageBox.Yes:
			
        #                         query = '''DELETE FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)

        #                         # execute query and commit changes
        #                         self.executeUpdateQuery(query)

        #                         self.txtCategory.clear()
        #                         #refresh categories list
        #                         self.getExpenditureCategories()			
			
	# 	else:
	# 		QMessageBox.information(self, 'Delete Food Type', "Record not found")
        # #End block of methods for managing Expenditure Categories

	#Begin block of methods for managing Expenditure Types	
	def getExpenditureTypes(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT expendituretype FROM setup_expendituretypes'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtExpenditureType = QStandardItem( "%s" % row[0])
            		qtExpenditureType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtExpenditureType )
            		num = num + 1
                        		
        	self.expenseTypeListView.setModel(model)
		self.expenseTypeListView.show()

        def pickSelectedExpenditure(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.expenseTypeListView.model().item(index.row(),0).text()
                self.txtExpenseType.setText(selectedItem)
                
        def saveExpenditureType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myexpendituretype = self.txtExpenseType.text()		
        	
		# check if record exists
		query = '''SELECT expendituretype FROM setup_expendituretypes WHERE expendituretype='%s' ''' % (myexpendituretype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_expendituretypes(expendituretype) 
                     		VALUES('%s')''' % (myexpendituretype)
		else:
			query = '''UPDATE setup_expendituretypes SET expendituretype='%s'	WHERE expendituretype='%s' ''' % (myexpendituretype, myexpendituretype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
		#refresh categories list
		self.getExpenditureTypes()                
                
	def deleteExpenditureType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myexpendituretype = self.txtExpenseType.text()		
        	
		# check if record exists
		query = '''SELECT expendituretype FROM setup_expendituretypes WHERE expendituretype='%s' ''' % (myexpendituretype)

                recordset = self.executeResultsQuery(query)
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Expenditure Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_expendituretypes WHERE expendituretype='%s' ''' % (myexpendituretype)

                                # execute query and commit changes
                                recordset = self.executeUpdateQuery(query)

                                self.txtExpenseType.clear()
                                #refresh categories list
                                self.getExpenditureTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Expenditure Type', "Record not found")
        #End block of methods for managing Expenditure Types
			
