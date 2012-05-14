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
from includes.xlrd import open_workbook
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

    def getProjectCropsFoods(self,incometype,projectincomes):
        incomes = []
        for income in projectincomes:
            tempname = "'" + income[0] + "'"
            incomes.append(tempname)

        incomesourcelist = ','.join(incomes)
        query = '''SELECT name, unitofmeasure FROM  setup_foods_crops WHERE  category='%s' AND name in (%s)''' % (incometype,incomesourcelist)
        recordset = self.getincomeSources(query)
        
        return recordset

    def getincomeSources(self,query):
        '''run various select queries'''
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recordset

    def getCropsFoodsIncomeSourceDetails(self,incometype):
        '''Get Income-source Names and Units of Measure for Crops, Livestocks, and Wildfoods, to be displayed in data entry spreadsheet'''
        incomesquery = self.buildQueries(incometype)
        projectincomes = self.getincomeSources(incomesquery)
        incomesourcedetails = self.getProjectCropsFoods(incometype,projectincomes)
        return incomesourcedetails

    def getprojetAssets(self):
        query = '''SELECT assettype, assetname FROM projectassets WHERE pid=%s ORDER BY assettype, assetname''' % self.pid
        self.database.open()
        assets = self.database.execSelectQuery(query)
        self.database.close()
        return assets
    
    def getProjectSocialTransfers(self):
        query = '''SELECT incomesource FROM projectincomesources WHERE incometype ='transfers' AND pid=%s ORDER BY incomesource''' % self.pid
        self.database.open()
        transfers = self.database.execSelectQuery(query)
        self.database.close()
        return transfers

    def getProjectOfficialTransfers(self):
        query = '''SELECT incomesource FROM projectincomesources WHERE incometype ='officialtransfer' AND pid=%s ORDER BY incomesource''' % self.pid
        self.database.open()
        transfers = self.database.execSelectQuery(query)
        self.database.close()
        return transfers

    def populateSocialTranfers(self,book,style1,style2,row):
        recordset = self.getProjectSocialTransfers()
        sheet = book.get_sheet(1)
        col = 0
        #set section Headings
        transferheadings = ["TransferSource","CashPerYear","FoodType","Unit","UnitsConsumed","UnitsSold","PricePerUnit"]
        for itemheader in transferheadings:
            sheet.write(row, col, itemheader, style2)
            col = col + 1
        row = row +1

        #write transfer sources
        col = 0
        for rec in recordset:
            celvalue = rec[col]
            sheet.write(row, col, celvalue)
            row = row + 1
        row = row + 4 # set space between Income source type sections
        return row

    def populateOfficialTranfers(self,book,style1,style2,row):
        recordset = self.getProjectSocialTransfers()
        sheet = book.get_sheet(1)
        col = 0
        #set section Headings
        transferheadings = ["TransferSource","CashPerYear","FoodType","Unit","UnitsConsumed","UnitsSold","PricePerUnit"]
        for itemheader in transferheadings:
            sheet.write(row, col, itemheader, style2)
            col = col + 1
        row = row +1

        #write transfer sources
        col = 0
        for rec in recordset:
            celvalue = rec[col]
            sheet.write(row, col, celvalue)
            row = row + 1
        row = row + 4 # set space between Income source type sections
        return row

    
    def getAssetUnitOfMeasure(self,unitfld, tblname,assetfld,assettype):
        unitofmeasure =""
        query = '''SELECT %s FROM %s WHERE %s='%s' ''' % (unitfld, tblname,assetfld,assettype)
        self.database.open()
        assets = self.database.execSelectQuery(query)
        
        for item in assets:
            unitofmeasure = item[0]
        self.database.close()
        return unitofmeasure

    def getAssetList(self):
        assets = []
        assets = self.getprojetAssets()
        finalassetlist = []
        for row in assets:
            templist = []
            for item in row:
                templist.append(item)
                
            if templist [0] =='Crops':
                tblname, assetfld, unitfld = "setup_crops", "foodtype", "measuringunit"
            elif templist [0] =='Land':
                tblname, assetfld, unitfld = "setup_landtypes", "landtype", "unitofmeasure"
            elif templist [0] =='Livestock':
                tblname, assetfld, unitfld = "setup_livestock", "incomesource", "unitofmeasure"
            elif templist [0] =='Tradable Goods':
                tblname, assetfld, unitfld = "setup_tradablegoods", "tradablegoodtype", "unitofmeasure"
            elif templist [0] =='Trees':
                tblname, assetfld, unitfld = "setup_treetypes", "treetype", "measuringunit"
            unitofmeasure = self.getAssetUnitOfMeasure(unitfld, tblname,assetfld,templist[1])
            templist.append(unitofmeasure)
            listtuple = tuple(templist)
            finalassetlist.append(listtuple)
        return finalassetlist
    
    def addProjectAssets(self,book,style1,style2):
        ''' Populate Sheet 3 with Assets for a selected project'''
        sheet4 = book.add_sheet("New Assets")
        headings = ["Category","Type","Unit","UnitCost","NumberOfUnits"]
        col = 0
        row = 0
        sheet4.write(row, col, "Assets", style1)
        row = row + 1
        for itemheader in headings:
            sheet4.write(row, col, itemheader, style2)
            col = col + 1
        row = row +1

        #set column width for sheet4 - Asset Columns
        for i in range(0,5):
            sheet4.col(i).width = 6000

    def populateProjectAssetssection(self,book,style1,style2,row):
        headings = ["Category","Type","Unit","UnitCost","TotalUnits"]
        col = 0
        sheet = book.get_sheet(1)
        for itemheader in headings:
            sheet.write(row, col, itemheader, style2)
            col = col + 1
        row = row +1
        
        recordset = self.getAssetList()
        for rec in recordset:
            col = 0
            assettype = rec[0]
            assetname = rec[1]
            unitofmeasure = rec[2]
            sheet.write(row, col, assettype)
            col = col + 1
            sheet.write(row, col, assetname)
            col = col + 1
            sheet.write(row, col, unitofmeasure)
            row = row + 1
        return row

    def writeFoodsCropsHeaders(self,sectionheading,headerrow,book,style1,style2):

        headings = ["Name","Unit","UnitsProduced","UnitsSold","UnitPrice","OtherUses","UnitsConsumed"]
        col = 0
        sheet = book.get_sheet(1)
        #if sectionheading=='Livestock':
        sectionheading = sectionheading + '-C'
        sheet.write(headerrow, col, sectionheading,style1)
        headerrow = headerrow +1
            
        for itemheader in headings:
            sheet.write(headerrow, col, itemheader, style2)
            col = col + 1

        headerrow = headerrow +1
        return headerrow

    def populateFoodsCropsSections(self,book,style1,style2,row):
        ''' Populate data Entry Sheet with Crops,Livestock,Wildfoods for a selected project'''

        incometypes = ['Crops','Livestock','Wildfoods']
        col = 0
        for incometype in incometypes:
            #set section Headings
            row = self.writeFoodsCropsHeaders(incometype,row,book,style1,style2)
            
            #get incomesource details and write in spreadsheet
            recordset = self.getCropsFoodsIncomeSourceDetails(incometype.lower())
            sheet = book.get_sheet(1)

            for rec in recordset:
                for col in range (0,2):
                    celvalue = rec[col]
                    sheet.write(row, col, celvalue)
                row = row + 1
                
            row = row + 4 # set space between Income source type sections
        return row

    def writeEmploymentSectionHeaders(self,headerrow,book,style1,style2):

        headings = ["Type","FoodPaid","Unit","UnitsPaid","Kcals","CashIncome"]
        col = 0
        sheet = book.get_sheet(1)
        sheet.write(headerrow, 0, "Employment", style1)
        headerrow = headerrow +1
        for itemheader in headings:
            sheet.write(headerrow, col, itemheader, style2)
            col = col + 1

        headerrow = headerrow +1
        return headerrow

    def getProjectEmploymentTypes(self):
        incometype = 'employment'
        query = self.buildQueries(incometype)
        recordset = self.getincomeSources(query)
        return recordset

    def populateEmployemntDetails(self,row,book,style1,style2):
        row = self.writeEmploymentSectionHeaders(row,book,style1,style2)
        recordset = self.getProjectEmploymentTypes()
        sheet = book.get_sheet(1)

        col = 0
        for rec in recordset:
            celvalue = rec[col]
            sheet.write(row, col, celvalue)
            row = row + 1
        row = row + 4 # set space between Income source type sections
        return row
            
    def populateIncomeSourcesSheet(self,book,style1,style2):
        ''' Populate Sheet 3 with Headers for ebtry of new income sources users may find during field visits'''
        
        #Income Sources
        sheet3 = book.add_sheet("New Income Sources")
        incometypes = ['Crops','Livestock','Wildfoods']
        col = 0
        headerrow = 0
        for incometype in incometypes:
            #set section Headings
            headings = ["Name","Unit","UnitsProduced","UnitsSold","UnitPrice","OtherUses","UnitsConsumed"]
            col = 0
            sheet3.write(headerrow, 0,incometype , style1)
            headerrow = headerrow +1
            for itemheader in headings:
                sheet3.write(headerrow, col, itemheader, style2)
                col = col + 1
            headerrow = headerrow +11

        #Write Employment Headings
        employmentheadings = ["Type","FoodPaid","Unit","UnitsPaid","Kcals","CashIncome"]
        col = 0
        sheet3.write(headerrow, 0, "Employment", style1)
        headerrow = headerrow +1
        for itemheader in employmentheadings:
            sheet3.write(headerrow, col, itemheader, style2)
            col = col + 1
        headerrow = headerrow +11

        #Write Transfer Headers
        incometypes = ['Social Transfers','Official Transfers']
        col = 0
        for incometype in incometypes:
            #set section Headings
            transferheadings = ["TransferSource","CashPerYear","FoodType","Unit","UnitsConsumed","UnitsSold","PricePerUnit"]
            col = 0
            sheet3.write(headerrow, 0,incometype , style1)
            headerrow = headerrow +1
            for itemheader in transferheadings:
                sheet3.write(headerrow, col, itemheader, style2)
                col = col + 1
            headerrow = headerrow +11

        sheet3.write(headerrow, 0, "")
        #set column width for sheet1
        for i in range(0,7):
            sheet3.col(i).width = 6000
    
    def writeDataSheets(self):
        book = Workbook(encoding="utf-8")
        
        #set style for headers
        style1 = easyxf('font: name Arial;''font: bold True;')
        style2 = easyxf('font: name Arial;''font: colour ocean_blue;''font: bold True;''border: left thick, top thick, right thick, bottom thick')
        style3 = easyxf('font: name Arial;''font: colour green;''font: bold True;''border: left thick, top thick, right thick, bottom thick')

        #create sheet for entering project households
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
        headerrow = headerrow + 1
        headerrow = self.populateProjectAssetssection(book,style1,style2,headerrow)
        
        #Expenditure
        headerrow = headerrow + 5
        sheet2.write(headerrow, 0, "Expenditure", style1)
        headerrow = headerrow + 1
        sheet2.write(headerrow, 0, "Type", style2)
        sheet2.write(headerrow, 1, "Unit", style2)
        sheet2.write(headerrow, 2, "KCalPerUnit", style2)
        sheet2.write(headerrow, 3, "UnitCost", style2)
        sheet2.write(headerrow, 4, "Units", style2)

        #Crop, Livestock, and Wildfood Income
        headerrow = headerrow + 11
        headerrow = self.populateFoodsCropsSections(book,style1,style2,headerrow)

        #Employment
        headerrow = self.populateEmployemntDetails(headerrow,book,style1,style2)
        
        #Social Transfers
        headerrow = self.populateSocialTranfers(book,style1,style2,headerrow)

        #Transfers from Organisations
        #headerrow = self.populateOfficialTranfers(book,style1,style2,headerrow) - ACTIVATE THIS

        #set column width for sheet2
        for i in range(0,7):
            sheet2.col(i).width = 6000
            
        self.populateIncomeSourcesSheet(book,style1,style2)
        self.addProjectAssets(book,style1,style2)

        folder = "inputs/"
        filename = folder + "dataEntrySheet-ProjectID-" + str(self.pid) + ".xls"
        book.save(filename)
        completionmessage = '''Template Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Data Entry Template', completionmessage)
 
        #
        os.system(os.path.curdir + "\\inputs\\dataEntrySheet-ProjectID-" + str(self.pid) + ".xls")
        
        
