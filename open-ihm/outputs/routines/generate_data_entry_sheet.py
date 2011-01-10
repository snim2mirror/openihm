#-------------------------------------------------------------------	
#	Filename: generate_data_entry_sheet.py
#-------------------------------------------------------------------
import os
from xlwt import Workbook, easyxf
import data.mysql.connector
from data.config import Config
from PyQt4 import QtGui
from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager

class DataEntrySheets:
    def __init__(self,projectid):
        self.database = Database()
        self.pcharstable = 'p' + str(projectid) +'personalcharacteristics'
        self.hcharstable = 'p' + str(projectid) +'householdcharacteristics'
        self.pid = projectid
        self.config = Config.dbinfo().copy()

    def getPersonalCharacteristics(self):
        query = '''SHOW columns FROM %s''' %(self.pcharstable)
        self.database.open()
        pchars = self.database.execSelectQuery(query)
        self.database.close()
        return pchars
        

    def getHouseholdCharacteristics(self):
        query = '''SHOW columns FROM %s''' %(self.hcharstable)
        self.database.open()
        hchars = self.database.execSelectQuery(query)
        self.database.close()
        return hchars
    
    def writeDataSheets(self):
        book = Workbook(encoding="utf-8")
        
        #set style for headers
        style1 = easyxf('font: name Arial;''font: bold True;')
        style2 = easyxf('font: name Arial;''font: colour ocean_blue;''font: bold True;''border: left thick, top thick, right thick, bottom thick')
        style3 = easyxf('font: name Arial;''font: colour green;''font: bold True;''border: left thick, top thick, right thick, bottom thick')

        
        
        #create sheet for entering project households
        #projectid = self.pid
        sheettitle = "%s" % self.pid
        print self.pid
        sheet1 = book.add_sheet(sheettitle)
        sheet1.write(0, 0, "Project Households", style1)
        sheet1.write(1, 0, "HouseholdNumber", style2)
        sheet1.write(1, 1, "HouseholdName", style2)
        sheet1.write(1, 2, "DateVisited", style2)

        #Basic Details for Household Members
        sheet2 = book.add_sheet("Template")
        sheet2.write(1, 0, "HouseholdMembers", style1)
        sheet2.write(2, 0, "Sex", style2)
        sheet2.write(2, 1, "Age", style2)
        sheet2.write(2, 2, "YearofBirth", style2)
        sheet2.write(2, 3, "HouseholdHead", style2)

        #set column width for sheet1
        for i in range(0,3):
            sheet1.col(i).width = 6000

        #get personal and household characteristics, configured for current project
        pchars = self.getPersonalCharacteristics()
        hchars = self.getHouseholdCharacteristics()

        #section for extended personal characteristics
        sheet2.write(8, 0, "PersonalCharacteristics", style1)
        col = 0
        for char in pchars:
            value = char[0]
            typep = char[1]
            if value!='pid' and value !='hhid':
                stringvar = 'varchar'
                boolvar = 'enum'
                intvar = 'bigint'
                doublevar ='double'
                if typep.startswith(tuple(stringvar)):
                    vartype ='String'
                elif typep.startswith(tuple(boolvar)):
                    vartype ='Yes/No'
                elif typep.startswith(tuple(intvar)):
                    vartype ='Integer'
                elif typep.startswith(tuple(doublevar)):
                    vartype ='Double'

                sheet2.write(9, col, value, style2)
                sheet2.write(10, col, vartype, style3)
                col = col + 1
                
        #section for household characteristics
        sheet2.write(17, 0, "HouseholdCharacteristics", style1)
        col = 0
        for char in hchars:
            value = char[0]
            typep = char[1]
            if value !='pid' and value !='hhid':
                stringvar = 'varchar'
                boolvar = 'enum'
                intvar = 'bigint'
                doublevar ='double'
                if typep.startswith(tuple(stringvar)):
                    vartype ='String'
                elif typep.startswith(tuple(boolvar)):
                    vartype ='Yes/No'
                elif typep.startswith(tuple(intvar)):
                    vartype ='Integer'
                elif typep.startswith(tuple(doublevar)):
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
        
        sheet2.write(headerrow, 0, "Livestock", style1)
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

        folder = "inputs/"
        filename = folder + "dataEntrySheet-ProjectID-" + str(self.pid) + ".xls"
        book.save(filename)
        completionmessage = '''Template Saved As open-ihm/''' + str(filename) +'''\n\nClick OK to open the spreadsheet. This may take a few seconds. '''
        QtGui.QMessageBox.information(None, 'Data Entry Template', completionmessage)
 
        #
        os.system(os.path.curdir + "\\inputs\\dataEntrySheet-ProjectID-" + str(self.pid) + ".xls")
        
        
