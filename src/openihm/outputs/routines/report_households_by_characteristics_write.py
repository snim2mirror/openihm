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


import includes.xlwt
from time import time
import os
from PyQt4 import QtGui

class HouseholdsByCharacteristicsWrite:
    #def __init__(self):
        #self.database = Database()

    def writeSpreadsheetReport(self,reporttable):
        book = includes.xlwt.Workbook(encoding="utf-8") 

        sheet1 = book.add_sheet("Households By Characteristics")
        sheet1.write(0, 0, "Household ID")
        sheet1.write(0, 1, "Name of Household")
        i = 1
        sheet1.col(0).width = 5500
        sheet1.col(1).width = 5500
        for row in reporttable:
            sheet1.write(i, 0, "%s" % row[1])
            sheet1.write(i, 1, "%s" % row[2])
            i = i + 1

        sheet1.col(0).width = 5500
        sheet1.col(1).width = 5500

        folder = "outputs/spreadsheets/"
        filename =  folder + "openihm_ProjectHouseholdsByCharacteristics-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)

        
