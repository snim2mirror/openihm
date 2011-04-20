# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_openihm.ui'
#
# Created: Wed Apr 20 15:53:50 2011
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AboutOpenIHM(object):
    def setupUi(self, AboutOpenIHM):
        AboutOpenIHM.setObjectName("AboutOpenIHM")
        AboutOpenIHM.resize(417, 467)
        AboutOpenIHM.setMinimumSize(QtCore.QSize(417, 467))
        self.cmdOk = QtGui.QPushButton(AboutOpenIHM)
        self.cmdOk.setGeometry(QtCore.QRect(320, 430, 75, 31))
        self.cmdOk.setObjectName("cmdOk")
        self.textEdit = QtGui.QTextEdit(AboutOpenIHM)
        self.textEdit.setGeometry(QtCore.QRect(3, 10, 411, 411))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(AboutOpenIHM)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL("clicked()"), AboutOpenIHM.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(AboutOpenIHM)

    def retranslateUi(self, AboutOpenIHM):
        AboutOpenIHM.setWindowTitle(QtGui.QApplication.translate("AboutOpenIHM", "About Open-IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("AboutOpenIHM", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("AboutOpenIHM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/EfDChancoComposite.jpg\" width=\"375\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">open-ihm is a software program used to analyse household income data, collected using the Individual Household Method (IHM). IHM is a method of collecting and analysing individual household income data, and was developed by </span><a href=\"http://www.evidencefordevelopment.com\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">Evidence for Development</span></a><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">open-ihm was written by Tiwonge Manda and Brown Msiska of </span><a href=\"http://www.chanco.unima.mw/\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">Chancellor College, University of Malawi</span></a><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">, with technical support from Sarah Mount, </span><a href=\"http://www.wlv.ac.uk\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">University of Wolverhampton </span></a><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">and Dai Clegg, </span><a href=\"http://www.netezza.com/\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">Netezza Corporation</span></a><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">. Celia Petty and John Seaman, Evidence for Development, provided domain expertise.  </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">open-ihm is based on </span><a href=\"http://www.evidencefordevelopment.com\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">Evidence for Development</span></a><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">\'s analytical software, written by John Seaman.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">In using open-ihm software, IHM data collection protocols must be</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">followed. For information on training, contact </span><a href=\"mailto:info@evidencefordevelopment.com\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">info@evidencefordevelopment.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
