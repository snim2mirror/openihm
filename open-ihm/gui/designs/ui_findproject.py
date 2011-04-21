# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findproject.ui'
#
# Created: Thu Apr 21 19:32:46 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindProject(object):
    def setupUi(self, FindProject):
        FindProject.setObjectName(_fromUtf8("FindProject"))
        FindProject.resize(440, 201)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FindProject.sizePolicy().hasHeightForWidth())
        FindProject.setSizePolicy(sizePolicy)
        FindProject.setMinimumSize(QtCore.QSize(400, 160))
        self.formLayout = QtGui.QFormLayout(FindProject)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(FindProject)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label = QtGui.QLabel(FindProject)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtProjectID = QtGui.QLineEdit(FindProject)
        self.txtProjectID.setObjectName(_fromUtf8("txtProjectID"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtProjectID)
        self.label_2 = QtGui.QLabel(FindProject)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtProjectTitle = QtGui.QLineEdit(FindProject)
        self.txtProjectTitle.setObjectName(_fromUtf8("txtProjectTitle"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtProjectTitle)
        self.groupBox = QtGui.QGroupBox(FindProject)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOk = QtGui.QPushButton(self.groupBox)
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.horizontalLayout.addWidget(self.cmdOk)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(FindProject)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProject.findProject)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProject.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(FindProject)
        FindProject.setTabOrder(self.txtProjectID, self.txtProjectTitle)

    def retranslateUi(self, FindProject):
        FindProject.setWindowTitle(QtGui.QApplication.translate("FindProject", "Find Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindProject", "Enter Project ID or Project Title [entering nothing will list all projects]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindProject", "Project ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindProject", "Project Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("FindProject", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("FindProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

