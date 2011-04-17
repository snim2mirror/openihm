#-------------------------------------------------------------------	
#	Filename: report_disposableincome_write.py
#-------------------------------------------------------------------

from xlwt import Workbook, easyxf
from time import time
import os
from PyQt4 import QtGui

class HouseholdsIncomeWrite:
    #def __init__(self):
        #self.database = Database()

    def writeSpreadsheetReport(self,reporttable,reporttype):
        
        book = Workbook(encoding="utf-8") 
        sheet1 = book.add_sheet("Household Disposable Income")
        style1 = easyxf('font: name Arial;''font: bold True;')


        #Write Table Title
        reptitle = "%s" % reporttype
        sheet1.write(0, 0, reptitle, style1) 
        sheet1.col(0).width = 2500
        sheet1.col(1).width = 4500
        #write Headers
        
            
        sheet1.write(2, 0, 'hhid', style1)
        sheet1.write(2, 1, 'Disposable Income', style1)
        if reporttype=='Living Threshold':
            sheet1.write(2, 2, 'Above STOL', style1)

        #write Data 
        myrow = 3
        for row in reporttable:
            hhid = row[0]
            householdDI = row[1]

            sheet1.write(myrow, 0, int(hhid))
            sheet1.write(myrow, 1, float(householdDI))
            
            if reporttype=='Living Threshold':
                incomeLessExpenses = row[2]
                if incomeLessExpenses > 0:
                    sheet1.write(myrow, 2, float(incomeLessExpenses))
            
            myrow = myrow + 1
                
        folder = "outputs/spreadsheets/income_sources/"
        filename =  folder + "openihm_DisposableIncome-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)
