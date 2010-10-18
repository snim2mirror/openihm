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
                pass
            elif cropsQuery !='' and livestockQuery !='':
                pass
            elif cropsQuery !='' and loansQuery !='':
                pass
            elif cropsQuery !='' and transfersQuery !='':
                pass
            elif cropsQuery !='' and wildfoodsQuery !='':
                pass
            elif employmentQuery !='' and livestockQuery !='':
                pass
            elif employmentQuery !='' and loansQuery !='':
                pass
            elif employmentQuery !='' and transfersQuery !='':
                pass
            elif employmentQuery !='' and wildfoodsQuery !='':
                pass
            elif livestockQuery !='' and loansQuery !='':
                pass
            elif livestockQuery !='' and transfersQuery !='':
                pass
            elif livestockQuery !='' and wildfoodsQuery !='':
                pass
            elif loansQuery !='' and transfersQuery !='':
                pass
            elif loansQuery !='' and wildfoodsQuery !='':
                pass
            elif transfersQuery !='' and wildfoodsQuery !='':
                pass

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

