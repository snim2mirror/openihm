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

        	self.model = QStandardItemModel()
        	self.listView.setModel(self.model)
        			
		# get asset types
        	self.getAssetCategories()

		# connect relevant signals and slots
		#self.connect(self.btnAssetsClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.listView.selectionModel(), SIGNAL("clicked(QModelIndex)"), self.manageCategories(QModelIndex))

	def getAssetCategories(self):
               	# select query to retrieve Asset Categories
        	query = '''SELECT assettype FROM assettypes'''
        	
                p = GenericDBOP(query)
                recordset = p.runSelectQuery()
				
		num = 0

       		for row in recordset:
			qtAssetType = QStandardItem( "%s" % row[0])
            		qtAssetType.setTextAlignment( Qt.AlignLeft )
            		self.model.setItem( num, 0, qtAssetType )
            		num = num + 1
                        		
        	
		#self.listView.show()

        def manageCategories(self,index1):
                tem = QStandardItem
                tem = str(self.model.index(index1).text())
                print item
               # self.txtAssetCategories.setText(int( self.model.itemFromIndex(0,0).text() ))
                
