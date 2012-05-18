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


from includes.xlwt import Workbook, easyxf
from time import time
import os
from PyQt4 import QtGui

class HouseholdsIncomeWrite:
    #def __init__(self):
        #self.database = Database()

    def writeSpreadsheetReport(self,reporttable,simreporttable):
        reporttype = 'Disposable Income Simulation'
        
        book = Workbook(encoding="utf-8") 
        sheet1 = book.add_sheet("Household Disposable Income")
        style1 = easyxf('font: name Arial;''font: bold True;')


        #Write Table Title
        reptitle = "%s" % reporttype
        sheet1.write(0, 0, reptitle, style1) 
        sheet1.col(0).width = 2500
        
        #write Headers
        sheet1.write(2, 0, 'hhid', style1)
        
        sheet1.write(2, 1, 'Normal DIncome', style1)
        sheet1.write(2, 2, 'Simulation DIncome', style1)
        sheet1.col(1).width = 6000

        #write Data 
        myrow = 3
        print simreporttable
        counter = len(reporttable)
        for i in range(0,counter):
                       
            hhid = reporttable[i][0]
            householdDI = reporttable[i][1]
            simhouseholdDI = simreporttable[i][1]

            sheet1.write(myrow, 0, int(hhid))
            
            sheet1.write(myrow, 1, float(householdDI))
            sheet1.write(myrow, 2, float(simhouseholdDI))
            myrow = myrow + 1
                
        folder = "outputs/spreadsheets/income_sources/"
        filename =  folder + "openihm_SimulatedDisposableIncome-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)
