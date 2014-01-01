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


# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from data.config import Config

# import the Create Project Dialog design class
Ui_FindHousehold, base_class = uic.loadUiType("gui/designs/ui_findhousehold.ui")

from frmfindhouseholdresults import FrmFindHouseholdResults

from mixins import MDIDialogMixin
from data.db import session_scope
from model.alchemy_schema import Household
from sqlalchemy import or_


class FrmFindHousehold(QDialog, Ui_FindHousehold, MDIDialogMixin):
    ''' Creates the Find Household form'''
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.config = Config.dbinfo().copy()

    def findHousehold(self):
        ''' Find a household matching the criteria entered by user '''
        hhid = self.txtHouseholdNo.text()
        hhname = self.txtHouseholdName.text()

        pid = self.parent.projectid
        count = 0
        with session_scope() as session:
            q = session.query(Household).filter(Household.pid == pid)
            if hhname != "":
                if hhid == "":
                    q = q.filter(Household.householdname.like(hhname))
                else:
                    q = q.filter(or_(Household.householdname.like(hhname), 
                                        Household.hhid == hhid))
            elif hhid != "":
                q = q.filter(Household.hhid == hhid)
            count = q.count()

        if ( count != 0 ):
            form = FrmFindHouseholdResults( self.parent, hhid, hhname )
            subWin = self.parent.mdi.addSubWindow( form )
            self.parent.centerSubWindow( subWin )
            # close this form
            self.parent.mdi.closeActiveSubWindow()
            # show the details form
            form.showMaximized()
        else:
            msg = "No household matching the criteria specified exists."
            QMessageBox.information( self, "Find Household", msg )
