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
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid
                                LEFT JOIN (%s) table6 ON table5.hhid=table6.hhid )''' % (cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

            # conditions for combinations of 5 income source categories for output
            elif cropsQuery !='' and employmentQuery!='' and livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery)

            elif cropsQuery !='' and employmentQuery!='' and livestockQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (cropsQuery,employmentQuery,livestockQuery,loansQuery,wildfoodsQuery)

            elif cropsQuery !='' and employmentQuery!='' and livestockQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (cropsQuery,employmentQuery,livestockQuery,transfersQuery,wildfoodsQuery)
                
            elif cropsQuery !='' and employmentQuery!='' and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (cropsQuery,employmentQuery,loansQuery,transfersQuery,wildfoodsQuery)
                
            elif cropsQuery !='' and livestockQuery!='' and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (cropsQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

            elif employmentQuery !='' and livestockQuery!='' and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid
                                LEFT JOIN (%s) table5 ON table4.hhid=table5.hhid)''' % (employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

            # conditions for combinations of 4 income source categories for output
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,livestockQuery,loansQuery)
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,livestockQuery,transfersQuery)
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,livestockQuery,wildfoodsQuery)
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,loansQuery,transfersQuery)
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,loansQuery,wildfoodsQuery)
            elif cropsQuery !='' and employmentQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (cropsQuery,employmentQuery,transfersQuery,wildfoodsQuery)

            elif employmentQuery !='' and livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (employmentQuery,livestockQuery,loansQuery,transfersQuery)
            elif employmentQuery !='' and livestockQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (employmentQuery,livestockQuery,loansQuery,wildfoodsQuery)
            elif employmentQuery!=0 and livestockQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (employmentQuery,livestockQuery,transfersQuery,wildfoodsQuery)
            elif employmentQuery!=0 and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (employmentQuery,loansQuery,transfersQuery,wildfoodsQuery)
            elif livestockQuery!=0 and loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid
                                LEFT JOIN (%s) table4 ON table3.hhid=table4.hhid )''' % (livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

            # conditions for combinations of 3 income source categories for output
            elif cropsQuery !='' and employmentQuery !='' and livestockQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,employmentQuery,livestockQuery)
            elif cropsQuery !='' and employmentQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,employmentQuery,loansQuery)
            elif cropsQuery !='' and employmentQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,employmentQuery,transfersQuery)
            elif cropsQuery !='' and employmentQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,employmentQuery,wildfoodsQuery)
            elif cropsQuery !='' and livestockQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,livestockQuery,loansQuery)
            elif cropsQuery !='' and livestockQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,livestockQuery,transfersQuery)
            elif cropsQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,livestockQuery,wildfoodsQuery)
            elif cropsQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,loansQuery,transfersQuery)
            elif cropsQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (cropsQuery,loansQuery,wildfoodsQuery)
            elif employmentQuery !='' and livestockQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (employmentQuery,livestockQuery,loansQuery)
            elif employmentQuery !='' and livestockQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (employmentQuery,livestockQuery,transfersQuery)
            elif employmentQuery !='' and livestockQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (employmentQuery,livestockQuery,wildfoodsQuery)
            elif employmentQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (employmentQuery,loansQuery,transfersQuery)
            elif employmentQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (employmentQuery,loansQuery,wildfoodsQuery)
            elif livestockQuery !='' and loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (livestockQuery,loansQuery,transfersQuery)
            elif livestockQuery !='' and loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (livestockQuery,loansQuery,wildfoodsQuery)
            elif loansQuery !='' and transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid
                                LEFT JOIN (%s) table3 ON table2.hhid = table3.hhid )''' % (loansQuery,transfersQuery,wildfoodsQuery)

            # conditions for combinations of 2 income source categories for output
            elif cropsQuery !='' and employmentQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,employmentQuery)
            elif cropsQuery !='' and livestockQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,livestockQuery)
            elif cropsQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,loansQuery)
            elif cropsQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,transfersQuery)
            elif cropsQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (cropsQuery,wildfoodsQuery)
            elif employmentQuery !='' and livestockQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,livestockQuery)
            elif employmentQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,loansQuery)
            elif employmentQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,transfersQuery)
            elif employmentQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (employmentQuery,wildfoodsQuery)
            elif livestockQuery !='' and loansQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,loansQuery)
            elif livestockQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,transfersQuery)
            elif livestockQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (livestockQuery,wildfoodsQuery)
            elif loansQuery !='' and transfersQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (loansQuery,transfersQuery)
            elif loansQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (loansQuery,wildfoodsQuery)
            elif transfersQuery !='' and wildfoodsQuery !='':
                query = ''' SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 ON table1.hhid = table2.hhid)''' % (transfersQuery,wildfoodsQuery)

            # conditions for combinations of 1 income source category for output
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

