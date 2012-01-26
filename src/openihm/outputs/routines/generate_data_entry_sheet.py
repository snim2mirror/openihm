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

import os
from includes.xlwt import Workbook, easyxf
import includes.mysql.connector as connector # FIXME: DO we need this?
from data.config import Config
from PyQt4 import QtGui
from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager

class DataEntrySheets:
    def __init__(self,projectid):
        self.database = Database()
        self.pcharstable = 'p' + str(projectid) +'PersonalCharacteristics'
        self.hcharstable = 'p' + str(projectid) +'HouseholdCharacteristics'
        self.pid = projectid
        self.config = Config.dbinfo().copy()

    
    def getPersonalCharacteristics(self):
        query = '''SELECT characteristic, datatype FROM projectcharacteristics WHERE pid=%s and chartype='Personal' ''' %(self.pid)
        self.database.open()
        pchars = self.database.execSelectQuery(query)
        self.database.close()
        return pchars
        

    def getHouseholdCharacteristics(self):
        query = '''SELECT characteristic, datatype FROM projectcharacteristics WHERE pid=%s and chartype='Household' ''' %(self.pid)
        self.database.open()
        hchars = self.database.execSelectQuery(query)
        self.database.close()
        return hchars

        # Income sources
    def buildQueries(self,incometype):
        query = '''SELECT incomesource FROM projectincomesources WHERE incometype='%s' AND pid=%s''' % (incometype,self.pid)
        return query

    def getincomeSources(self,query):
        '''run various select queries'''
        
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recordset
    
    def getprojetAssets(self):
        query = '''SELECT assettype, assetname FROM projectassets WHERE pid=%s ORDER BY assettype, assetname''' % self.pid
        self.database.open()
        assets = self.database.execSelectQuery(query)
        self.database.close()
        return assets
    
    def addProjectAssets(self,book,style2):
        ''' Populate Sheet 3 with Assets for a selected project'''
        sheet4 = book.add_sheet("Assets")
        sheet4.write(1, 0, "Asset Type", style2)
        sheet4.write(1, 1, "Asset Name", style2)

        #set column width for sheet3 - Asset Columns
        for i in range(0,2):
            sheet4.col(i).width = 6000

        recordset = self.getprojetAssets()
        row = 2
        for rec in recordset:
            col = 0
            assettype = rec[0]
            assetname = rec[1]
            sheet4.write(row, col, assettype)
            col = col + 1
            sheet4.write(row, col, assetname)
            row = row + 1
    
    def populateIncomeSourcesSheet(self,book,style2):
        ''' Populate Sheet 3 with income sources for a selected project'''
        
        #Income Sources
        sheet3 = book.add_sheet("Income Sources")
        sheet3.write(1, 0, "Crop Types", style2)
        sheet3.write(1, 2, "Employment Types", style2)
        sheet3.write(1, 4, "Livestock Types", style2)
        sheet3.write(1, 6, "Transfer Types", style2)
        sheet3.write(1, 8, "Wild Food Types", style2)

        #set column width for sheet3
        for i in range(0,10,2):
            sheet3.col(i).width = 6000

        incometypes = ['crops','employment','livestock','transfers','wildfoods']
        col = 0

        for incometype in incometypes:
            row = 2
            query = self.buildQueries(incometype)
            recordset = self.getincomeSources(query)

            for rec in recordset:
                cellvalue = rec[0]
                sheet3.write(row, col, cellvalue)
                row = row + 1
            col = col + 2
    
    def writeDataSheets(self):
        book = Workbook(encoding="utf-8")
        
        #set style for headers
        style1 = easyxf('font: name Arial;''font: bold True;')
        style2 = easyxf('font: name Arial;''font: colour ocean_blue;''font: bold True;''border: left thick, top thick, right thick, bottom thick')
        style3 = easyxf('font: name Arial;''font: colour green;''font: bold True;''border: left thick, top thick, right thick, bottom thick')

        #create sheet for entering project households
        #projectid = self.pid
        sheettitle = "%s" % self.pid
        sheet1 = book.add_sheet(sheettitle)
        sheet1.write(0, 0, "Project Households", style1)
        sheet1.write(1, 0, "HouseholdNumber", style2)
        sheet1.write(1, 1, "HouseholdName", style2)
        sheet1.write(1, 2, "DateVisited", style2)

        #set column width for sheet1
        for i in range(0,3):
            sheet1.col(i).width = 6000

        #Basic Details for Household Members
        sheet2 = book.add_sheet("Template")
        sheet2.write(1, 0, "HouseholdMembers", style1)
        sheet2.write(2, 0, "Sex", style2)
        sheet2.write(2, 1, "Age", style2)
        sheet2.write(2, 2, "YearofBirth", style2)
        sheet2.write(2, 3, "HouseholdHead", style2)
        sheet2.write(2, 4, "PeriodAway", style2)

        #get personal and household characteristics, configured for current project
        pchars = self.getPersonalCharacteristics()
        hchars = self.getHouseholdCharacteristics()

        #section for extended personal characteristics
        col = 0
        sheet2.write(8, 0, "PersonalCharacteristics", style1)
        sheet2.write(9, col, 'personid', style2)
        sheet2.write(10, col, 'String', style3)
        col = col + 1

        for char in pchars:
            value = char[0]
            chartype = char[1]
            vartype =''
            if value!='pid' and value !='hhid':
                if chartype == 1:
                    vartype ='Yes/No'
                elif chartype == 2:
                    vartype ='Integer'
                elif chartype == 3:
                    vartype ='String'
                elif chartype == 4:
                    vartype ='Double'
                sheet2.write(9, col, value, style2)
                sheet2.write(10, col, vartype, style3)
                col = col + 1
                
        #section for household characteristics
        sheet2.write(17, 0, "HouseholdCharacteristics", style1)
        col = 0
        for char in hchars:
            value = char[0]
            chartype = char[1]
            vartype =''
            if value!='pid' and value !='hhid':
                if chartype == 1:
                    vartype ='Yes/No'
                elif chartype == 2:
                    vartype ='Integer'
                elif chartype == 3:
                    vartype ='String'
                elif chartype == 4:
                    vartype ='Double'

                sheet2.write(18, col, value, style2)
                sheet2.write(19, col, vartype, style3)
                col = col + 1

        headerrow = 25
        itemrow = 26

        #Assets
        sheet2.write(headerrow, 0, "Assets", style1)
        sheet2.write(itemrow, 0, "Category", style2)
        sheet2.write(itemrow, 1, "Type", style2)
        sheet2.write(itemrow, 2, "Unit", style2)
        sheet2.write(itemrow, 3, "UnitCost", style2)
        sheet2.write(itemrow, 4, "Units", style2)

        #Expenditure
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "Expenditure", style1)
        sheet2.write(itemrow, 0, "Type", style2)
        sheet2.write(itemrow, 1, "Unit", style2)
        sheet2.write(itemrow, 2, "KCalPerUnit", style2)
        sheet2.write(itemrow, 3, "UnitCost", style2)
        sheet2.write(itemrow, 4, "Units", style2)

        #Crop Income
        headerrow = headerrow + 11
        itemrow = itemrow + 11

        sheet2.write(headerrow, 0, "Crops", style1)
        sheet2.write(itemrow, 0, "Name", style2)
        sheet2.write(itemrow, 1, "Unit", style2)
        sheet2.write(itemrow, 2, "UnitsProduced", style2)
        sheet2.write(itemrow, 3, "UnitsSold", style2)
        sheet2.write(itemrow, 4, "UnitPrice", style2)
        sheet2.write(itemrow, 5, "OtherUses", style2)
        sheet2.write(itemrow, 6, "UnitsConsumed", style2)

        #Livestock
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "Livestock-C", style1)
        sheet2.write(itemrow, 0, "Name", style2)
        sheet2.write(itemrow, 1, "Unit", style2)
        sheet2.write(itemrow, 2, "UnitsProduced", style2)
        sheet2.write(itemrow, 3, "UnitsSold", style2)
        sheet2.write(itemrow, 4, "UnitPrice", style2)
        sheet2.write(itemrow, 5, "OtherUses", style2)
        sheet2.write(itemrow, 6, "UnitsConsumed", style2)
        						
        #WildFoods
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "WildFoods", style1)
        sheet2.write(itemrow, 0, "Name", style2)
        sheet2.write(itemrow, 1, "Unit", style2)
        sheet2.write(itemrow, 2, "UnitsProduced", style2)
        sheet2.write(itemrow, 3, "UnitsSold", style2)
        sheet2.write(itemrow, 4, "UnitPrice", style2)
        sheet2.write(itemrow, 5, "OtherUses", style2)
        sheet2.write(itemrow, 6, "UnitsConsumed", style2)

        #Employment
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "Employment", style1)
        sheet2.write(itemrow, 0, "Type", style2)
        sheet2.write(itemrow, 1, "FoodPaid", style2)
        sheet2.write(itemrow, 2, "Unit", style2)
        sheet2.write(itemrow, 3, "UnitsPaid", style2)
        sheet2.write(itemrow, 4, "Kcals", style2)
        sheet2.write(itemrow, 5, "CashIncome", style2)

        #Social Transfers
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "SocialTransfer", style1)
        sheet2.write(itemrow, 0, "TransferSource", style2)
        sheet2.write(itemrow, 1, "CashPerYear", style2)
        sheet2.write(itemrow, 2, "FoodType", style2)
        sheet2.write(itemrow, 3, "Unit", style2)
        sheet2.write(itemrow, 4, "UnitsConsumed", style2)
        sheet2.write(itemrow, 5, "UnitsSold", style2)
        sheet2.write(itemrow, 6, "PricePerUnit", style2)

        #Transfers from Organisations
        headerrow = headerrow + 11
        itemrow = itemrow + 11
        
        sheet2.write(headerrow, 0, "TransferFromOrganisations", style1)
        sheet2.write(itemrow, 0, "TransferSource", style2)
        sheet2.write(itemrow, 1, "CashPerYear", style2)
        sheet2.write(itemrow, 2, "FoodType", style2)
        sheet2.write(itemrow, 3, "Unit", style2)
        sheet2.write(itemrow, 4, "UnitsConsumed", style2)
        sheet2.write(itemrow, 5, "UnitsSold", style2)
        sheet2.write(itemrow, 6, "PricePerUnit", style2)

        #set column width for sheet2
        for i in range(0,7):
            sheet2.col(i).width = 6000
            
        self.populateIncomeSourcesSheet(book,style1)
        self.addProjectAssets(book,style1)

        folder = "inputs/"
        filename = folder + "dataEntrySheet-ProjectID-" + str(self.pid) + ".xls"
        book.save(filename)
        completionmessage = '''Template Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Data Entry Template', completionmessage)
 
        #
        os.system(os.path.curdir + "\\inputs\\dataEntrySheet-ProjectID-" + str(self.pid) + ".xls")
        
        
