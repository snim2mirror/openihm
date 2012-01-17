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
from PyQt4 import QtGui, QtCore, uic

from control.controller import Controller

# import forms required to edit household
Ui_OpenProject, base_class = uic.loadUiType("gui/designs/ui_project_open.ui")

from mixins import MDIDialogMixin

class FrmOpenProject(QtGui.QDialog, Ui_OpenProject, MDIDialogMixin):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # get projects
        self.getProjects()
        
    def getProjects(self):
        # connect to mysql database
        controller = Controller()
        
        for project in controller.getProjects():
            projectid = project.getProjectID()
            projectname = project.getProjectName()
            self.cboProjectName.addItem(projectname, QtCore.QVariant(projectid))
    
    def openProject(self):
        ''' Show Household Details '''
        temp = self.cboProjectName.itemData(self.cboProjectName.currentIndex()).toInt()
        self.parent.projectid = temp[0]
        self.parent.projectname = self.cboProjectName.currentText()
        self.parent.setWindowTitle("Open IHM - " + self.cboProjectName.currentText())
        self.parent.actionClose_Project.setDisabled(False)
        self.mdiClose()
