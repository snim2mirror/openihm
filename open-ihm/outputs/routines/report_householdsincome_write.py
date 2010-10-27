#-------------------------------------------------------------------	
#	Filename: report_householdsincome_write.py
#-------------------------------------------------------------------

from xlwt import Workbook, easyxf
import os

class HouseholdsIncomeWrite:
    #def __init__(self):
        #self.database = Database()

    def writeSpreadsheetReport(self,reporttable,reporttype):
        
        book = Workbook(encoding="utf-8") 
        sheet1 = book.add_sheet("Households By Income Source")
        style1 = easyxf('font: name Arial;''font: bold True;')


        #Wrire Table Title
        print reporttype
        reptitle = "%s" % reporttype
        sheet1.write(0, 0, reptitle, style1) 
        sheet1.col(0).width = 1500
        #write Headers
        i = 1
        row = reporttable[0]
        keylist = row.keys()
        keylist.sort()
        for key in keylist:
            if key =='hhid':
                sheet1.write(2, 0, key, style1)
                #sheet1.col(0).width = 1500
            else:
                sheet1.write(2, i, key,style1)
                sheet1.col(i).width = 4000
                i = i + 1

        #write Data 
        myrow = 3
        mycol = 1
        for row in reporttable:
            for key in keylist:
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
        
        dirpath = os.path.join("outputs", "spreadsheets")
        book.save("openihm_spreadsheet1.xls")
 
