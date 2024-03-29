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

class HouseholdBudgetWrite:
    def drawBudgetTemplate(self):
        pass
        
    def writePageTitleSection(self,sheetName,style1):
        #Write Table Title
        reptitle = "Household Budget"
        sheetName.write(0, 0, reptitle, style1) 
        sheetName.col(0).width = 15000
        #set column width for cols 1 to 3
        for i in range(1,4):
            sheetName.col(i).width = 5000
        
    def writeHouseholdMembership(self,HouseholdMembership,sheetName,sectionrow,style1,style2,style3):
        
        #write Headers
        sheetName.write(2, 0, 'Household Number:', style1)
        sheetName.write(4, 0, 'Household Membership:', style1)
        sheetName.write(4, 1, 'Male', style1)
        sheetName.write(4, 2, 'Female', style1)
        sheetName.write(5, 1, 'Age - years', style1)
        sheetName.write(5, 2, 'Age - years', style1)

        #write details of Household members
        sectionrow = 6
        for row in HouseholdMembership:
            if row[1]=='Male':
                sheetName.write(sectionrow, 1, row[2], style3)
            else:
                sheetName.write(sectionrow, 2, row[2], style3)
            
            sectionrow = sectionrow + 1

        return sectionrow
    
    def writeAssetDetails(self,householdAssets,sheetName,sectionrow,style1,style2,style3):
        #Assets
        headerrow = sectionrow + 5
        itemrow = headerrow + 1
        
        sheetName.write(headerrow, 0, "Assets", style1)
        assetHeaders = ['Category','Type','Unit','Value']
        itemcolumn = 0
        for assetHeader in assetHeaders:
            sheetName.write(itemrow, itemcolumn, assetHeader, style2) 
            itemcolumn = itemcolumn + 1

        #write Asset Details
        itemrow = itemrow + 1
        for row in householdAssets:
            rowindex = 0
            for i in range(0,4):
                rowindex = i +1
                sheetName.write(itemrow, i, row[rowindex], style3)
            itemrow = itemrow + 1
            
        return itemrow

    def writeHouseholdIncome(self,householdCashIncome,householdFoodIncome,sheetName,sectionrow,style1,style2,style3):
        #Income Sources - Headers
        headerrow = sectionrow + 5
        itemrow = headerrow + 1
        
        sheetName.write(headerrow, 0, "Income", style1)
        sheetName.write(itemrow, 0, "Income Source", style2)
        sheetName.write(itemrow, 1, "Food (Kcal)", style2)
        
        cashtitle =  "Cash - " #+ projectcurrency
        sheetName.write(itemrow, 2, cashtitle, style2) 


        #Income Sources - Category Titles
        IncomeSourceTitles = ['Crop production','Employment','Livestock & livestock products','Gifts','Wild foods & hunting','Total']
        for incomecat in IncomeSourceTitles:
            itemrow = itemrow + 1
            sheetName.write(itemrow, 0, incomecat, style2)

        #Income Sources - Category Values - Food
        itemrow = headerrow + 2
        for i in range(1,7):
            sheetName.write(itemrow,1, householdFoodIncome[i], style3)
            itemrow = itemrow + 1
            
        #Income Sources - Category Values - Cash
        itemrow = headerrow + 2
        for i in range(1,7):
            sheetName.write(itemrow,2, householdCashIncome[i], style3)
            itemrow = itemrow + 1
            
        return itemrow

    def writeFinalSummary(self,householdBudgetSummary,sheetName,sectionrow,style1,style2,style3):
        #The Household Budget
        headerrow = sectionrow + 5
        itemrow = headerrow + 2
        sheetName.write(headerrow, 0, "The Household Budget", style1)
        budgetTitles = ['Household food energy requirement','% household food requirement met from own production',
                              'Cost of food purchase to meet household requirement','% of food deficit which can be afforded',
                              'Cash remaining after food purchase','Cost of non-food expenses','% of non-food expenses which can be met',
                              'Cash remaining after non-food expenses','Kcals/resident person/day']
        
        for incomecat in budgetTitles:
            sheetName.write(itemrow, 0, incomecat, style2)
            itemrow = itemrow + 1
            
        itemrow = sectionrow + 7
        for i in range (1,9):
            sheetName.write(itemrow, 1, householdBudgetSummary[i], style3)
            itemrow = itemrow + 1
            

    def saveReport(self,book):
        folder = "outputs/spreadsheets/income_sources/"
        filename =  folder + "openihm_HouseholdBudget-" + str(time()) + ".xls"
        book.save(filename)
       
        completionmessage = '''Report Table Spreadsheet Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Report Table', completionmessage)
        filepath= os.path.relpath(filename,start='.')
        
        os.system(filepath)

    def writeSpreadsheetReport(self,selectedHouseholds,householdMembership,householdAssets,householdCashIncome,householdFoodIncome,householdBudgetSummary):
        book = Workbook(encoding="utf-8")
        style1 = easyxf('font: name Arial;''font: bold True;' 'border: left thick, top thick, right thick, bottom thick')
        style2 = easyxf('font: name Arial;''font: colour ocean_blue;''font: bold True;''border: left thin, top thin, right thin, bottom thin')
        style3 = easyxf('font: name Arial;''border: left thin, top thin, right thin, bottom thin')
        style4 = easyxf('font: name Arial;''font: colour green;''font: bold True;''border: left thick, top thick, right thick, bottom thick')

        sheetNumber = 1
        listIndex = 0

        for hid in selectedHouseholds:
            sheetName = 'sheet' + '%s' % sheetNumber
            sheetNumber = sheetNumber + 1
            sheetTitle = 'Household Number ' + '%s' % hid
            sheetName = book.add_sheet(sheetTitle)
            
            sectionrow = self.writePageTitleSection(sheetName,style1)
            sectionrow = self.writeHouseholdMembership(householdMembership[listIndex],sheetName,sectionrow,style1,style2,style3)
            sectionrow = self.writeAssetDetails(householdAssets[listIndex],sheetName,sectionrow,style1,style2,style3)
            sectionrow = self.writeHouseholdIncome(householdCashIncome[listIndex],householdFoodIncome[listIndex],sheetName,sectionrow,style1,style2,style3)
            self.writeFinalSummary(householdBudgetSummary[listIndex],sheetName,sectionrow,style1,style2,style3)
            listIndex = listIndex + 1
            
        self.saveReport(book)

