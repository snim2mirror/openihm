# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the Manage Asset Types Dialog design class
from gui.designs.ui_manageassets import Ui_ManageAssetDetails

#import GenericDBOP which has methods for managing database operations
from data.GenericDBOP import GenericDBOP

class ManageTradableGoods(QDialog, Ui_ManageAssetDetails):
    ''' Creates the Manage Asset Details from. Uses the design class
		in gui.designs.ui_manageassets. '''	
	
    def __init__(self, parent):
        
	''' Set up the dialog box interface '''
	self.parent = parent
        QDialog.__init__(self)
       	self.setupUi(self)
        self.parent = parent
        
    #Begin block of methods for managing TradableGood details 
    def getTradableGoodTypes(self):
        
        '''Get pre-existing tree types from database and populate categories list'''
        # select query to retrieve Food types
        query = '''SELECT tradablegoodtype FROM setup_tradablegoods'''
        	
        p = GenericDBOP(query)
        recordset = p.runSelectQuery()
				
	model = QStandardItemModel()
	num = 0

       	for row in recordset:
		qtTradableGoodType = QStandardItem( "%s" % row[0])
        	qtTradableGoodType.setTextAlignment( Qt.AlignLeft )
        	model.setItem( num, 0, qtTradableGoodType )
        	num = num + 1
                        		
        self.tradableGoodsListView.setModel(model)
	self.tradableGoodsListView.show()	

    def pickSelectedTradableGoodType(self,index):
        '''get selected item and populate categories textbox'''
                
        selectedTradableGoodType = self.tradableGoodsListView.model().item(index.row(),0).text()
        self.txtTradableGoodType.setText(selectedTradableGoodType)
        #select query to retrieve measuring unit for selected tree type
        query = '''SELECT unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (selectedTradableGoodType)

        p = GenericDBOP(query)
        recordset = p.runSelectQuery()
	      		
	for row in recordset:
            unitOfMeasure = row[0]

	self.txtTradableGoodMeasuringUnit.setText(unitOfMeasure)

    def saveTradableGoodType(self):
        ''' Saves newly created data to database '''

        # get the data entered by user
        mytradablegood = self.txtTradableGoodType.text()
        mymeasuringunit = self.txtTradableGoodMeasuringUnit.text()
                        	
	# check if record exists
	query = '''SELECT tradablegoodtype, unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)    
		
	p = GenericDBOP(query)
        recordset = p.runSelectQuery()

	numrows = 0		
	for row in recordset:
            numrows = numrows + 1
				      	
            if numrows == 0:
			
		query = '''INSERT INTO setup_tradablegoods(tradablegoodtype, unitofmeasure) 
                     		VALUES('%s','%s')''' % (mytradablegood, mymeasuringunit)
            else:
		query = '''UPDATE setup_tradablegoods SET tradablegoodtype='%s', unitofmeasure='%s'
                     		WHERE tradablegoodtype='%s' ''' % (mytradablegood, mymeasuringunit, mytradablegood)
    
        # execute query and commit changes
        temp = GenericDBOP(query)
        recordset = temp.runUpdateQuery()
	#refresh categories list
	#self.getCategories()
                                
    def deleteTradableGoodType(self):
	''' Deletes record from database '''

       	# get the data entered by user
       	mytradablegood = self.txtTradableGoodType.text()		
        	
	# check if record exists
	query = '''SELECT tradablegoodtype, unitofmeasure FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)
		
	p = GenericDBOP(query)
        recordset = p.runSelectQuery()
	numrows = 0		
	for row in recordset:
		numrows = numrows + 1

	if numrows <> 0:
			
		query = '''DELETE FROM setup_tradablegoods WHERE tradablegoodtype='%s' ''' % (mytradablegood)

		# execute query and commit changes
       		temp = GenericDBOP(query)
                recordset = temp.runUpdateQuery()

			
       		#self.cmbKCalories.clear()
			
		#refresh categories list
		self.getAssetCategories()			
			
	else:
		QMessageBox.information(self, 'Delete TradableGood Type', "Record not found")
        #End block of methods for managing TradableGood details


    
