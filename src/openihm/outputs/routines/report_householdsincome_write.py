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

    def writeSpreadsheetReport(self,reporttable,reporttype):
        
        book = Workbook(encoding="utf-8") 
        sheet1 = book.add_sheet("Households By Income Source")
        style1 = easyxf('font: name Arial;''font: bold True;')

        #Write Table Title
        reptitle = "%s" % reporttype
        sheet1.write(0, 0, reptitle, style1) 
        sheet1.col(0).width = 1500
        #write Headers
        i = 1
        if len(reporttable)!=0:
            row = reporttable[0]
            keylist = row.keys()
            keylist.sort()
            for key in keylist:
                if key !='incometotal':
                    if key =='hhid':
                        sheet1.write(2, 0, key, style1)
                        #sheet1.col(0).width = 1500
                    else:
                        sheet1.write(2, i, key,style1)
                        sheet1.col(i).width = 5500
                        i = i + 1

            #write Data 
            myrow = 3
            mycol = 1
            for row in reporttable:
                for key in keylist:
                    if key !='incometotal':
                    #for key in row.keys():
                        if row[key]:
                            value = row[key]
                        else:
                            value = 0
                        if key =='hhid':
                            sheet1.write(myrow, 0, float(value))
                        else:
                            sheet1.write(myrow, mycol, float(value))
                            mycol = mycol + 1
                mycol =1
                myrow = myrow + 1
                
        folder = "outputs/spreadsheets/income_sources/"
        filename =  folder + "openihm_incomesources-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)
