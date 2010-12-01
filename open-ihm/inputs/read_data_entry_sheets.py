#-------------------------------------------------------------------	
#	Filename: read_data_entry_sheets.py
#-------------------------------------------------------------------

from xlrd import open_workbook,cellname,xldate_as_tuple
from datetime import date
from data.database import Database
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ReadDataEntrySheets:
    
    def __init__(self,projectid):
        self.database = Database()
        self.pid = projectid

    def readdata(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home')
        book = open_workbook(filename)
        projectsheet = book.sheet_by_index(0)
        self.readProjectHouseholdsData(book)
        
        projectid = projectsheet.name
        for sheet_index in range(2,book.nsheets):
            householdsheet = book.sheet_by_index(sheet_index)
            houseid = householdsheet.name
            
            #traverse sheet looking for section markers e.g crops
            for row_index in range(householdsheet.nrows):
                cellvalue = householdsheet.cell(row_index,0).value
                print cellvalue
                if cellvalue == 'HouseholdMembers':
                    self.readBasicMemberDetails(householdsheet,row_index)
                elif cellvalue == 'PersonalCharacteristics':
                    pass
                elif cellvalue == 'HouseholdCharacteristics':
                    pass
                elif cellvalue == 'Assets':
                    self.readAssetData(householdsheet,row_index)
                elif cellvalue == 'Expenditure':
                    self.readExpenditureData(householdsheet,row_index)
                elif cellvalue == 'Crops':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'Livestock':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'WildFoods':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'Employment':
                    self.readEmploymentData(householdsheet,row_index)
                elif cellvalue == 'SocialTransfer':
                    pass
                elif cellvalue == 'TransferFromOrganisations':
                    pass
                         

    def readProjectHouseholdsData(self,book):
        sheet1 = book.sheet_by_index(0)

        # Start Block of code for importing a project's households
        database = Database()
        database.open()

        for row in range(2,sheet1.nrows):
            values = []
            for col in range(sheet1.ncols):
                skiprow =False
                cellvalue = sheet1.cell(row,col).value
                cell = sheet1.cell(row,col)
                if cellvalue =='' or (col ==3 and cell.ctype!=3):
                    skiprow =True
                    break
                
                else:
                    if cell.ctype == 3: #date
                        date_value = xldate_as_tuple(cell.value,book.datemode)
                        cellvalue = date(*date_value[:3])
                    else:
                        cellvalue = cell.value

                values.append(cellvalue)

            if skiprow ==True:
                continue
            else:
                hhid = values[0]
                hholdname = values[1]
                datevisited = values[2]
                pid= sheet1.name

                query ='''REPLACE INTO households (hhid,householdname,dateofcollection,pid) VALUES (%s,'%s','%s',%s)''' % (hhid,hholdname,datevisited,pid)
                database.execUpdateQuery(query)

        database.close()


    def readBasicMemberDetails(self,householdsheet,row_index):
        
        #print book.nsheets
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,4):
                exitmain = False
                skiprow =False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if cellvalue == 'PersonalCharacteristics':
                    exitmain = True
                    break

                if (col_index == 0 or colindex ==1) and cellvalue=='':
                    skiprow =True
                    break
                
                try:
                    cellvalue = int(cellvalue)
                    digitvalue = True
                except ValueError:
                    digitvalue = False

                if cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue = 'NULL'
                if (col_index ==1 or col_index ==2) and digitvalue == False:
                    cellvalue = 0
                if col_index == 3 and (cellvalue == 1 or cellvalue.lower() =='yes' or cellvalue.lower() =='y'):
                    cellvalue = 'Yes'
                elif col_index == 3 and (cellvalue != 1 or cellvalue.lower() !='yes' or cellvalue.lower() !='y'):
                    cellvalue = 'No'

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if empty_cell_count == 4 or skiprow == True:   #check if entire row is empty
                    continue
                else:
                    
                    sex = str(values[0])
                    age = values[1]
                    yearofbirth = values[2]
                    hhead = values[3]
                    if sex.lower() == 'male' or sex.lower() == 'm':
                        personid = 'm' + str(age)
                    elif sex.lower() == 'female' or sex.lower() == 'f':
                        personid = 'f' + str(age)

                    query ='''REPLACE INTO householdmembers (personid,hhid,headofhousehold,yearofbirth,sex,pid)
                            VALUES ('%s',%s,'%s',%s,'%s',%s)''' % (personid,hhid,hhead,yearofbirth,sex,self.pid)
                                           
                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readAssetData(self,householdsheet,row_index):
        
        #print book.nsheets
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,5):
                digitvalue = True
                skiprow = False
                exitmain = False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if cellvalue == 'Expenditure':
                    exitmain = True
                    break
                if col_index == 0 and cellvalue=='':
                    skiprow =True
                    break
                    
                if cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue = 'NULL'
                if (col_index ==3 or col_index ==4):
                    
                    try:
                        cellvalue = float(cellvalue)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if empty_cell_count >= 5 or skiprow == True:   #check if entire row is empty
                    continue
                else:
                    
                    category = values[0]
                    assettype = values[1]
                    unit = values[2]
                    unitcost = values[3]
                    units = values[4]

                    query ='''REPLACE INTO assets (hhid,assetcategory,assettype,unitofmeasure,unitcost,totalunits,pid)
                            VALUES ('%s','%s','%s','%s',%s,%s,%s)''' % (hhid,category,assettype,unit,unitcost,units,self.pid)
                 
                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readExpenditureData(self,householdsheet,row_index):
        
        #print book.nsheets
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,5):
                exitmain = False
                digitvalue = True
                skiprow = False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if cellvalue == 'Crops':
                    exitmain = True
                    break
                if  col_index == 0 and cellvalue=='':
                    skiprow = True
                    break
                if col_index!=0 and cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue = 'NULL'
                if (col_index >=2 and col_index <=4):
                    
                    try:
                        cellvalue = float(cellvalue)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if empty_cell_count >= 3 or skiprow == True:   #check if at least three cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    expendituretype = values[0]
                    unit = values[1]
                    kcalperunit = values[2]
                    unitcost = values[3]
                    units = values[4]

                    query ='''REPLACE INTO expenditure (hhid,exptype,unitofmeasure,priceperunit,kcalperunit,totalunits,pid)
                            VALUES (%s,'%s','%s',%s,%s,%s,%s)''' % (hhid,expendituretype,unit,unitcost,kcalperunit,units,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readCropAndFoodsIncomeData(self,householdsheet,row_index,incometype):
        
        #print book.nsheets
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,7):
                exitmain = False
                digitvalue = True
                skiprow = False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if incometype== 'Crops':
                    if cellvalue == 'Livestock':
                        exitmain = True
                        break
                elif incometype== 'Livestock':
                    if cellvalue == 'WildFoods':
                        exitmain = True
                        break
                elif incometype== 'WildFoods':
                    if cellvalue == 'Employment':
                        exitmain = True
                        break
                
                if col_index == 0 and cellvalue=='':
                    skiprow = True
                    break
                if col_index!=0 and cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue='NULL'

                if (col_index >=2 and col_index <=6):
                    
                    try:
                        cellvalue = float(cellvalue)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if empty_cell_count >= 5 or skiprow==True:   #check if four cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    name = values[0]
                    unit = values[1]
                    unitsproduced = values[2]
                    unitssold = values[3]
                    unitprice = values[4]
                    otheruses = values[5]
                    unitsconsumed = values[6]
                    if incometype=='Crops':
                        tablename='cropincome'
                    elif incometype=='Livestock':
                        tablename='livestockincome'
                    elif incometype=='WildFoods':
                        tablename='wildfoods'

                    query ='''REPLACE INTO %s (hhid,incomesource,unitofmeasure,unitsproduced,unitssold,unitprice,otheruses,unitsconsumed,pid) 
                            VALUES (%s,'%s','%s',%s,%s,%s,%s,%s,%s)''' % (tablename,hhid,name,unit,unitsproduced,unitssold,unitprice,otheruses,unitsconsumed,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readEmploymentData(self,householdsheet,row_index):
        
        #print book.nsheets
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,6):
                exitmain = False
                digitvalue = True
                skiprow = False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                print cellvalue

                if cellvalue == 'SocialTransfer':
                    exitmain = True
                    break
                if  col_index == 0 and cellvalue=='':
                    skiprow = True
                    break
                if col_index!=0 and cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue = 'NULL'
                if (col_index >=3 and col_index <=5):
                    
                    try:
                        cellvalue = float(cellvalue)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)
            print exitmain
            print skiprow

            if exitmain == True:
                break
            else:
                if empty_cell_count > 4 or skiprow == True:   #check if at least three cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    employmenttype = values[0]
                    foodpaid = values[1]
                    unit = values[2]
                    unitspaid = values[3]
                    kcals = values[4]
                    cashincome = values[5]

                    query ='''REPLACE INTO employmentincome (hhid,incomesource,foodtypepaid,unitofmeasure,unitspaid,incomekcal,cashincome,pid)
                            VALUES (%s,'%s','%s','%s',%s,%s,%s,%s)''' % (hhid,employmenttype,foodpaid,unit,unitspaid,kcals,cashincome,self.pid)

                    print query
                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()

    def readTransferData(self,householdsheet,row_index,incometype):
        
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,7):
                exitmain = False
                digitvalue = True
                skiprow = False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if incometype== 'SocialTransfer':
                    if cellvalue == 'TransferFromOrganisations':
                        exitmain = True
                        break

                if col_index == 0 and cellvalue=='':
                    skiprow = True
                    break
                if col_index!=0 and cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue='NULL'

                if col_index ==2 or(col_index >=4 and col_index <=7):
                    
                    try:
                        cellvalue = float(cellvalue)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if empty_cell_count > 5 or skiprow==True:   #check if four cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    transfersource = values[0]
                    cash = values[1]
                    foodtype = values[2]
                    unit = values[3]
                    unitsreceived = values[4]
                    unitsconsumed = values[5]
                    unitssold= values[6]
                    unitprice= values[7]
                    
                    if incometype=='SocialTransfer':
                        sourcetype='Internal'
                    elif incometype=='TransferFromOrganisations':
                        sourcetype='External'

                    query ='''REPLACE INTO tansfers (hhid,sourcetype,sourceoftransfer,cashperyear,foodtype,unitofmeasure,unitsgiven,unitsconsumed,unitssold,priceperunit,pid) 
                            VALUES (%s,'%s','%s',%s,'%s','%s',%s,%s,%s,%s,%s)''' % (hhid,sourcetype,transfersource,cash,foodtype,unit,unitsreceived,unitsconsumed,unitssold,unitprice,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
    
 
