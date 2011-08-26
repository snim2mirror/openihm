#!/usr/bin/env python

"""
Mixin classes for the open-ihm GUI.
"""

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import includes.mysql.connector as connector
    
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

    TODO: move this from the gui package to a model (as in MVC) package.
    """

    def executeUpdateQuery(self, query):
        """Execute a query that needs to be committed to the database.
        For example, an INSERT or UPDATE query.
        """
        db = connector.Connect(**self.config)             
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        cursor.close()
        db.close()
        return
    
    def executeResultsQuery(self, query):
        """Execute a query for which the database will return results.
        For example a SELECT query.
        """
        db = connector.Connect(**self.config)             
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    
    def executeMultipleUpdateQueries(self, queries):
        """This method is idential to self.executeUpdateQuery
        except that it takes a list of query strings and executes each in turn
        """
        db = connector.Connect(**self.config)             
        cursor = db.cursor()
        for query in queries:
            cursor.execute(query)
            db.commit()
        cursor.close()
        db.close()
        return

    def executeMultipleResultsQueries(self, queries):
        """This method is idential to self.executeResultsQuery
        except that it takes a list of query strings, executes each in turn
        and returns a corresponding list of results.
        """
        results = []        
        db = connector.Connect(**self.config)             
        cursor = db.cursor()
        for query in queries:
            cursor.execute(query)
            result = cursor.fetchall()
            results.append(result)
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
