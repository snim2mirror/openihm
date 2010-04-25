#-------------------------------------------------------------------	
#	Filename: frmhouseholds.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_households_all import Ui_AllHouseholds

class FrmHouseholds(QDialog, Ui_AllHouseholds):	
    ''' Creates the household data (income, assets, expenditure, etc) form '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.config = Config.dbinfo().copy()
        
        self.lblProjectName.setText( self.parent.projectname ) 
        # get current project details
        self.getHouseholds()
        
        # connect relevant signals and slots
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        
    def getHouseholds(self):
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project households
        query = '''SELECT hhid, householdname, totalassetvalue, totalincomevalue, totalexpenditure, dateofcollection 
                     FROM households WHERE pid=%i''' % (self.parent.projectid)
        
        cursor.execute(query)
        
        model = QStandardItemModel(1,2)

        # set model headers
        model.setHorizontalHeaderItem(0,QStandardItem('Household No.'))
        model.setHorizontalHeaderItem(1,QStandardItem('Household Name'))
        model.setHorizontalHeaderItem(2,QStandardItem('Total Asset Value'))
        model.setHorizontalHeaderItem(3,QStandardItem('Total Income Value'))
        model.setHorizontalHeaderItem(4,QStandardItem('Total Expenditure'))
        model.setHorizontalHeaderItem(5,QStandardItem('Date Visited'))
        
        # add  data rows
        num = 0
        
        for row in cursor.fetchall():
            qtHouseholdNo = QStandardItem( "%i" % row[0])
            qtHouseholdNo.setTextAlignment( Qt.AlignCenter )
            
            qtHouseholdName = QStandardItem( row[1] )
            
            qtAssetValue = QStandardItem( "%i" % row[2] )
            qtAssetValue.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
            
            qtIncomeValue = QStandardItem( "%i" % row[3] )
            qtIncomeValue.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
            
            qtExpenditure = QStandardItem( "%i" % row[4] )
            qtExpenditure.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
            
            qtDateCollected = QStandardItem( QDate(row[5]).toString("dd/MM/yyyy") )
            qtDateCollected.setTextAlignment( Qt.AlignCenter )
            
            model.setItem( num, 0, qtHouseholdNo )
            model.setItem( num, 1,  qtHouseholdName )
            model.setItem( num, 2, qtAssetValue )
            model.setItem( num, 3, qtIncomeValue )
            model.setItem( num, 4, qtExpenditure )
            model.setItem( num, 5, qtDateCollected )
            num = num + 1
        
        self.tableView.setModel(model)

