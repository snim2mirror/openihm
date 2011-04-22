#!/usr/bin/env python

"""
Mixin classes for the open-ihm GUI.
"""

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *


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
        print 'MDIDialogMixin'
        if hasattr(self, 'mdi') and self.mdi is not None:
            self.mdi.closeActiveSubWindow()
            print 'self.mdi.closeActiveSubWindow()'
        elif hasattr(self, 'parent') and hasattr(self.parent, 'closeActiveSubWindow'):
            self.parent.closeActiveSubWindow()
            print 'self.parent.closeActiveSubWindow()'
        elif hasattr(self, 'parent') and hasattr(self.parent, 'mdi'):
            self.parent.mdi.closeActiveSubWindow()
            print 'self.parent.mdi.closeActiveSubWindow()'
#        elif (hasattr(self, 'parent') and hasattr(self.parent, 'parent') and
#              hasattr(self.parent.parent, 'mdi')):
#            self.parent.parent.mdi.closeActiveSubWindow()
#            print 'self.parent.parent.mdi.closeActiveSubWindow()'        
        else:
            self.close()
            print 'self.close()'
        # This code *should* be unreachable
#        print 'UNREACHABLE'
#        self.close()
#        print 'REJECT'
#        self.reject()
#        return

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
