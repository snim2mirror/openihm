# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findprojectresults.ui'
#
# Created: Thu Apr 21 19:28:06 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindProjectResults(object):
    def setupUi(self, FindProjectResults):
        FindProjectResults.setObjectName(_fromUtf8("FindProjectResults"))
        FindProjectResults.resize(548, 468)
        FindProjectResults.setMinimumSize(QtCore.QSize(548, 424))
        self.verticalLayout_2 = QtGui.QVBoxLayout(FindProjectResults)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FindProjectResults)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtProjectID = QtGui.QLineEdit(self.groupBox)
        self.txtProjectID.setObjectName(_fromUtf8("txtProjectID"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtProjectID)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtProjectTitle = QtGui.QLineEdit(self.groupBox)
        self.txtProjectTitle.setObjectName(_fromUtf8("txtProjectTitle"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtProjectTitle)
        self.cmdSearch = QtGui.QPushButton(self.groupBox)
        self.cmdSearch.setObjectName(_fromUtf8("cmdSearch"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmdSearch)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(FindProjectResults)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblResults = QtGui.QTableView(self.groupBox_3)
        self.tblResults.setAlternatingRowColors(True)
        self.tblResults.setSortingEnabled(True)
        self.tblResults.setObjectName(_fromUtf8("tblResults"))
        self.verticalLayout.addWidget(self.tblResults)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(FindProjectResults)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOpen = QtGui.QPushButton(self.groupBox_2)
        self.cmdOpen.setObjectName(_fromUtf8("cmdOpen"))
        self.horizontalLayout.addWidget(self.cmdOpen)
        self.cmdClose = QtGui.QPushButton(self.groupBox_2)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(FindProjectResults)
        QtCore.QObject.connect(self.cmdSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.showResults)
        QtCore.QObject.connect(self.cmdOpen, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.openProject)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(FindProjectResults)
        FindProjectResults.setTabOrder(self.txtProjectID, self.txtProjectTitle)
        FindProjectResults.setTabOrder(self.txtProjectTitle, self.cmdSearch)

    def retranslateUi(self, FindProjectResults):
        FindProjectResults.setWindowTitle(QtGui.QApplication.translate("FindProjectResults", "Project Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FindProjectResults", "Search Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FindProjectResults", "Enter Project ID or Project Title [entering nothing will list all projects]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindProjectResults", "Project ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindProjectResults", "Project Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSearch.setText(QtGui.QApplication.translate("FindProjectResults", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("FindProjectResults", "Found Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOpen.setText(QtGui.QApplication.translate("FindProjectResults", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("FindProjectResults", "Close", None, QtGui.QApplication.UnicodeUTF8))

