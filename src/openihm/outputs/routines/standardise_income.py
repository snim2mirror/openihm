    def getReportTable(self,query):
        result = []
        databaseConnector = Database()
        if query !='':
            db = data.mysql.connector.Connect(**self.config)
            cursor = db.cursor()
	    cursor.execute(query)
            columns = tuple( [d[0].decode('utf8') for d in cursor.description] )
            rows = cursor.fetchall()
            for row in rows:
                if reporttype = 'standardised':
                    hhid = row[0]
                    householdAE = self.getAdultEquivalent(hhid,pid)
                    row = self.standardiseIncome(self,row,householdAE)
                print row
                result.append(dict(zip(columns, row)))
                
	    # close database connection
            cursor.close()
            db.close()
        return result

    def getAdultEquivalent(self, hhid,pid):
        adultEquivalentCalc = AdultEquivalent()
        householdAE = adultEquivalentCalc.calculateHouseholdEnergyReq(hhid,pid)
        return householdAE
        
    def standardiseIncome(self,row,householdAE):
        listlength = len(row)
        for i in range(1,listlength):
            if row[i]:
                row[i]=row[i]/householdAE

        return row
