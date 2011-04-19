#-------------------------------------------------------------------	
#	Filename: frmexpendituretypes.py
#
#	Class to create the Manage Expenditure Types form - FrmExpenditureTypes.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Manage Asset Types Dialog design class
from gui.designs.ui_expendituretypes import Ui_ExpenditureTypes

#import GenericDBOP which has methods for managing database operations
from data.GenericDBOP import GenericDBOP

class FrmExpenditureTypes(QDialog, Ui_ExpenditureTypes):	
	''' Creates the Manage Expenditure Types from. Uses the design class
		in gui.designs.ui_expendituretypes. '''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

        	self.getExpenditureCategories()
        	self.getExpenditureTypes()
	
	def mdiClose(self):
		self.parent.closeActiveSubWindow()		

	#Begin block of methods for managing Expenditure Categories 	
	def getExpenditureCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT expenditurecategory FROM setup_expenditurecategories'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtExpenditureType = QStandardItem( "%s" % row[0])
            		qtExpenditureType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtExpenditureType )
            		num = num + 1
                        		
        	self.expenditureCategorylistView.setModel(model)
		self.expenditureCategorylistView.show()

        def pickSelectedCategory(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.expenditureCategorylistView.model().item(index.row(),0).text()
                self.txtCategory.setText(selectedItem)
                
        def saveCategoryType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	categorytype = self.txtCategory.text()		
        	
		# check if record exists
		query = '''SELECT expenditurecategory FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_expenditurecategories(expenditurecategory) 
                     		VALUES('%s')''' % (categorytype)
		else:
			query = '''UPDATE setup_expenditurecategories SET expenditurecategory='%s'	WHERE expenditurecategory='%s' ''' % (categorytype, categorytype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		self.getExpenditureCategories()                
                
	def deleteCategoryType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	categorytype = self.txtCategory.text()		
        	
		# check if record exists
		query = '''SELECT expenditurecategory FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Expenditure Category Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_expenditurecategories WHERE expenditurecategory='%s' ''' % (categorytype)

                                # execute query and commit changes
                                temp = GenericDBOP(query)
                                recordset = temp.runUpdateQuery()

                                self.txtCategory.clear()
                                #refresh categories list
                                self.getExpenditureCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Expenditure Categories

	#Begin block of methods for managing Expenditure Types	
	def getExpenditureTypes(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT expendituretype FROM setup_expendituretypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
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
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_expendituretypes(expendituretype) 
                     		VALUES('%s')''' % (myexpendituretype)
		else:
			query = '''UPDATE setup_expendituretypes SET expendituretype='%s'	WHERE expendituretype='%s' ''' % (myexpendituretype, myexpendituretype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		self.getExpenditureTypes()                
                
	def deleteExpenditureType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myexpendituretype = self.txtExpenseType.text()		
        	
		# check if record exists
		query = '''SELECT expendituretype FROM setup_expendituretypes WHERE expendituretype='%s' ''' % (myexpendituretype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
                        msg = "Are sure sure you want to delete this Expenditure Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:
			
                                query = '''DELETE FROM setup_expendituretypes WHERE expendituretype='%s' ''' % (myexpendituretype)

                                # execute query and commit changes
                                temp = GenericDBOP(query)
                                recordset = temp.runUpdateQuery()

                                self.txtExpenseType.clear()
                                #refresh categories list
                                self.getExpenditureTypes()			
			
		else:
			QMessageBox.information(self, 'Delete Expenditure Type', "Record not found")
        #End block of methods for managing Expenditure Types
			
