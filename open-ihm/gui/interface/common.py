#-------------------------------------------------------------------	
#	Filename: common.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def countRowsSelected(tblVw):
     selectedRows = getSelectedRows(tblVw)
     return len(selectedRows)

def getSelectedRows(tblVw):
     selectedRows = []
     selectedIndexes = tblVw.selectedIndexes()

     for indexVal in selectedIndexes:
         if indexVal.row() not in selectedRows:
             selectedRows.append(indexVal.row())

     return selectedRows

def getCurrentRow(tblVw):
     indexVal = tblVw.currentIndex()
     return indexVal.row()
     
def getDbString(strSeed):
     return strSeed.replace("'", "xxx")
     
def getViewString(strSeed):
     return strSeed.replace("xxx", "'")
     
def getStringMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     return months[month]
     
def getIntMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     return months[month]

