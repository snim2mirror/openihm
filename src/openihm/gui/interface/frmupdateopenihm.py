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

# some needed modules
import os
import logging
import stat
import tempfile

# Import modules used by the automatic software updator.
from mercurial import commands, hg, ui, error
from distutils.dir_util import copy_tree
import shutil
import sys
import traceback

# QT modules
from PyQt4 import QtGui, QtCore, uic

Ui_UpdateOpenIHM, base_class = uic.loadUiType("gui/designs/ui_updateopenihm.ui")

# FIXME: Edit this value in Brown's innosetup script, take it from an .ini file.
REPO_DIR = os.path.expanduser(os.path.join('~', '.openihmrepo'))

# FIXME: Can we get INSTALL_DIR from an .ini file or similar?
INSTALL_DIR = os.path.normpath(os.path.dirname(__file__) + '../../../')
#INSTALL_DIR = '/home/snim2/site-packages' # Just for testing

# FIXME: Refactor this out to its own file.
class OpenIhmUpdator(QtCore.QThread):
    """This class automatically updates open-ihm from the Google Code repository.

    Requires Mercurial to be installed.
    """

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.logger = logging.getLogger('__main__')
        self.info = lambda msg : self.logger.info(msg)
        self.debug = lambda msg : self.logger.debug(msg)        
        self.ui = ui.ui()
        self.url = 'https://open-ihm.googlecode.com/hg/'
        try:
            self.repo = hg.repository(self.ui, REPO_DIR)
        except Exception:
            self.repo = hg.repository(self.ui, REPO_DIR, create=True)
        return

    def chmod(self):
        """Fix a Windows bug which marks files / folders in REPO_DIR read-only.
        """
        if not (sys.platform == 'win32' or sys.platform == 'cygwin'):
            return
        for root, dirs, files in os.walk(REPO_DIR):
            for name in files:
                os.chmod(os.path.join(root, name), stat.S_IWRITE)
            for name in dirs:
                os.chmod(os.path.join(root, name), stat.S_IWRITE)                

    def fail(self):
        """Called if an error occurs.

        Take the traceback, log it and notify the MainWindow.
        """
        ty, value, tback = sys.exc_info()
        msg = ''.join(traceback.format_exception(ty, value, tback))
        self.debug(msg)
        self.updateFail(msg)
        return

    def run(self):
        # Redirect stdin and stdout to tempfiles. 
        # This fixes a Windows bug which causes a Bad File Descriptor error.
        sys.stdout = tempfile.TemporaryFile()
        sys.stderr = tempfile.TemporaryFile()
        try:
            self.pullAndMerge()
        except Exception:
            self.fail()
            return
        try:
            self.install()
        except Exception:
            self.fail()
            return
        self.emit(QtCore.SIGNAL("updateSuccess()"))
        return

    def clone(self):
        """If we don't have a copy of the open-ihm repository on disk
        clone one now.
        """
        try:
            self.chmod()
            commands.clone(self.ui, self.url, dest=REPO_DIR, insecure=True)
        except Exception:
            self.fail()
        return

    def pullAndMerge(self):
        """Run an hg pull and update.
        Overwrite all local changes by default.
        If anything goes wrong with the pull or update, clone instead.
        """
        try:
            self.chmod()
            commands.pull(self.ui, self.repo, source=self.url)
            self.chmod()
            commands.update(self.ui, self.repo, clean=True)
        except error.RepoError:
            if os.path.exists(REPO_DIR):
                shutil.rmtree(REPO_DIR)
                self.clone()
        return
    
    def install(self):
        """Copy code to site-packages.

        FIXME: Do this with setuptools or distutils or similar. May need runpy.
        """
        copy_tree(os.path.join(REPO_DIR, 'src/openihm'), INSTALL_DIR)
        return

    def updateFail(self, message):
        """If checking for updates times out (for example, if there
        is no current network connection) then fail silently.
        """
        self.emit(QtCore.SIGNAL("updateFailure(QString)"), QtCore.QString(message))
        return
        
class FrmUpdateOpenIHM(QtGui.QDialog, Ui_UpdateOpenIHM):
    ''' Creates the Main Window of the application using the main 
    window design in the gui.designs.ui_updateopenihm module '''
    
    def __init__(self, parent=None):
        ''' Initialises Dialog '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.thread = OpenIhmUpdator() 
        self.updateSuccessful = True
        
    def updateOpenIHM(self):
        """Automatically fetch and install latest software from Google Code repo.
        """
        todo = self.cmdUpdate.text()
        
        if todo == "Update":
            msg = ("Software update starting. \n" +
                   "This may take some time.\n" +
                   "Please make sure you have a working Internet connection" +
                   "and do not close open-ihm until you see a message " +
                   "saying that the update has finished.")
            QtGui.QMessageBox.information(self, "Software update notice", msg)
            self.txtFeedback.setPlainText("Wait: Update in Progress ...")
            self.connect(self.thread, QtCore.SIGNAL("updateSuccess()"), self.updateSuccess)
            self.connect(self.thread, QtCore.SIGNAL("updateFailure(QString)"), self.updateFailed)
            self.connect(self.thread, QtCore.SIGNAL("noChanges()"), self.updateNoChanges)
            self.thread.start()
            return
        else:
            self.closeForm()
            
    def closeForm(self):
        self.close()
        
    def updateNoChanges(self):
        """No changes to pull.

        FIXME: Could remove this if it the updator never signals.
        """
        msg = ( "There are no software updates currently available." )
        QtGui.QMessageBox.critical(self, "Software update notice", msg)
        self.txtFeedback.setPlainText("Update Notice\n\nThere are no software updates currently available.")
        self.cmdUpdate.setText("Close")
        return
    
    def updateFailed(self, message):
        """Report to the user that a software update has failed.
        """
        msg = ("Software update failed.\n" +
               "Click OK to see details" )
               
        self.txtFeedback.setPlainText(message)
        QtGui.QMessageBox.critical(self, "Software update notice", msg)
        self.cmdUpdate.setText("Close")
        return

    def updateSuccess(self):
        """Report to the user that a software update has been successful.
        open-ihm now needs to be restarted.
        """
        msg = ("Software update was successful.")
        QtGui.QMessageBox.information(self, "Software update notice", msg)
        self.txtFeedback.setPlainText("Update Completed\n\n" +
                                      "Close this tool and start openihm for the updates to take effect.")
        self.cmdUpdate.setText("Close")
        return
