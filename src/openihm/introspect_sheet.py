from xlrd import open_workbook,cellname,xldate_as_tuple
from datetime import date
from data.database import Database


book = open_workbook('projects.xls')
sheet1 = book.sheet_by_index(0)

# Start Block of code for importing a project's households
database = Database()
database.open()

for row in range(2,sheet1.nrows):
    values = []
    for col in range(sheet1.ncols):
        value = sheet1.cell(row,col).value
        cell = sheet1.cell(row,col)
        if cell.ctype == 3: #date
            date_value = xldate_as_tuple(cell.value,book.datemode)
            value = date(*date_value[:3])
        else:
            value = cell.value

        values.append(value)

    hhid = values[0]
    hholdname = values[1]
    datevisited = values[2]
    pid= sheet1.name

    query ='''REPLACE INTO households (hhid,householdname,dateofcollection,pid) VALUES (%s,'%s','%s',%s)''' % (hhid,hholdname,datevisited,pid)
    database.execUpdateQuery(query)

    #self.insertValuesInDB(hhid,hholdname,datevisited,pid)

database.close()

'''for sheet in range(2,book.sheets):
    huseid = sheet.name
    projectsheet = book.sheet_by_index(0)
    projectid = projectsheet.name'''
    
#def insertValuesInDB(hhid,hholdname,datevisited,pid):
#query ='''REPLACE INTO households (hhid,householdname,dateofcollection,pid) VALUES (%s,'%s',%s,%s)''' % (hhid,hholdname,datevisited,pid)
#database.execUpdateQuery(query)
        
