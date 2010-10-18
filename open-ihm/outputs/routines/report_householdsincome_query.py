#-------------------------------------------------------------------	
#	Filename: report_householdsincome_query.py
#-------------------------------------------------------------------

from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager

class HouseholdIncomeQuery:
    def __init__(self):
        self.database = Database()

    def buildFinalReportQuery (self,householdIDs,cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery):
        householdids = tuple(householdIDs)
        query =''
        if len(householdIDs)!=0:
            
            if cropsQuery !='' and employmentQuery!='' and livestockQuery !='' and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = '''SELECT * FROM (%s UNION ALL %s UNION ALL %s UNION ALL %s UNION ALL %s UNION ALL %s UNION ALL %s) AS householdincome''' % (basequery, cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)


            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and loansQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and livestockQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass
            elif employmentQuery !='' and livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif employmentQuery!=0 and livestockQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass
            elif employmentQuery!=0 and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass
 
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and employmentQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and livestockQuery !='' and loansQuery !='':
                pass
            elif cropsQuery !='' and livestockQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                pass
            elif cropsQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif employmentQuery !='' and livestockQuery !='' and loansQuery !='':
                pass
            elif employmentQuery !='' and livestockQuery !='' and transfersQuery !='':
                pass
            elif employmentQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                pass
            elif employmentQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif employmentQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                pass
            elif livestockQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                pass
            elif loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                pass


            elif cropsQuery !='' and employmentQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,employmentQuery)
             elif cropsQuery !='' and livestockQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,livestockQuery)
            elif cropsQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,loansQuery)
            elif cropsQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,transfersQuery)
            elif cropsQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,wildfoodsQuery)
            elif employmentQuery !='' and livestockQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,livestockQuery)
            elif employmentQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,loansQuery)
            elif employmentQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,transfersQuery)
            elif employmentQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,wildfoodsQuery)
            elif livestockQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,loansQuery)
            elif livestockQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,transfersQuery)
            elif livestockQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,wildfoodsQuery)
            elif loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (loansQuery,transfersQuery)
            elif loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (loansQuery,wildfoodsQuery)
            elif transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (transfersQuery,wildfoodsQuery)

            elif cropsQuery !='':
                query = cropsQuery

            elif employmentQuery !='':
                query = employmentQuery

            elif livestockQuery !='':
                query = livestockQuery

            elif loansQuery !='':
                query = loansQuery

            elif transfersQuery !='':
                query = transfersQuery

            elif wildfoodsQuery !='':
                query = wildfoodsQuery

            else:
                #if cropsQuery =='' and employmentQuery =='' and livestockQuery =='' and loansQuery)=='' and transfersQuery =='' and wildfoodsQuery =='':
                QMessageBox.information(self,"Households By Income Source","No Income sources Selected")
                
        print query
        return query

