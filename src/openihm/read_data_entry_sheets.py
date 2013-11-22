#-------------------------------------------------------------------	
#	Filename: read_data_entry_sheets.py
#-------------------------------------------------------------------

from xlrd import open_workbook
from data.database import Database

class ReadDataEntrySheets:
    
    def __init__(self,projectid):
        self.database = Database()
        self.pid = projectid

    def readdata(self):
        book = open_workbook('dataEntrySheet-ProjectID-5.xls')
        print book.nsheets
        projectsheet = book.sheet_by_index(0)
        projectid = projectsheet.name
        for sheet_index in range(2,book.nsheets):
            householdsheet = book.sheet_by_index(sheet_index)
            houseid = householdsheet.name

            #traverse sheet looking for section markers e.g crops
            for row_index in range(householdsheet.nrows):
                value = householdsheet.cell(row_index,0).value
                if value == 'HouseholdMembers':
                    self.readBasicMemberDetails(householdsheet,row_index)
                elif value == 'PersonalCharacteristics':
                    pass
                elif value == 'HouseholdCharacteristics':
                    pass
                elif value == 'Assets':
                    pass
                elif value == 'Crops':
                    pass
                elif value == 'Livestock':
                    pass
                elif value == 'WildFoods':
                    pass
                elif value == 'Employment':
                    pass
                elif value == 'SocialTransfer':
                    pass
                elif value == 'TransferFromOrganisations':
                    pass
                elif value == 'Expenditure':
                    pass

        def readBasicMemberDetails(self,householdsheet,row_index):
            #print book.nsheets
            start_row_index = row_index + 1
            empty_cell_count = 0
            hhid = householdsheet.name
            print hhid
            database = Database()
            database.open()

            for current_row_index in range(start_row_index, householdsheet.nrows):
                values = []
                for col_index in range(0,4):
                    cellvalue = householdsheet.cell(current_row_index,col_index).value
                    print cellvalue
                    if cellvalue == '':
                        empty_cell_count = empty_cell_count + 1
                        cellvalue = None
                    if col_index > 0 and valueisdigit()== False:
                        cellvalue = None
                    if col_index == 3 and (cellvalue == 1 or cellvalue =='yes'):
                        cellvalue = 'Yes'
                    else:
                         cellvalue = 'No'
                                           
                    values.append(cellvalue)

                if empty_cell_count == 4 or value == 'PersonalCharacteristics':   #check if entire row is empty
                    break
                else:
                    
                    sex = values[0]
                    age = values[1]
                    yearofbirth = values[2]
                    hhead = values[3]
                    personid = str(sex)+str(age)

                query ='''REPLACE INTO householdmembers (personid,hhid,headofhousehold,yearofbirth,sex,pid)
                            VALUES ('%s',%s,'%s',%s,'%s','%s',%s)''' % (personid,hhid,hhead,yearofbirth,self.pid)
                                           
                print query
                database.execUpdateQuery(query)

                empty_cell_count = 0
                
            database.close()
                        
            
