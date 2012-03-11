#!/usr/bin/env python

"""
The main module of Open IHM. PyQt4 is used to implement the GUI
of the system. Also used is the sys (system) package.

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


# imports from sys and PyQt4 packages
import sys
from PyQt4 import QtGui, QtCore

import logging
import logging.handlers
import traceback

LOGFILE = 'openihmlog.txt'

def main():
     log = logging.getLogger(__name__)
     log.setLevel(logging.DEBUG)
     handler = logging.handlers.RotatingFileHandler(LOGFILE, backupCount=5)
     log.addHandler(handler)

     #
     # Start open-ihm.
     #
     try:

          # import class that creates Open IHM Main Window
          from gui.interface.frmupdateopenihm import FrmUpdateOpenIHM
          
          log.info('updating openihm.')
          
          app = QtGui.QApplication(sys.argv)

          window = FrmUpdateOpenIHM()
          window.show()

          # enter the application event loop - accept and handle events until user exists the application.
          log.info('Starting main loop of GUI.')
          sys.exit(app.exec_())

     except Exception, e:
          log.debug('Exception raised in __main__.')
          ty, value, tback = sys.exc_info()
          log.debug('Exception raised in start script. Debug info follows:')
          log.debug(''.join(traceback.format_exception(ty, value, tback)))


if __name__ == '__main__':
     main()
