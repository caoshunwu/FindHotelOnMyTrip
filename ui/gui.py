# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_1 = QtWidgets.QGridLayout()
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.checkInLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.checkInLineEdit.setObjectName("checkInLineEdit")
        self.gridLayout_1.addWidget(self.checkInLineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_1.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_1.addWidget(self.label_3, 1, 2, 1, 1)
        self.roomsComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.roomsComboBox.setObjectName("roomsComboBox")
        self.roomsComboBox.addItem("")
        self.roomsComboBox.addItem("")
        self.roomsComboBox.addItem("")
        self.roomsComboBox.addItem("")
        self.roomsComboBox.addItem("")
        self.roomsComboBox.addItem("")
        self.gridLayout_1.addWidget(self.roomsComboBox, 2, 1, 1, 1)
        self.checkOutLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.checkOutLineEdit.setObjectName("checkOutLineEdit")
        self.gridLayout_1.addWidget(self.checkOutLineEdit, 1, 3, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout_1.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_1.addWidget(self.label_5, 2, 4, 1, 1)
        self.childsComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.childsComboBox.setObjectName("childsComboBox")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.childsComboBox.addItem("")
        self.gridLayout_1.addWidget(self.childsComboBox, 2, 5, 1, 1)
        self.adultsComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.adultsComboBox.setObjectName("adultsComboBox")
        self.adultsComboBox.addItem("")
        self.adultsComboBox.addItem("")
        self.adultsComboBox.addItem("")
        self.adultsComboBox.addItem("")
        self.adultsComboBox.addItem("")
        self.adultsComboBox.addItem("")
        self.gridLayout_1.addWidget(self.adultsComboBox, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem, 2, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_1.addWidget(self.label, 2, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.gridLayout_1.addWidget(self.addButton, 0, 6, 1, 1)
        self.hotelLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.hotelLineEdit.setObjectName("hotelLineEdit")
        self.gridLayout_1.addWidget(self.hotelLineEdit, 0, 1, 1, 5)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_1.addWidget(self.label_4, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem1, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setStatusTip("")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deleteButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout_2.addWidget(self.deleteButton)
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_2.addWidget(self.clearButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLinsence = QtWidgets.QAction(MainWindow)
        self.actionLinsence.setObjectName("actionLinsence")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionLinsence)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.adultsComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkInLineEdit.setText(_translate("MainWindow", "2019-02-22"))
        self.label_2.setText(_translate("MainWindow", "Check In"))
        self.label_3.setText(_translate("MainWindow", "Check Out"))
        self.roomsComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.roomsComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.roomsComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.roomsComboBox.setItemText(3, _translate("MainWindow", "4"))
        self.roomsComboBox.setItemText(4, _translate("MainWindow", "5"))
        self.roomsComboBox.setItemText(5, _translate("MainWindow", "6"))
        self.checkOutLineEdit.setText(_translate("MainWindow", "2019-02-24"))
        self.label_1.setText(_translate("MainWindow", "Hotel"))
        self.label_5.setText(_translate("MainWindow", "Childs"))
        self.childsComboBox.setItemText(0, _translate("MainWindow", "0"))
        self.childsComboBox.setItemText(1, _translate("MainWindow", "1"))
        self.childsComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.childsComboBox.setItemText(3, _translate("MainWindow", "3"))
        self.childsComboBox.setItemText(4, _translate("MainWindow", "4"))
        self.childsComboBox.setItemText(5, _translate("MainWindow", "5"))
        self.childsComboBox.setItemText(6, _translate("MainWindow", "6"))
        self.adultsComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.adultsComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.adultsComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.adultsComboBox.setItemText(3, _translate("MainWindow", "4"))
        self.adultsComboBox.setItemText(4, _translate("MainWindow", "5"))
        self.adultsComboBox.setItemText(5, _translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "Rooms"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.label_4.setText(_translate("MainWindow", "Adults"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hotel"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Check In"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Check Out"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Days"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Rooms"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Adults"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Childs"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLinsence.setText(_translate("MainWindow", "License"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

