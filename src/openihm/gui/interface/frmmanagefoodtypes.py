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

Ui_FoodTypes, base_class = uic.loadUiType("gui/designs/ui_managefoodtypes_1.ui")

from frm_managefoodtypes_add import FrmAddFoodCropType
from frm_managefoodtypes_edit import FrmEditCropType

from mixins import MDIDialogMixin, MySQLMixin, TableViewMixin

class FrmManageFoodTypes(QDialog, Ui_FoodTypes, MySQLMixin, TableViewMixin, MDIDialogMixin):
        ''' Creates the Edit Project form. '''	
        def __init__(self, parent):
                
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)
		
        	# get food type
        	self.getFoodTypes()

                #connect relevant signals
#		self.connect(self.cmdManageFoodClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		
#		self.connect(self.cmdDelete, SIGNAL("clicked()"), self.deleteFoodType)
		
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		self.connect(self.cmdDeleteRows, SIGNAL("clicked()"), self.deleteSelectedCropTypes)
		self.connect(self.cmdEditRow, SIGNAL("clicked()"), self.editCropType)
		self.connect(self.cmdAddRow, SIGNAL("clicked()"), self.saveCropType)
		self.connect(self.cmdSearch, SIGNAL("clicked()"), self.searchCropType)
	
	def getFoodTypes(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT foodtype,measuringunit,energyvalueperunit FROM setup_crops'''

                recordset = self.executeResultsQuery(query)

		model = QStandardItemModel(1,2)
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('''Food Type'''))
		model.setHorizontalHeaderItem(1,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(2,QStandardItem('Kcals per Kg'))
		
		# add  data rows
		num = 0
	    
		for row in recordset:
		    qtCrop = QStandardItem( "%s" % row[0])
		    qtCrop.setTextAlignment( Qt.AlignLeft | Qt.AlignVCenter )
		    
		    qtUnitOfMeasure = QStandardItem( "%s" % row[1] )
		    qtUnitOfMeasure.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtUnitKcals = QStandardItem( "%i" % row[2] )
		    qtUnitKcals.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    model.setItem( num, 0, qtCrop )
		    model.setItem( num, 1, qtUnitOfMeasure )
		    model.setItem( num, 2, qtUnitKcals )
		    num = num + 1
	    
		self.tableView.setModel(model)
		#self.tableView.verticalHeader().hide()
                self.tableView.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
		self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
		self.tableView.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
		self.tableView.show()
            	
	def saveCropType(self):
		''' Show the Add Food Types form '''
		
		form = FrmAddCropType(self, self.parent.mdi)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
                form.exec_()
		self.getFoodTypes()

	def editCropType(self):
                
                if self.countRowsSelected(self.tableView) != 0:
                        
			# get the age of the selected record
			selectedRow = self.getCurrentRow(self.tableView)
			selectedcrop = self.tableView.model().item(selectedRow,0).text()
			measuringunit = self.tableView.model().item(selectedRow,1).text()
			energyvalue = self.tableView.model().item(selectedRow,2).text()

			# show edit food energy requirement form
			form = FrmEditCropType(self.parent,self.parent.mdi,selectedcrop,measuringunit,energyvalue)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			self.getFoodTypes()
			
		else:
			QMessageBox.information(self,"Edit Food Type","Please select the row containing food type to be edited.")
                
	def deleteSelectedCropTypes(self):

		numSelected = self.countRowsSelected(self.tableView)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected record?"
			else:
				msg = "Are you sure you want to delete the selected records?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the crop names for the selected records
			selectedRows = self.getSelectedRows(self.tableView)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tableView.model().item(row,0).text() )
			 
			# delete record with selected food type
			queries = []
			for cropname in selectedIds:
				queries.append('''DELETE FROM setup_crops WHERE foodtype='%s' ''' % (cropname))
			self.executeMultipleUpdateQueries(queries)

			self.getFoodTypes()

		else:
			QMessageBox.information(self,"Delete Food Types","Please select the rows containing food type(s) to be deleted.")

        def searchCropType(self):
                croptype = self.txtSearchCrop.text()
                numrows = self.tableView.model().rowCount()
                counter = 0
                cropfound = 0
                for counter in range(0,numrows):
                        currentIndex = self.tableView.model().index(counter,0)
                        currentitem = self.tableView.model().item(currentIndex.row(),0).text()
                        if croptype.lower() == currentitem.lower():
                                cropfound = 1
                                desiredIndex = currentIndex
                if cropfound:
                        self.tableView.scrollTo(currentIndex,QAbstractItemView.EnsureVisible)
                        self.tableView.selectRow(currentIndex.row())
                else:
                        QMessageBox.information(self,"Item Not Found","Item not found")
                        
                                
                                
