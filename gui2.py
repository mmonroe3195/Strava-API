# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(200, 110, 60, 16))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.yearcombobox = QtWidgets.QComboBox(self.centralwidget)
        self.yearcombobox.setGeometry(QtCore.QRect(60, 80, 101, 22))
        self.yearcombobox.setObjectName("yearcombobox")
        self.yearcombobox.addItem("")
        self.yearcombobox.addItem("")
        self.yearcombobox.addItem("")
        self.yearcombobox.addItem("")
        self.yearcombobox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 571, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.actComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.actComboBox.setGeometry(QtCore.QRect(240, 80, 101, 22))
        self.actComboBox.setObjectName("actComboBox")
        self.actComboBox.addItem("")
        self.actComboBox.addItem("")
        self.actComboBox.addItem("")
        self.actComboBox.addItem("")
        self.actComboBox.setItemText(3, "")
        self.monthComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.monthComboBox.setGeometry(QtCore.QRect(430, 80, 101, 22))
        self.monthComboBox.setObjectName("monthComboBox")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 140, 471, 171))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.yearlabel = QtWidgets.QLabel(self.centralwidget)
        self.yearlabel.setGeometry(QtCore.QRect(60, 60, 60, 16))
        self.yearlabel.setObjectName("yearlabel")
        self.activitylabel = QtWidgets.QLabel(self.centralwidget)
        self.activitylabel.setGeometry(QtCore.QRect(240, 60, 91, 16))
        self.activitylabel.setObjectName("activitylabel")
        self.monthlabel = QtWidgets.QLabel(self.centralwidget)
        self.monthlabel.setGeometry(QtCore.QRect(430, 60, 71, 16))
        self.monthlabel.setObjectName("monthlabel")
        self.PieChartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PieChartBtn.setEnabled(False)
        self.PieChartBtn.setGeometry(QtCore.QRect(190, 320, 91, 51))
        self.PieChartBtn.setCheckable(False)
        self.PieChartBtn.setDefault(False)
        self.PieChartBtn.setObjectName("PieChartBtn")
        self.BarGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BarGraphBtn.setEnabled(False)
        self.BarGraphBtn.setGeometry(QtCore.QRect(300, 320, 91, 51))
        self.BarGraphBtn.setObjectName("BarGraphBtn")
        self.yearcombobox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.yearcombobox_2.setGeometry(QtCore.QRect(10, 340, 171, 22))
        self.yearcombobox_2.setObjectName("yearcombobox_2")
        self.yearcombobox_2.addItem("")
        self.yearcombobox_2.addItem("")
        self.yearcombobox_2.addItem("")
        self.yearlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.yearlabel_2.setGeometry(QtCore.QRect(10, 320, 141, 16))
        self.yearlabel_2.setObjectName("yearlabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yearcombobox.setItemText(0, _translate("MainWindow", "All"))
        self.yearcombobox.setItemText(1, _translate("MainWindow", "2018"))
        self.yearcombobox.setItemText(2, _translate("MainWindow", "2019"))
        self.yearcombobox.setItemText(3, _translate("MainWindow", "2020"))
        self.yearcombobox.setItemText(4, _translate("MainWindow", "2021"))
        self.label.setText(_translate("MainWindow", "Select a year,  activity type, and month option.  Then press \"Show Stats\" to see your data."))
        self.actComboBox.setItemText(0, _translate("MainWindow", "All Activities"))
        self.actComboBox.setItemText(1, _translate("MainWindow", "Bike"))
        self.actComboBox.setItemText(2, _translate("MainWindow", "Run"))
        self.monthComboBox.setItemText(0, _translate("MainWindow", "All Months"))
        self.monthComboBox.setItemText(1, _translate("MainWindow", "January"))
        self.monthComboBox.setItemText(2, _translate("MainWindow", "Feburary"))
        self.monthComboBox.setItemText(3, _translate("MainWindow", "March"))
        self.monthComboBox.setItemText(4, _translate("MainWindow", "April"))
        self.monthComboBox.setItemText(5, _translate("MainWindow", "May"))
        self.monthComboBox.setItemText(6, _translate("MainWindow", "June"))
        self.monthComboBox.setItemText(7, _translate("MainWindow", "July"))
        self.monthComboBox.setItemText(8, _translate("MainWindow", "August"))
        self.monthComboBox.setItemText(9, _translate("MainWindow", "Sepember"))
        self.monthComboBox.setItemText(10, _translate("MainWindow", "October"))
        self.monthComboBox.setItemText(11, _translate("MainWindow", "November"))
        self.monthComboBox.setItemText(12, _translate("MainWindow", "December"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "You traveled a total distnance of _ with Strava "))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "You ran a totla distance of _ with Strava."))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.yearlabel.setText(_translate("MainWindow", "Year:"))
        self.activitylabel.setText(_translate("MainWindow", "Activity Type:"))
        self.monthlabel.setText(_translate("MainWindow", "Month:"))
        self.PieChartBtn.setText(_translate("MainWindow", "Pie Chart"))
        self.BarGraphBtn.setText(_translate("MainWindow", "Bar Graph"))
        self.yearcombobox_2.setItemText(0, _translate("MainWindow", "Compare Activity Types"))
        self.yearcombobox_2.setItemText(1, _translate("MainWindow", "Compare Years"))
        self.yearcombobox_2.setItemText(2, _translate("MainWindow", "Compare Months"))
        self.yearlabel_2.setText(_translate("MainWindow", "Pie Chart Settings:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
