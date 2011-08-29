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
from PyQt4 import QtGui, QtCore

from data.controller import Controller

# import the Edit Project Dialog design class
from gui.designs.ui_editproject_details import Ui_EditProject

from mixins import MDIDialogMixin

class FrmEditProject(QtGui.QDialog, Ui_EditProject, MDIDialogMixin):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        
        # get current project details
        controller  = Controller()
        self.getCurrencies()
        self.project     = controller.getProject( self.parent.projectid )
        self.getProjectData()
        
        # allow the calendar widget to pop up
        self.dtpStartDate.setCalendarPopup(True)
        self.dtpEndDate.setCalendarPopup(True)
        
    def getCurrencies(self):
        ''' Loads currencies into the currency combo box '''
        controller      = Controller()
        currencies = controller.getCurrencies()
        for currency in currencies:
            self.cmbCurrency.addItem(currency.name)
        
    def getProjectData(self):
        ''' Retrieves project data from the database '''
        self.lblProjectID.setText(str( self.project.getProjectID() ))
        self.txtProjectName.setText( self.project.getProjectName() )
        self.dtpStartDate.setDate( self.project.getStartDate() )
        if self.project.getEndDate() != None:
            self.dtpEndDate.setDate( self.project.getEndDate() )
        self.txtDescription.setText( self.project.getDescription() )
        self.cmbCurrency.setCurrentIndex(self.cmbCurrency.findText( self.project.getCurrency() ))
        
    def saveProject(self):
        ''' Saves changes database '''
                
        # get the data entered by user
        projectname = self.txtProjectName.text()
        startdate     = self.dtpStartDate.date().toString("yyyy-MM-dd")
        enddate       = self.dtpEndDate.date().toString("yyyy-MM-dd")
        description   = self.txtDescription.toPlainText()
        currency      = self.cmbCurrency.currentText()
        pid              = self.parent.projectid
        
        # save project changes
        self.project.setData(projectname, startdate, enddate, description, currency)
        
        # set the newly inserted project as the current project
        self.parent.projectname = projectname
        self.parent.setWindowTitle("Open IHM - " + projectname)
        
        # close new project window
        self.mdiClose()
