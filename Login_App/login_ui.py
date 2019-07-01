# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(474, 329)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:    qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.5625 rgba(78, 164, 255, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"border-bottom: 1px solid darkgrey;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 8pt \"Rockwell\";\n"
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    color: #555;\n"
"    background-color: #fff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border-color:#66afe9;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLCDNumber{\n"
"color: rgb(255, 85, 0);\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 71))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(250, 250, 250, 90), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom: 1px solid darkgrey;}\n"
"\n"
"QToolButton{\n"
"    font: 9pt \"Rockwell\";\n"
"    background-color:transparent;\n"
"    border:none;\n"
"}\n"
"\n"
"QToolButton:Checked, QToolButton:presses{\n"
"    background-color:rgb(193,220,255);\n"
"    border: 1px solid rgb(60,127,177);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color:rgb(224,232,246);\n"
"}\n"
"\n"
"QToolButton::checked:hover{\n"
"background-color:rgb(193,210,238);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.facebook = QtWidgets.QToolButton(self.layoutWidget)
        self.facebook.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facebook.setMouseTracking(False)
        self.facebook.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebook.setIcon(icon1)
        self.facebook.setIconSize(QtCore.QSize(32, 32))
        self.facebook.setCheckable(True)
        self.facebook.setChecked(False)
        self.facebook.setAutoRepeat(False)
        self.facebook.setAutoExclusive(True)
        self.facebook.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.facebook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.facebook.setArrowType(QtCore.Qt.NoArrow)
        self.facebook.setObjectName("facebook")
        self.horizontalLayout.addWidget(self.facebook)
        self.twitter = QtWidgets.QToolButton(self.layoutWidget)
        self.twitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twitter.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter.setIcon(icon2)
        self.twitter.setIconSize(QtCore.QSize(32, 32))
        self.twitter.setCheckable(True)
        self.twitter.setAutoExclusive(True)
        self.twitter.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twitter.setObjectName("twitter")
        self.horizontalLayout.addWidget(self.twitter)
        self.instagram = QtWidgets.QToolButton(self.layoutWidget)
        self.instagram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.instagram.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagram.setIcon(icon3)
        self.instagram.setIconSize(QtCore.QSize(32, 32))
        self.instagram.setCheckable(True)
        self.instagram.setAutoExclusive(True)
        self.instagram.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.instagram.setObjectName("instagram")
        self.horizontalLayout.addWidget(self.instagram)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(150, 270, 166, 31))
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"Rockwell\";\n"
"font-size:14px;\n"
"border:1px solid transparent;\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"background-color: #428bca;\n"
"border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color:#3071a9;\n"
"border-color: #285e8e;\n"
"}")
        self.login.setObjectName("login")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 90, 371, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLineEdit(self.layoutWidget1)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.layoutWidget1)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 220, 291, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ClockLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.ClockLabel.setStyleSheet("QLabel{\n"
"font: 14pt \"Palatino Linotype\";\n"
"color: rgb(255, 85, 0);\n"
"}")
        self.ClockLabel.setIndent(5)
        self.ClockLabel.setObjectName("ClockLabel")
        self.horizontalLayout_2.addWidget(self.ClockLabel)
        self.Clock = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.Clock.setAutoFillBackground(False)
        self.Clock.setStyleSheet("QLCDNumber{rgb(255, 85, 0)}")
        self.Clock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Clock.setLineWidth(1)
        self.Clock.setMidLineWidth(0)
        self.Clock.setNumDigits(8)
        self.Clock.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.Clock.setObjectName("Clock")
        self.horizontalLayout_2.addWidget(self.Clock)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log in Application"))
        self.facebook.setText(_translate("Dialog", "Facebook"))
        self.facebook.setShortcut(_translate("Dialog", "Ctrl+F"))
        self.twitter.setText(_translate("Dialog", "Twitter"))
        self.twitter.setShortcut(_translate("Dialog", "Ctrl+T"))
        self.instagram.setText(_translate("Dialog", "Instagram"))
        self.instagram.setShortcut(_translate("Dialog", "Ctrl+I"))
        self.login.setText(_translate("Dialog", "Log in"))
        self.username.setPlaceholderText(_translate("Dialog", "Username"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.ClockLabel.setText(_translate("Dialog", "Current Time:"))

import icons_rc
