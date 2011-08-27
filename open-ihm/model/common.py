#-------------------------------------------------------------------	
#	Filename: common.py
#-------------------------------------------------------------------
 
def getDbString(strSeed):
     return strSeed.replace("'", "xxx")
     
def getViewString(strSeed):
     return strSeed.replace("xxx", "'")
     
def getStringMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     for key, val in months.items():
         if str(month) == key:
             return val
     
def getIntMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     for key, val in months.items():
         if month == val:
             return key
