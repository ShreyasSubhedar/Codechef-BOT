# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codebot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# 
# WARNING! All changes made in this file will be lost!

import bs4 as bs
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout


class Ui_Codechef(object):
    def setupUi(self, Codechef):
        Codechef.setObjectName("Codechef")
        Codechef.resize(649, 436)
        Codechef.setMaximumSize(QtCore.QSize(649, 436))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Codechef.setFont(font)
        Codechef.setStyleSheet("  background-color: rgb(1,1,1)\n"
                               "")
        Codechef.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(Codechef)
        self.centralwidget.setStyleSheet("background color:blue")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 50, 551, 361))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("  background-color:rgb(76, 175, 80)\n"
                                       "\n"
                                       "")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 10, 81, 31))
        self.pushButton.setStyleSheet(" \n"
                                      "  font-size: 15px;\n"
                                      "  text-align: center;\n"
                                      "  cursor: pointer;\n"
                                      "  outline: none;\n"
                                      "  color: #fff;\n"
                                      "  background-color: #4CAF50;\n"
                                      "  border: none;\n"
                                      "  border-radius: 15px;\n"
                                      "  box-shadow: 0 9px #999;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("  background-color: rgb(0,0,0);\n"
                                    "color: white;")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("  background-color: rgb(0, 0, 0);\n"
                                 "color:white;")
        self.label.setObjectName("label")
        Codechef.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Codechef)
        self.statusbar.setObjectName("statusbar")
        Codechef.setStatusBar(self.statusbar)

        self.retranslateUi(Codechef)
        QtCore.QMetaObject.connectSlotsByName(Codechef)

    def retranslateUi(self, Codechef):
        _translate = QtCore.QCoreApplication.translate
        Codechef.setWindowTitle(_translate("Codechef", "Codechef Bot"))
        Codechef.setWindowIcon(QtGui.QIcon("spider.png"))
        self.tableWidget.setSortingEnabled(False)
        self.pushButton.setText(_translate("Codechef", "Search"))
        self.lineEdit.setPlaceholderText(_translate("Codechef", "Codechef Username...."))
        self.label.setText(_translate("Codechef", "Codechef Bot"))

# Main Code start

def wrapper():
        q = ui.lineEdit.text()
        if(q==''):
            ui.lineEdit.setPlaceholderText( "Codechef Username....")
        else:
            try:
                from selenium import webdriver                                        # Importing selenium testing library
                from selenium.webdriver.chrome.options import Options                 # Importing options 
                # Creating Option object
                options = Options()
                # Making all calls with headless browser
                options.add_argument("--headless")
                browser = webdriver.Chrome(options=options)
                # Fetching HTML DOM for the given URL
                browser.get("https://www.codechef.com/users/" + q)
                # Calling BeautifulSoup Object for the given source page. 
                # BeautifulSoup('HTML/XML DOM page_course', 'option fo the same')
                soup = bs.BeautifulSoup(browser.page_source, 'html.parser')
                table = soup.find('table', class_='dataTable')                       # Finding table tag as all the information is present in table.
                rows = table.findAll('tr')                                           # Inside table finding all the rows.
                data = ['|'.join([td.findNext(text=True) for td in tr.findAll("td")]) for tr in rows]
                s = ''
                row = 0
                for i in data:
                    x = i.split('|')
                    if (len(x) == 4):
                        col = 0
                        for str in x:
                            ui.tableWidget.setItem(row, col, QTableWidgetItem(str))  # Connecting data object to the GUI. 
                            col += 1
                        row += 1

                browser.close()
            except Exception as e:
                ui.lineEdit.setText('')
                ui.lineEdit.setPlaceholderText("Codechef Username....")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Codechef = QtWidgets.QMainWindow()
    ui = Ui_Codechef()
    ui.setupUi(Codechef)
    Codechef.show()
    ui.pushButton.clicked.connect(wrapper)
    sys.exit(app.exec_())
