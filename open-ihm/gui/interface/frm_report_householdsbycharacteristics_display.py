#-------------------------------------------------------------------	
#	Filename: frm_report_householdsbycharacteristics_display.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.designs.ui_report_householdsbycharacteristics_display import Ui_DisplayHouseholdsByChar
from outputs.routines.report_households_by_characteristics_write import HouseholdsByCharacteristicsWrite

from mixins import MDIDialogMixin

class HouseholdsByCharDisplay(QDialog, Ui_DisplayHouseholdsByChar, MDIDialogMixin):
    ''' Creates the view households form '''	
    def __init__(self, parent,freporttable):
        ''' Set up the dialog box interface '''
	self.parent = parent
	self.rtable = freporttable
	QDialog.__init__(self)
	self.setupUi(self)
	self.parent = parent

	self.populateForm()
	    
    def saveReportAsSpreadtsheet(self):
        
        # write report in a spreadsheet file
        report = HouseholdsByCharacteristicsWrite()
        report.writeSpreadsheetReport(self.rtable)

    def populateForm(self):
        model = QStandardItemModel(1,2)
		
	# set model headers
	model.setHorizontalHeaderItem(0,QStandardItem('Household No.'))
	model.setHorizontalHeaderItem(1,QStandardItem('Household Name'))
		
	# add  data rows
	num = 0
	    
	for row in self.rtable:
            qtHouseholdNo = QStandardItem( "%i" % row[0])
	    qtHouseholdNo.setTextAlignment( Qt.AlignCenter )
		    
	    qtHouseholdName = QStandardItem( row[1] )
		    
	    model.setItem( num, 0, qtHouseholdNo )
	    model.setItem( num, 1,  qtHouseholdName )
	    num = num + 1
	    
	self.tableView.setModel(model)
	self.tableView.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	tablewidth = self.tableView.columnWidth (0) + self.tableView.columnWidth (1)
	self.tableView.setMaximumSize(tablewidth,551)
	self.tableView.setMaximumSize(tablewidth + 30,629)
	self.tableView.show()
