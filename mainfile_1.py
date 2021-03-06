# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainfile_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from TEAMS import Ui_Dialog as teamsui
from BOARD_NAME import Ui_Form as board
from STADIUM_CAPACIT import Ui_Dialog as capa
from TEAM_STADIUM import Ui_Dialog as stad
from played_at import Ui_Form as play
from players import Ui_Form as players
from schedules import Ui_Form as sched
from selected import Ui_Form as select
from PLAYER_1 import Ui_Form as stat
from orange import Ui_Form as orange
from purple_1 import Ui_Form as purple
import sqlite3 as s

pconn=s.connect('minidatabase.db')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(100, 60, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/ss/A.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu_Bar = QtWidgets.QMenu(self.menubar)
        self.menuMenu_Bar.setObjectName("menuMenu_Bar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTEAMS = QtWidgets.QAction(MainWindow)
        self.actionTEAMS.setObjectName("actionTEAMS")
        self.actionPLAYERS = QtWidgets.QAction(MainWindow)
        self.actionPLAYERS.setObjectName("actionPLAYERS")
        self.actionSCHEDULES = QtWidgets.QAction(MainWindow)
        self.actionSCHEDULES.setObjectName("actionSCHEDULES")
        self.actionPLAYED_AT = QtWidgets.QAction(MainWindow)
        self.actionPLAYED_AT.setObjectName("actionPLAYED_AT")
        self.actionSELECTED_FOR = QtWidgets.QAction(MainWindow)
        self.actionSELECTED_FOR.setObjectName("actionSELECTED_FOR")
        self.actionSTADIUM_CAPACITY = QtWidgets.QAction(MainWindow)
        self.actionSTADIUM_CAPACITY.setObjectName("actionSTADIUM_CAPACITY")
        self.actionTEAM_STADIUM = QtWidgets.QAction(MainWindow)
        self.actionTEAM_STADIUM.setObjectName("actionTEAM_STADIUM")
        self.actionCRICKET_BOARDS = QtWidgets.QAction(MainWindow)
        self.actionCRICKET_BOARDS.setObjectName("actionCRICKET_BOARDS")
        self.actionPLAYER_STAT = QtWidgets.QAction(MainWindow)
        self.actionPLAYER_STAT.setObjectName("actionPLAYER_STAT")
        self.actionHIGHEST_RUN_GETTER = QtWidgets.QAction(MainWindow)
        self.actionHIGHEST_RUN_GETTER.setObjectName("actionHIGHEST_WICKET_GETTER")
        self.actionHIGHEST_WICKET_GETTER = QtWidgets.QAction(MainWindow)
        self.actionHIGHEST_WICKET_GETTER.setObjectName("actionHIGHEST_WICKET_GETTER")
        
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionTEAMS)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionPLAYERS)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionSCHEDULES)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionPLAYED_AT)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionSELECTED_FOR)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionSTADIUM_CAPACITY)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionTEAM_STADIUM)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionCRICKET_BOARDS)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionPLAYER_STAT)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionHIGHEST_RUN_GETTER)
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionHIGHEST_WICKET_GETTER)
        self.menuMenu_Bar.addSeparator()
        
        self.menubar.addAction(self.menuMenu_Bar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuMenu_Bar.triggered[QtWidgets.QAction].connect(self.actionSlot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu_Bar.setTitle(_translate("MainWindow", "Menu Bar"))
        self.actionTEAMS.setText(_translate("MainWindow", "TEAMS"))
        self.actionPLAYERS.setText(_translate("MainWindow", "PLAYERS"))
        self.actionSCHEDULES.setText(_translate("MainWindow", "SCHEDULES"))
        self.actionPLAYED_AT.setText(_translate("MainWindow", "PLAYED_AT"))
        self.actionSELECTED_FOR.setText(_translate("MainWindow", "SELECTED_FOR"))
        self.actionSTADIUM_CAPACITY.setText(_translate("MainWindow", "STADIUM_CAPACITY"))
        self.actionCRICKET_BOARDS.setText(_translate("MainWindow", "CRICKET_BOARDS"))
        self.actionPLAYER_STAT.setText(_translate("MainWindow", "PLAYER_STAT"))
        self.actionHIGHEST_RUN_GETTER.setText(_translate("MainWindow", "HIGHEST_RUN_GETTER"))
        self.actionHIGHEST_WICKET_GETTER.setText(_translate("MainWindow", "HIGHEST_WICKET_GETTER"))
        self.actionTEAM_STADIUM.setText(_translate("MainWindow", "TEAM_STADIUM"))


    def actionSlot(self,action):
        txt=action.text();
        if txt=="TEAMS":
            self.teamNameWindow=QtWidgets.QDialog()
            self.dialog=teamsui()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()
        elif txt=="PLAYERS":
            
            self.teamNameWindow1=QtWidgets.QWidget()
            self.aei=players()
            self.aei.setupUi(self.teamNameWindow1)
            self.teamNameWindow1.show()
        elif txt=="SCHEDULES":
            
            self.teamNameWindow1=QtWidgets.QWidget()
            self.aei=sched()
            self.aei.setupUi(self.teamNameWindow1)
            self.teamNameWindow1.show()

        elif txt=="PLAYED_AT":
            
            self.teamNameWindow1=QtWidgets.QWidget()
            self.aei=play()
            self.aei.setupUi(self.teamNameWindow1)
            self.teamNameWindow1.show()

        elif txt=="SELECTED_FOR":
            
            self.teamNameWindow1=QtWidgets.QWidget()
            self.aei=select()
            self.aei.setupUi(self.teamNameWindow1)
            self.teamNameWindow1.show()

        elif txt=="STADIUM_CAPACITY":
            self.teamNameWindow=QtWidgets.QDialog()
            self.dialog=capa()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()

        elif txt=="CRICKET_BOARDS":
            self.teamNameWindow1=QtWidgets.QWidget()
            self.aei=board()
            self.aei.setupUi(self.teamNameWindow1)
            self.teamNameWindow1.show()

        elif txt=="TEAM_STADIUM":
            self.teamNameWindow=QtWidgets.QDialog()
            self.dialog=stad()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()

        elif txt=="PLAYER_STAT":
            self.teamNameWindow=QtWidgets.QWidget()
            self.dialog=stat()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()
            
        elif txt=="HIGHEST_RUN_GETTER":
            self.teamNameWindow=QtWidgets.QWidget()
            self.dialog=orange()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()

        elif txt=="HIGHEST_WICKET_GETTER":
            self.teamNameWindow=QtWidgets.QWidget()
            self.dialog=purple()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()

            

       

            

        
        
            
        

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
