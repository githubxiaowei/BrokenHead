# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutda = QtWidgets.QHBoxLayout()
        self.horizontalLayoutda.setSpacing(1)
        self.horizontalLayoutda.setObjectName("horizontalLayoutda")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.List = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.List.setFont(font)
        self.List.setMouseTracking(False)
        self.List.setTabletTracking(False)
        self.List.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.List.setInputMethodHints(QtCore.Qt.ImhNone)
        self.List.setWordWrap(False)
        self.List.setSelectionRectVisible(False)
        self.List.setObjectName("List")
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        self.verticalLayout.addWidget(self.List)
        self.horizontalLayoutda.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.view2d = QtWidgets.QGraphicsView(self.centralwidget)
        self.view2d.setObjectName("view2d")
        self.horizontalLayout.addWidget(self.view2d)
        self.view3d = QtWidgets.QGraphicsView(self.centralwidget)
        self.view3d.setObjectName("view3d")
        self.horizontalLayout.addWidget(self.view3d)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayoutda.addLayout(self.verticalLayout_2)
        self.NIImessage = QtWidgets.QTextBrowser(self.centralwidget)
        self.NIImessage.setObjectName("NIImessage")
        self.horizontalLayoutda.addWidget(self.NIImessage)
        self.horizontalLayoutda.setStretch(0, 1)
        self.horizontalLayoutda.setStretch(1, 4)
        self.horizontalLayoutda.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayoutda, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.menu.addSeparator()
        self.menu.addAction(self.actionopen)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BrokenHead"))
        __sortingEnabled = self.List.isSortingEnabled()
        self.List.setSortingEnabled(False)
        item = self.List.item(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.List.item(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.List.item(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.List.item(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.List.item(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.List.item(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.List.item(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.List.item(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.List.item(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.List.item(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.List.item(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.List.item(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.List.item(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.List.item(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.List.item(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.List.item(15)
        item.setText(_translate("MainWindow", "16"))
        self.List.setSortingEnabled(__sortingEnabled)
        self.NIImessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionopen.setText(_translate("MainWindow", "打开文件夹"))
        self.actionopen.setIconText(_translate("MainWindow", "open"))

