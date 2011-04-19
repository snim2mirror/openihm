# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_openihm.ui'
#
# Created: Tue Apr 19 08:09:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutOpenIHM(object):
    def setupUi(self, AboutOpenIHM):
        AboutOpenIHM.setObjectName(_fromUtf8("AboutOpenIHM"))
        AboutOpenIHM.resize(400, 300)
        AboutOpenIHM.setMinimumSize(QtCore.QSize(400, 300))
        self.cmdOk = QtGui.QPushButton(AboutOpenIHM)
        self.cmdOk.setGeometry(QtCore.QRect(290, 250, 75, 31))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.textEdit = QtGui.QTextEdit(AboutOpenIHM)
        self.textEdit.setGeometry(QtCore.QRect(3, 10, 391, 221))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(AboutOpenIHM)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutOpenIHM.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(AboutOpenIHM)

    def retranslateUi(self, AboutOpenIHM):
        AboutOpenIHM.setWindowTitle(QtGui.QApplication.translate("AboutOpenIHM", "About Open-IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("AboutOpenIHM", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("AboutOpenIHM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/EfDChancoComposite.jpg\" width=\"375\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">open-ihm is a software program used to analyse household income data, collected using the Individual Household Method (IHM). IHM is a method of collecting and analysing individual household income data, and was developed by <a href=\"http://www.evidencefordevelopment.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Evidence for Development</span></a>.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">open-ihm was written by Tiwonge Manda and Brown Msiska of <a href=\"http://www.chanco.unima.mw/\"><span style=\" text-decoration: underline; color:#0000ff;\">Chancellor College, University of Malawi</span></a>, with technical support from Sarah Mount, <a href=\"http://www.wlv.ac.uk\"><span style=\" text-decoration: underline; color:#0000ff;\">University of Wolverhampton </span></a>and Dai Clegg, <a href=\"http://www.netezza.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Netezza Corporation</span></a>. Celia Petty and John Seaman, Evidence for Development, provided domain expertise.  </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">open-ihm is based on <a href=\"http://www.evidencefordevelopment.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Evidence for Development</span></a>\'s analytical software, written by John Seaman.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In using open-ihm software, IHM data collection protocols must be</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">followed. For information on training, contact <a href=\"mailto:info@evidencefordevelopment.com\"><span style=\" text-decoration: underline; color:#0000ff;\">info@evidencefordevelopment.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
