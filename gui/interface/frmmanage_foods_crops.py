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

#from gui.designs.ui_managefoodtypes import Ui_FoodTypes
Ui_FoodTypes, base_class = uic.loadUiType("gui/designs/ui_managefoodtypes_1.ui")


from frm_managefoodtypes_add import FrmAddFoodCropType
from frm_managefoodtypes_edit import FrmEditCropType

from mixins import MDIDialogMixin, MySQLMixin

class FrmManageTypes(QDialog, Ui_FoodTypes, MySQLMixin, MDIDialogMixin):		
        ''' Creates the Edit Project form. '''	
        def __init__(self, parent):
                
                ''' Set up the dialog box interface '''
                self.parent = parent
                QDialog.__init__(self)
                self.setupUi(self)
		
        	# get food type
        	self.getTypes()

		# self.connect(self.cmdManageFoodClose, SIGNAL("clicked()"), self.parent.closeActiveSubWindow)
		
		# self.connect(self.cmdDelete, SIGNAL("clicked()"), self.deleteFoodType)
		

	def getTypes(self):
               	# select query to retrieve Food Types and related information
        	query = '''SELECT name,category,unitofmeasure,energyvalueperunit FROM setup_foods_crops'''
                recordset = self.executeResultsQuery(query)

		model = QStandardItemModel(1,2)
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Name'))
		model.setHorizontalHeaderItem(1,QStandardItem('Category'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(3,QStandardItem('Kcals per Kg'))
		
		# add  data rows
		num = 0
	    
		for row in recordset:
		    qtName = QStandardItem( "%s" % row[0])
		    qtName.setTextAlignment( Qt.AlignLeft | Qt.AlignVCenter )
		    
		    qtCategory = QStandardItem( "%s" % row[1] )
		    qtCategory.setTextAlignment( Qt.AlignLeft | Qt.AlignVCenter )

		    qtUnitOfMeasure = QStandardItem( "%s" % row[2] )
		    qtUnitOfMeasure.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtUnitKcals = QStandardItem( "%i" % row[3] )
		    qtUnitKcals.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    model.setItem( num, 0, qtName )
		    model.setItem( num, 1, qtCategory )
		    model.setItem( num, 2, qtUnitOfMeasure )
		    model.setItem( num, 3, qtUnitKcals )
		    num = num + 1
	    
		self.tableView.setModel(model)
		#self.tableView.verticalHeader().hide()
                self.tableView.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
                self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
		self.tableView.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
		self.tableView.horizontalHeader().setResizeMode(3, QHeaderView.ResizeToContents)
		self.tableView.show()
            	
	def saveCropType(self):
		''' Show the Add Food Types form '''
		
		form = FrmAddFoodCropType(self, self.parent)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
                form.exec_()
		self.getTypes()

	def editCropType(self):
                
                if self.countRowsSelected(self.tableView) != 0:
                        
			# get the age of the selected record
			selectedRow = self.getCurrentRow(self.tableView)
			selectedtype = self.tableView.model().item(selectedRow,0).text()
			category = self.tableView.model().item(selectedRow,1).text()
			measuringunit = self.tableView.model().item(selectedRow,2).text()
			energyvalue = self.tableView.model().item(selectedRow,3).text()

			# show edit food/crop energy requirement form
			form = FrmEditCropType(self.parent,selectedtype,category,measuringunit,energyvalue)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			self.getTypes()
			
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
			# get the names for the selected records
			selectedRows = self.getSelectedRows(self.tableView)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tableView.model().item(row,0).text() )

			queries = []
			for name in selectedIds:
				queries.append('''DELETE FROM setup_foods_crops WHERE name='%s' ''' % (name))
			self.executeMultipleUpdateQueries(queries)
    
			self.getTypes()

		else:
			QMessageBox.information(self,"Delete Types","Please select the rows containing food/crop type(s) to be deleted.")

	def countRowsSelected(self, tblVw):
		selectedRows = self.getSelectedRows(tblVw)
		return len(selectedRows)
		
	def getSelectedRows(self, tblVw):
		
		selectedRows = []
		selectedIndexes = tblVw.selectedIndexes()
		
		for indexVal in selectedIndexes:
			if indexVal.row() not in selectedRows:
				selectedRows.append(indexVal.row())
				
		return selectedRows
	
	def getCurrentRow(self, tblVw):
		indexVal = tblVw.currentIndex()
		return indexVal.row()

        def searchCropType(self):
                croptype = str(self.txtSearchCrop.text())
                numrows = self.tableView.model().rowCount()
                counter = 0
                cropfound = 0
                for counter in range(0,numrows):
                        
                        currentIndex = self.tableView.model().index(counter,0)
                        currentitem = str(self.tableView.model().item(currentIndex.row(),0).text())
                        if croptype.lower() == currentitem.lower():
                                cropfound = 1
                                desiredIndex = currentIndex
                                break
                if cropfound==1:
                        self.tableView.scrollTo(currentIndex,QAbstractItemView.EnsureVisible)
                        self.tableView.selectRow(currentIndex.row())
                else:
                        QMessageBox.information(self,"Item Not Found","Item not found")
                        
                                
                                
