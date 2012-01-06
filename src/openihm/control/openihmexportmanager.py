#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
from datetime import date
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

from model.database import Database          # connector to mysql database
from datetime import date

class OpenIhmExportManager:
     def exportIhmProject(self, projectid,  filename):
         project = self.getProject(projectid)                  # self refers to controller which inherits OpenIhmExportManager
         projectline = "project<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>" \
                           % (project.projectname + " [imported]", project.startdate, project.enddate,  project.description,  project.currency)
         ihmFile = open(filename, 'w')
         ihmFile.write(projectline)
         ihmFile.close()
    
