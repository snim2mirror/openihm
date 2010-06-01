#-------------------------------------------------------------------	
#	Filename: frmmanageassets.py
#
#	Class to create the Manage Asset Details form - FrmManageAssetDetails.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Manage Asset Types Dialog design class
from gui.designs.ui_manageassets import Ui_ManageAssetDetails

#import GenericDBOP which has methods for managing database operations
from data.GenericDBOP import GenericDBOP

class FrmManageAssetDetails(QDialog, Ui_ManageAssetDetails):	
	''' Creates the Manage Asset Details from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent
        			
		# get asset types
        	self.getAssetCategories()

		# connect relevant signals and slots
		#self.connect(self.btnAssetsClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		#self.connect(self.listView.selectionModel(), SIGNAL("currentChanged(QModelIndex,QModelIndex)"), self.manageCategories)
		self.connect(self.btnCatSave, SIGNAL("clicked()"), self.saveCategoryType)
		self.connect(self.btnCatDelete, SIGNAL("clicked()"), self.deleteCategoryType)
		self.connect(self.listView, SIGNAL("clicked(QModelIndex)"), self.getCategories)

	def getAssetCategories(self):
               	# select query to retrieve Asset Categories
        	query = '''SELECT assettype FROM assettypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtAssetType = QStandardItem( "%s" % row[0])
            		qtAssetType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtAssetType )
            		num = num + 1
                        		
        	self.listView.setModel(model)
		self.listView.show()

        def getCategories(self,index):
                #get selected item and populate categories textbox
                selectedItem = self.listView.model().item(index.row(),0).text()
                self.txtAssetCategories.setText(selectedItem)
                
        def saveCategoryType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	categorytype = self.txtAssetCategories.text()		
        	
		# check if record exists
		query = '''SELECT assettype FROM assettypes WHERE assettype='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()

		numrows = 0		
		for row in recordset:
			numrows = numrows + 1
				      	
		if numrows == 0:
			
			query = '''INSERT INTO assettypes(assettype) 
                     		VALUES('%s')''' % (categorytype)
		else:
			query = '''UPDATE assettypes SET assettype='%s'	WHERE assettype='%s' ''' % (categorytype, categorytype)
    
        	# execute query and commit changes
        	temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()
		#refresh categories list
		#self.getCategories()                
                
	def deleteCategoryType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	categorytype = self.txtAssetCategories.text()		
        	
		# check if record exists
		query = '''SELECT assettype FROM assettypes WHERE assettype='%s' ''' % (categorytype)    
		
		p = GenericDBOP(query)
                recordset = p.runSelectQuery()
		numrows = 0		
		for row in recordset:
			numrows = numrows + 1

		if numrows <> 0:
			
			query = '''DELETE FROM assettypes WHERE assettype='%s' ''' % (categorytype)

			# execute query and commit changes
        		temp = GenericDBOP(query)
                        recordset = temp.runUpdateQuery()

			
        		#self.cmbKCalories.clear()
			
			#refresh categories list
			self.getCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
