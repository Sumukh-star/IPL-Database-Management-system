# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selected.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as s

conn=s.connect('minidatabase.db')
cur=conn.cursor()


class Ui_Form(object):
    def loadData(self):
            query="SELECT * FROM SELECTED_FOR"
        
            result=conn.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number,row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

            conn.close()
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.loadData)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Selected_for"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cap_no"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Player_Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Team1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Team2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Position"))
        self.pushButton.setText(_translate("Form", "load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
