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


from database import Database

class EditIncomesourcesReferenceData:
    def __init__(self):
        self.database = Database()
        '''self.incomesource = incomesource
        self.percentageincome = mpercentageincome
        self.percentageproduction = mpercentageproduction
        self.projectid = projectid'''

    def setIncomeData(self,incomesource,percentageincome, percentageproduction,projectid):
        if incomesource == "Employment":
            incomesourcetable ='employmentincome'
            query = '''UPDATE %s SET preferenceincome=%s WHERE pid=%s''' % (incomesourcetable,percentageincome, projectid)

        elif incomesource == "Crops":
            incomesourcetable ='cropincome'
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction =%s
                        WHERE pid=%s''' % (incomesourcetable,percentageincome, percentageproduction,projectid)

        elif incomesource == "Informal Tansfers":
            incomesourcetable ='transfers'
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction =%s
                        WHERE sourcetype='Internal' AND pid=%s''' % (incomesourcetable,percentageincome, percentageproduction,projectid)

        elif incomesource == "Livestock":
            incomesourcetable ='livestockincome'
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction =%s
                        WHERE pid=%s''' % (incomesourcetable,percentageincome, percentageproduction,projectid)

        elif incomesource == "Formal Transfers":
            incomesourcetable ='transfers'
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction =%s
                        WHERE sourcetype='External' AND pid=%s''' % (incomesourcetable,percentageincome, percentageproduction,projectid)

        elif incomesource == "WildFoods":
            incomesourcetable ='wildfoods'
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction =%s
                        WHERE pid=%s''' % (incomesourcetable,percentageincome, percentageproduction,projectid)

        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()

    def restDietModelData(self,projectid):
        #modelprice = 1 # default value for used when resetin model price, in GUI, can be set here
        #query = '''UPDATE diet SET modelprice=%s WHERE pid=%s''' % (modelprice,projectid)
        query = '''UPDATE diet SET modelprice=priceperunit WHERE pid=%s''' % (projectid)

        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()

    def resetStandardOfLivingModelData(self,projectid):
        #modelprice = 1 # default value for used when resetin model price, in GUI, can be set here 
        #query = '''UPDATE standardofliving SET modelprice=%s WHERE pid=%s''' % (modelprice,projectid)
        query = '''UPDATE standardofliving SET modelprice=costperyear WHERE pid=%s''' % (projectid)

        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
