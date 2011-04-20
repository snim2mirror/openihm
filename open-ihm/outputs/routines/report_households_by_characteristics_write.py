#-------------------------------------------------------------------	
#	Filename: report_households_by_characteristics_write.py
#-------------------------------------------------------------------

import xlwt
from time import time
import os
from PyQt4 import QtGui

class HouseholdsByCharacteristicsWrite:
    #def __init__(self):
        #self.database = Database()

    def writeSpreadsheetReport(self,reporttable):
        book = xlwt.Workbook(encoding="utf-8") 

        sheet1 = book.add_sheet("Households By Characteristics")
        sheet1.write(0, 0, "Household ID")
        sheet1.write(0, 1, "Name of Household")
        i = 1
        for row in reporttable:
            sheet1.write(i, 0, "%s" % row[0])
            sheet1.write(i, 1, "%s" % row[1])
            i = i + 1

        folder = "outputs/spreadsheets/"
        filename =  folder + "openihm_ProjectHouseholdsByCharacteristics-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)

        
