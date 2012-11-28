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


from includes.xlrd import open_workbook,cellname,xldate_as_tuple
from datetime import date,datetime
from data.database import Database
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ReadDataEntrySheets:
    
    def __init__(self,projectid):
        self.database = Database()
        self.pid = projectid
        self.pcharstable = 'personalcharacteristics'
        self.hcharstable = 'householdcharacteristics'

    def readdata(self):
        '''Base method for data importation'''
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home')
        book = open_workbook(filename)
        projectsheet = book.sheet_by_index(0)
        self.readProjectHouseholdsData(book)
        
        projectid = projectsheet.name
            
        for sheet_index in range(3,book.nsheets):
            householdsheet = book.sheet_by_index(sheet_index)
            houseid = householdsheet.name
            
            #traverse sheet looking for section markers e.g crops
            
            for row_index in range(householdsheet.nrows):
                cellvalue = householdsheet.cell(row_index,0).value
                if cellvalue == 'HouseholdMembers':
                    self.readBasicMemberDetails(householdsheet,row_index)
                elif cellvalue == 'PersonalCharacteristics':
                    self.readPCharacteristicsData(householdsheet,row_index)
                elif cellvalue == 'HouseholdCharacteristics':
                    self.readHCharacteristicsData(householdsheet,row_index)
                elif cellvalue == 'Assets':
                    self.readAssetData(householdsheet,row_index)
                elif cellvalue == 'Expenditure':
                    self.readExpenditureData(householdsheet,row_index)
                elif cellvalue == 'Crops-C':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'Livestock-C':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'Wildfoods-C':
                    self.readCropAndFoodsIncomeData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'Employment':
                    self.readEmploymentData(householdsheet,row_index)
                elif cellvalue == 'SocialTransfer':
                    self.readTransferData(householdsheet,row_index,cellvalue)
                elif cellvalue == 'TransferFromOrganisations':
                    self.readTransferData(householdsheet,row_index,cellvalue)
        QtGui.QMessageBox.information(None, 'Importing Data', "Data Importation Completed")
        #QtGui.QMessageBox.information(None, 'Importing Data Error', "Data Importation Failed")

    def readProjectHouseholdsData(self,book):
        '''Import Project Households'''
        sheet1 = book.sheet_by_index(0)

        # Start Block of code for importing a project's households
        database = Database()
        database.open()

        for row in range(2,sheet1.nrows):
            values = []
            for col in range(sheet1.ncols):
                skiprow =False
                cell = sheet1.cell(row,col)
                cellvalue = cell.value
                #cellvalue = sheet1.cell(row,col).value
                
                if cellvalue =='':
                    #if cellvalue =='' or (col ==3 and cell.ctype!=3):
                    skiprow =True
                    break

                else:
                    if col == 2:
                        if cell.ctype == 3: #date
                            date_value = xldate_as_tuple(cell.value,book.datemode)
                            cellvalue = date(*date_value[:3])
                        else:
                            cellvalue = datetime.strptime(cellvalue, "%d-%m-%Y").strftime('%Y-%m-%d')

                values.append(cellvalue)

            if skiprow ==True:
                continue
            else:
                hhid = values[0]
                hholdname = values[1]
                datevisited = values[2]
                pid= sheet1.name

                testquery ='''SELECT hhid,pid FROM households WHERE hhid='%s' AND pid =%s ''' % (hhid,self.pid)
                numrows =self.checkRecordExistence(testquery)
		if numrows ==0:
                    query ='''INSERT INTO households (hhid,householdname,dateofcollection,pid) VALUES ('%s','%s','%s',%s)''' % (hhid,hholdname,datevisited,pid)
                        
                else:
                    query ='''UPDATE households SET hhid='%s',householdname='%s',dateofcollection='%s',pid=%s
                                WHERE hhid='%s' AND pid =%s ''' % (hhid,hholdname,datevisited,pid,hhid,pid)
                database.execUpdateQuery(query)
                

        database.close()


    def readBasicMemberDetails(self,householdsheet,row_index):
        '''Import Data on Basic Personal Characteristics: - Sex,Age,year Of Birth, and household headship status'''
        
        start_row_index = row_index + 2
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,5):
                exitmain = False
                skiprow =False
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                if cellvalue == 'PersonalCharacteristics':
                    exitmain = True
                    break

                if (col_index == 0 or col_index ==1) and cellvalue=='':
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
                if (col_index ==1 or col_index ==2 or col_index ==4) and digitvalue == False:
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
                    
                    if values[2] ==0 and age !=0:
                        yearofbirth = date.today().year - values[1]
                        
                    elif values[2] ==0 and age ==0:
                        
                        yearofbirth = date.today().year
                    else:
                        yearofbirth = values[2]
                        
                    hhead = values[3]
                    if sex.lower() == 'male' or sex.lower() == 'm':
                        personid = 'm' + str(age)
                        sex = 'Male'
                    elif sex.lower() == 'female' or sex.lower() == 'f':
                        personid = 'f' + str(age)
                        sex='Female'
                    pidvalue = personid 

                    periodaway = values[4]

                    testquery ='''SELECT * FROM householdmembers WHERE hhid='%s' AND personid ='%s' AND pid =%s ''' % (hhid,pidvalue,self.pid)
                    numrows =self.checkRecordExistence(testquery)
		    if numrows ==0:
                        query ='''INSERT INTO householdmembers (personid,hhid,headofhousehold,yearofbirth,sex,periodaway,pid)
                            VALUES ('%s','%s','%s',%s,'%s',%s,%s)''' % (personid,hhid,hhead,yearofbirth,sex,periodaway,self.pid)
                        
                    else:
                        #personid = personid + '_' + str(numrows+1)
                        query = ''' UPDATE householdmembers SET headofhousehold='%s',yearofbirth=%s,sex='%s',periodaway=%s
                                    WHERE personid='%s' AND hhid='%s' AND pid=%s''' % (hhead,yearofbirth,sex,periodaway,personid,hhid,self.pid)

            empty_cell_count = 0
                
        database.close()
            
    def readAssetData(self,householdsheet,row_index):
        '''Import Asset Data'''
        
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
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)
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

                    testquery ='''SELECT * FROM assets WHERE hhid='%s' AND assetcategory='%s' AND assettype='%s' AND pid =%s ''' % (hhid,category,assettype,self.pid)
                    numrows =self.checkRecordExistence(testquery)
		    if numrows ==0:

                        query ='''INSERT INTO assets (hhid,assetcategory,assettype,unitofmeasure,unitcost,totalunits,pid)
                                    VALUES ('%s','%s','%s','%s',%s,%s,%s)''' % (hhid,category,assettype,unit,unitcost,units,self.pid)
                    else:
                        query ='''UPDATE assets SET hhid='%s',assetcategory='%s',assettype='%s',unitofmeasure='%s',unitcost=%s,totalunits=%s,pid=%s
                                WHERE hhid='%s' AND assetcategory='%s' AND assettype='%s' AND pid =%s ''' % (hhid,category,assettype,unit,unitcost,units,self.pid,hhid,category,assettype,self.pid)
                 
                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readExpenditureData(self,householdsheet,row_index):
        '''Import Expenditure Data'''
        
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
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)
                if cellvalue == 'Crops-C':
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
                if skiprow == True:   #check if at least three cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    expendituretype = values[0]
                    unit = values[1]
                    kcalperunit = values[2]
                    unitcost = values[3]
                    units = values[4]

                    testquery ='''SELECT * FROM expenditure WHERE hhid='%s' AND exptype='%s' AND pid =%s''' % (hhid,expendituretype,self.pid)
                    numrows = self.checkRecordExistence(testquery)

		    if numrows ==0:
                        query ='''INSERT INTO expenditure (hhid,exptype,unitofmeasure,priceperunit,kcalperunit,totalunits,pid)
                            VALUES ('%s','%s','%s',%s,%s,%s,%s)''' % (hhid,expendituretype,unit,unitcost,kcalperunit,units,self.pid)
                    else:
                        query='''UPDATE expenditure SET hhid='%s',exptype='%s',unitofmeasure='%s',priceperunit=%s,kcalperunit=%s,totalunits=%s,pid=%s
                                WHERE hhid='%s' AND exptype='%s' AND pid =%s ''' % (hhid,expendituretype,unit,unitcost,kcalperunit,units,self.pid,hhid,expendituretype,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readCropAndFoodsIncomeData(self,householdsheet,row_index,incometype):
        '''Import Data for Crop, Livestock, and Wildfood Income'''
        
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
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)
                if incometype== 'Crops-C':
                    if cellvalue == 'Livestock-C':
                        exitmain = True
                        break
                elif incometype== 'Livestock-C':
                    if cellvalue == 'Wildfoods-C':
                        exitmain = True
                        break
                elif incometype== 'Wildfoods-C':
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
                if skiprow==True:   #check if four cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    name = values[0]
                    unit = values[1]
                    unitsproduced = values[2]
                    unitssold = values[3]
                    unitprice = values[4]
                    otheruses = values[5]
                    unitsconsumed = values[6]
                    if incometype=='Crops-C':
                        tablename='cropincome'
                    elif incometype=='Livestock-C':
                        tablename='livestockincome'
                    elif incometype=='Wildfoods-C':
                        tablename='wildfoods'

                    testquery =''' SELECT * FROM %s WHERE hhid='%s' AND incomesource='%s' AND pid=%s ''' % (tablename,hhid,name,self.pid)
                    numrows = self.checkRecordExistence(testquery)

                    if numrows ==0:

                        query ='''INSERT INTO %s (hhid,incomesource,unitofmeasure,unitsproduced,unitssold,unitprice,otheruses,unitsconsumed,pid) 
                            VALUES (%s,'%s','%s',%s,%s,%s,%s,%s,%s)''' % (tablename,hhid,name,unit,unitsproduced,unitssold,unitprice,otheruses,unitsconsumed,self.pid)
                    else:
                        query ='''UPDATE %s  SET hhid='%s',incomesource='%s',unitofmeasure='%s',unitsproduced=%s,unitssold=%s,unitprice=%s,otheruses=%s,unitsconsumed=%s,pid=%s 
                            WHERE hhid='%s' AND incomesource='%s' AND pid=%s  ''' % (tablename,hhid,name,unit,unitsproduced,unitssold,unitprice,otheruses,unitsconsumed,self.pid,hhid,name,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
            
    def readEmploymentData(self,householdsheet,row_index):
        '''Import Employment Data'''
        
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
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)

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
                        cellvalue = round(float(cellvalue),2)
                        digitvalue = True
                    except ValueError:
                        digitvalue = False
                    if digitvalue == False:
                        cellvalue = 0

                values.append(cellvalue)

            if exitmain == True:
                break
            else:
                if skiprow == True:   #check if at least three cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    employmenttype = values[0]
                    foodpaid = values[1]
                    unit = values[2]
                    unitspaid = values[3]
                    kcals = values[4]
                    cashincome = values[5]

                    testquery = '''SELECT * FROM employmentincome WHERE hhid='%s' AND incomesource='%s' AND pid =%s''' %(hhid,employmenttype,self.pid)
                    numrows = self.checkRecordExistence(testquery)

		    if numrows ==0:
                        query ='''INSERT INTO employmentincome (hhid,incomesource,foodtypepaid,unitofmeasure,unitspaid,incomekcal,cashincome,pid)
                            VALUES ('%s','%s','%s','%s',%s,%s,%s,%s)''' % (hhid,employmenttype,foodpaid,unit,unitspaid,kcals,cashincome,self.pid)
                        
                    else:
                        query = '''UPDATE employmentincome SET hhid='%s',incomesource='%s',foodtypepaid='%s',unitofmeasure='%s',unitspaid=%s,incomekcal=%s,cashincome=%s,pid=%s
                                    WHERE hhid='%s' AND incomesource='%s' AND pid =%s''' % (hhid,employmenttype,foodpaid,unit,unitspaid,kcals,cashincome,self.pid,hhid,employmenttype,self.pid)

                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()

    def readTransferData(self,householdsheet,row_index,incometype):
        '''Import data on social and Organisational Transfers'''
        
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
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)
                if incometype== 'SocialTransfer' and cellvalue == 'TransferFromOrganisations':
                    #if cellvalue == 'TransferFromOrganisations':
                    exitmain = True
                    break

                if col_index == 0 and cellvalue=='':
                    skiprow = True
                    break
                if col_index!=0 and cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue='NotSet'

                if col_index ==1 or(col_index >=4 and col_index <=7):
                    
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
                if skiprow==True:   #check if four cell in row or cell for expenditurety are empty
                    continue
                else:
                    
                    transfersource = values[0]
                    cash = values[1]
                    foodtype = values[2]
                    unit = values[3]
                    unitsconsumed = values[4]
                    unitssold= values[5]
                    unitprice= values[6]
                    
                    if incometype=='SocialTransfer':
                        sourcetype='Internal'
                    elif incometype=='TransferFromOrganisations':
                        sourcetype='External'

                    testquery = '''SELECT * from transfers WHERE hhid='%s' AND pid=%s AND sourcetype='%s' AND sourceoftransfer='%s' ''' %(hhid,self.pid,sourcetype,transfersource)
                    numrows = self.checkRecordExistence(testquery)
		    if numrows ==0:
                        
                        query ='''INSERT INTO transfers (hhid,sourcetype,sourceoftransfer,cashperyear,foodtype,unitofmeasure,unitsconsumed,unitssold,priceperunit,pid) 
                            VALUES ('%s','%s','%s',%s,'%s','%s',%s,%s,%s,%s)''' % (hhid,sourcetype,transfersource,cash,foodtype,unit,unitsconsumed,unitssold,unitprice,self.pid)
                    else:
                        query ='''UPDATE transfers SET hhid='%s',sourcetype='%s',sourceoftransfer='%s',cashperyear=%s,foodtype='%s',unitofmeasure='%s',unitsconsumed=%s,unitssold=%s,priceperunit=%s,pid=%s
                                WHERE hhid='%s' AND pid=%s AND sourcetype='%s' AND sourceoftransfer='%s' ''' % (hhid,sourcetype,transfersource,cash,foodtype,unit,unitsconsumed,unitssold,unitprice,self.pid,hhid,self.pid,sourcetype,transfersource)
                    database.execUpdateQuery(query)

            empty_cell_count = 0
                
        database.close()
    
    def readPCharacteristicsData(self,householdsheet,row_index):
        '''Import Data on Extended Personal Characteristics'''
        
        field_row_index = row_index + 1
        datatype_row_index = row_index + 2
        start_row_index = row_index + 3
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        #determine number of columns for pcharacteristics
        columns = 0
        datafields=[]
        fielddatatypes=[]
        for col_index in range (0,householdsheet.ncols):
            
            datafieldvalue = str(householdsheet.cell(field_row_index,col_index).value) 
            fieldtype = str(householdsheet.cell(datatype_row_index,col_index).value)
            
            if datafieldvalue!='':
                datafields.append(datafieldvalue)
                fielddatatypes.append(fieldtype)
                columns = columns + 1
            else:
                break

        empty_cell_count =0

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,columns):
                exitmain = False
                personid =''
                cellvalue = householdsheet.cell(current_row_index,col_index).value
                datatype = str(householdsheet.cell(datatype_row_index,col_index).value)
                if cellvalue == 'HouseholdCharacteristics':
                    exitmain = True
                    break
                if cellvalue == '':
                    empty_cell_count = empty_cell_count + 1
                    cellvalue = 'NULL'

                if datatype=='Double':
                    try:
                        cellvalue = float(cellvalue)
                        
                    except ValueError:
                        cellvalue = 0
                        
                elif datatype=='Integer':
                    try:
                        cellvalue = int(cellvalue)
                    except ValueError:
                        cellvalue = 0
                        
                elif datatype=='Yes/No':
                    try:
                        cellvalue = int(cellvalue)
                    except:
                        pass
                    tempvalue = str(cellvalue)
                    tempvalue = tempvalue.strip()
                    
                    if (tempvalue == '1' or tempvalue.lower() =='yes' or tempvalue.lower() =='y'):
                        cellvalue = 'Yes'
                    else:
                        cellvalue = 'No'

                values.append(cellvalue)

            if exitmain == True or empty_cell_count==columns:
                break
            else:
                if values[0]=='NULL': #skip row if personid was not entered in sheet
                    continue
                else:
                    for dataindex in range (1,len(datafields)):
                        paramlist=[]
                        characteristic = datafields[dataindex]
                        charvalue= values[dataindex]
                        testquery='''SELECT * from personalcharacteristics WHERE personid='%s' AND hhid='%s' AND pid=%s AND characteristic='%s' ''' %(values[0],hhid,self.pid,characteristic)
                        numrows = self.checkRecordExistence(testquery)
                        paramlist = (hhid,values[0],datafields[dataindex],values[dataindex])
                        if numrows == 0:
                            
                            query = self.buildPCharInsertQuery(paramlist)
                        else:
                            query= '''DELETE FROM personalcharacteristics WHERE personid='%s' AND hhid='%s' AND pid=%s AND characteristic='%s' ''' %(values[0],hhid,self.pid,characteristic)
                            database.execUpdateQuery(query)
                            query = self.buildPCharInsertQuery(paramlist)
                        database.execUpdateQuery(query)
                
            empty_cell_count = 0
                
        database.close()


    def readHCharacteristicsData(self,householdsheet,row_index):
        '''Import Data on Household Characteristics'''
        
        field_row_index = row_index + 1
        datatype_row_index = row_index + 2
        start_row_index = row_index + 3
        empty_cell_count = 0
        hhid = householdsheet.name
        database = Database()
        database.open()

        #determine number of columns for pcharacteristics
        columns = 0
        datafields=[]
        fielddatatypes=[]
        for col_index in range (0,householdsheet.ncols):
            
            datafieldvalue = householdsheet.cell(field_row_index,col_index).value 
            fieldtype = str(householdsheet.cell(datatype_row_index,col_index).value)
            
            if datafieldvalue!='':
                datafields.append(datafieldvalue)
                fielddatatypes.append(fieldtype)
                columns = columns + 1
            else:
                break

        empty_cell_count =0

        for current_row_index in range(start_row_index, householdsheet.nrows):
            values = []
            for col_index in range(0,columns):
                exitmain = False
                personid =''
                cellvalue = str(householdsheet.cell(current_row_index,col_index).value)
                datatype = str(householdsheet.cell(datatype_row_index,col_index).value)
                if cellvalue == 'Assets':
                    exitmain = True
                    break
                if cellvalue == '':
                    cellvalue ='NULL'
                    empty_cell_count = empty_cell_count + 1

                if datatype=='Double':
                    try:
                        cellvalue = float(cellvalue)
                        
                    except ValueError:
                        cellvalue = 0
                        
                elif datatype=='Integer':
                    try:
                        cellvalue = int(cellvalue)
                    except ValueError:
                        cellvalue = 0
                        
                elif datatype=='Yes/No':
                    try:
                        cellvalue = int(cellvalue)
                    except:
                        pass
                    tempvalue = str(cellvalue)
                    tempvalue = tempvalue.strip()
                    
                    if tempvalue == '1' or tempvalue.lower() =='yes' or tempvalue.lower() =='y':
                        cellvalue = 'Yes'
                    else:
                        cellvalue = 'No'

                values.append(cellvalue)
                
            if exitmain == True or empty_cell_count==columns:
                break
            else:
                for dataindex in range (0,len(datafields)):
                        paramlist=[]
                        characteristic = datafields[dataindex]
                        charvalue= values[dataindex]
                        testquery='''SELECT * from householdcharacteristics WHERE hhid='%s' AND pid=%s AND characteristic='%s' ''' %(hhid,self.pid,characteristic)
                        numrows = self.checkRecordExistence(testquery)
                        paramlist = (hhid,datafields[dataindex],values[dataindex])
                        if numrows == 0:
                            query = self.buildHCharInsertQuery(paramlist)
                        else:
                            query= '''DELETE FROM householdcharacteristics WHERE hhid='%s' AND pid=%s AND characteristic='%s' ''' %(hhid,self.pid,characteristic)
                            database.execUpdateQuery(query)
                            query = self.buildHCharInsertQuery(paramlist)
                        database.execUpdateQuery(query)
                
        database.close()
        
    def buildPCharInsertQuery(self,paramlist):
        ''' query generation for inserting personal characteristics'''
	### FIXME TODO: Check that hhid is escaped with quotes here.
        query = "INSERT INTO personalcharacteristics (pid, hhid, personid,characteristic,charvalue) VALUES " 
        parameterlist = '(' + str(self.pid) +',' + str(paramlist[0]) +', ' + "'" + str(paramlist[1]) + "'"+ ', ' +"'" + str(paramlist[2]) +"'"+ ', '
        if (type(paramlist[3]) is str) or (type(paramlist[3]) is unicode):
            parameterlist = parameterlist + "'" + paramlist[3] + "'"
        else:
            parameterlist = parameterlist + str(paramlist[3])
            
        parameterlist = parameterlist + ')'
        query = query + parameterlist
        return query

    def buildHCharInsertQuery(self,paramlist):
        ''' query generation for inserting household characteristics'''
	### FIXME TODO: Check that hhid is escaped with quotes here.        
        query = "INSERT INTO householdcharacteristics (pid, hhid,characteristic,charvalue) VALUES " 
        parameterlist = '(' + str(self.pid) +',' + str(paramlist[0]) +', ' +"'"+ str(paramlist[1]) +"'"+ ', '
        if (type(paramlist[2]) is str) or (type(paramlist[2]) is unicode):
            parameterlist = parameterlist + "'" + paramlist[2] + "'"
        else:
            parameterlist = parameterlist + str(paramlist[2])
            
        parameterlist = parameterlist + ')'
        query = query + parameterlist
        return query

    def checkRecordExistence(self,testquery):
        '''Test if a record with some given primary key already exists'''
        database = Database()
        database.open()
        testrecset = database.execSelectQuery(testquery)
        numrows =0
        for row in testrecset:
	    numrows = numrows + 1
        database.open()
	return numrows
