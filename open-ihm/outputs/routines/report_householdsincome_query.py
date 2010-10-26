#-------------------------------------------------------------------	
#	Filename: report_householdsincome_query.py
#-------------------------------------------------------------------

class HouseholdIncomeQuery:
    def __init__(self):
        self.query = ''

    def buildFinalReportQuery (self,projectid,householdIDs,cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery):
        
        householdids = ','.join(householdIDs)
        if len(householdIDs)!=0:
            
            if cropsQuery !='' or employmentQuery!='' or livestockQuery !='' or loansQuery !='' or transfersQuery !='' or wildfoodsQuery !='':
                self.query  = '''SELECT hhid from households WHERE hhid IN (%s) and pid =%s''' % (householdids,projectid)
                if cropsQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,cropsQuery)
                if employmentQuery!='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,employmentQuery)
                if livestockQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,livestockQuery)
                if loansQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,loansQuery)
                if transfersQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,transfersQuery)
                if wildfoodsQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,wildfoodsQuery)
            else:
                QMessageBox.information(self,"Households By Income Source","No Income sources Selected")
        print self.query 
        return self.query 
