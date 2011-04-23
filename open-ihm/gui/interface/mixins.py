#!/usr/bin/env python

"""
Mixin classes for the open-ihm GUI.
"""

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import data.mysql.connector
    
class TableViewMixin(object):

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


class MDIDialogMixin(object):
    """Used by all dialog boxes.
    """

    def setMdi(self, mdi):
        self.mdi = mdi
        
    def mdiClose(self):
        """Close this dialog box.
        
        The dialog may be the active sub-window of an MDI area, or not.
        """
        if hasattr(self, 'mdi') and self.mdi is not None:
            self.mdi.closeActiveSubWindow()
        elif hasattr(self, 'parent') and hasattr(self.parent, 'closeActiveSubWindow'):
            self.parent.closeActiveSubWindow()
        elif hasattr(self, 'parent') and hasattr(self.parent, 'mdi'):
            self.parent.mdi.closeActiveSubWindow()
        else:
            self.close()
        return


class MySQLMixin(object):
    """Methods for dealing with the MySQL database.

    TODO: move this class to a model (as in MVC) package
    FIXME: this should be four different methods.
    """

    def executeQuery(self, query):
        results = None
        
        db = data.mysql.connector.Connect(**self.config)             
        cursor = db.cursor()
        cursor.execute(query)
        try:
            results = cursor.fetchall()
        except Exception, e:
            pass
        try:
            cursor.commit()
        except Exception, e:
            pass
        cursor.close()
        db.close()
        return results

    def executeMultipleQueries(self, queries):
        results = []
        
        db = data.mysql.connector.Connect(**self.config)             
        cursor = db.cursor()
        for query in queries:
            cursor.execute(query)
            try:
                result = cursor.fetchall()
                results.append(result)
            except Exception, e:
                results.append(None)
            try:
                cursor.commit()
            except Exception, e:
                pass
        cursor.close()
        db.close()
        return results
        
    
class DataEntryMixin(object):
    
    def getDbString(strSeed):
         return strSeed.replace("'", "xxx")

    def getViewString(strSeed):
         return strSeed.replace("xxx", "'")

    def getStringMonth(month):
        return {"1" : "January","2" : "February", "3" : "March", "4" : "April",
                "5" : "May","6" : "June", "7" : "July","8" : "August",
                "9" : "September","10" : "October","11" : "November",
                "12" : "December"}[month]

    def getIntMonth(month):
        return {"1" : "January","2" : "February", "3" : "March", "4" : "April",
                "5" : "May","6" : "June", "7" : "July","8" : "August",
                "9" : "September","10" : "October","11" : "November",
                "12" : "December"}[month]
