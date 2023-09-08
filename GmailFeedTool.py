from PyQt5 import QtCore, QtGui, QtWidgets
from GmailSelenium import GmailSelenium
import os, time, subprocess
import pathlib
class GmailTool(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 1061, 61))
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setObjectName("groupBox_2")
        self.sell_token_address = QtWidgets.QLineEdit(self.groupBox_2)
        self.sell_token_address.setGeometry(QtCore.QRect(90, 20, 231, 20))
        self.sell_token_address.setObjectName("sell_token_address")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(370, 20, 71, 21))
        self.label_15.setObjectName("label_15")
        self.threadCount = QtWidgets.QSpinBox(self.groupBox_2)
        self.threadCount.setGeometry(QtCore.QRect(430, 20, 42, 22))
        self.threadCount.setProperty("value", 2)
        self.threadCount.setObjectName("threadCount")
        self.tab_data = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_data.setGeometry(QtCore.QRect(10, 110, 1081, 621))
        self.tab_data.setObjectName("tab_data")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_email_2 = QtWidgets.QTableWidget(self.tab)
        self.table_email_2.setGeometry(QtCore.QRect(10, 10, 511, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_email_2.sizePolicy().hasHeightForWidth())
        self.table_email_2.setSizePolicy(sizePolicy)
        self.table_email_2.setMinimumSize(QtCore.QSize(0, 1))
        self.table_email_2.setMaximumSize(QtCore.QSize(1025, 16777215))
        self.table_email_2.setMouseTracking(False)
        self.table_email_2.setTabletTracking(False)
        self.table_email_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_email_2.setLineWidth(1)
        self.table_email_2.setAutoScrollMargin(16)
        self.table_email_2.setDragEnabled(False)
        self.table_email_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_email_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_email_2.setShowGrid(True)
        self.table_email_2.setObjectName("table_email_2")
        self.table_email_2.setColumnCount(3)
        self.table_email_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_email_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email_2.setHorizontalHeaderItem(2, item)
        self.table_email_2.horizontalHeader().setDefaultSectionSize(170)
        self.table_email_2.verticalHeader().setStretchLastSection(True)
        self.table_content_3 = QtWidgets.QTableWidget(self.tab)
        self.table_content_3.setGeometry(QtCore.QRect(530, 10, 531, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_content_3.sizePolicy().hasHeightForWidth())
        self.table_content_3.setSizePolicy(sizePolicy)
        self.table_content_3.setMinimumSize(QtCore.QSize(0, 1))
        self.table_content_3.setMaximumSize(QtCore.QSize(1025, 16777215))
        self.table_content_3.setMouseTracking(False)
        self.table_content_3.setTabletTracking(False)
        self.table_content_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_content_3.setLineWidth(1)
        self.table_content_3.setAutoScrollMargin(16)
        self.table_content_3.setDragEnabled(False)
        self.table_content_3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_content_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_content_3.setShowGrid(True)
        self.table_content_3.setObjectName("table_content_3")
        self.table_content_3.setColumnCount(3)
        self.table_content_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_content_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_content_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_content_3.setHorizontalHeaderItem(2, item)
        self.table_content_3.horizontalHeader().setDefaultSectionSize(170)
        self.table_content_3.verticalHeader().setStretchLastSection(True)
        self.tab_data.addTab(self.tab, "")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(70, 70, 51, 31))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_start_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_3.setGeometry(QtCore.QRect(10, 70, 51, 31))
        self.btn_start_3.setObjectName("btn_start_3")
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(130, 70, 51, 31))
        self.btn_check.setObjectName("btn_check")
        self.show_transactions_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_transactions_2.setGeometry(QtCore.QRect(200, 80, 151, 17))
        self.show_transactions_2.setChecked(True)
        self.show_transactions_2.setObjectName("show_transactions_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_data.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Options"))
        self.label_14.setText(_translate("MainWindow", "Nhập mail"))
        self.label_15.setText(_translate("MainWindow", "Số luồng"))
        item = self.table_email_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_email_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_email_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table_content_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_content_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From"))
        item = self.table_content_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Content"))
        self.tab_data.setTabText(self.tab_data.indexOf(self.tab), _translate("MainWindow", "Mail tab"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_start_3.setText(_translate("MainWindow", "Start"))
        self.btn_check.setText(_translate("MainWindow", "Check"))
        self.show_transactions_2.setText(_translate("MainWindow", " Tất cả các mail"))
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        self.listAccountRunning = []
        self.list_hostmail = []
        self.runCount = 0
        self.index = 0
        self.LoadHotMail()
        self.btn_start_3.clicked.connect(self.StartReg)
    def closeEvent(self, event):
        sys.exit()
    
    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()
                
    def LoadHotMail(self):
        if os.path.exists("hotmail.txt"): 
            accountFile = open("hotmail.txt", 'r')
            if (accountFile): 
                for mail in accountFile.readlines():
                    if len(mail.split("|")) == 2:
                        self.list_hostmail.append(mail)
                self.showAccounts()
                
    def showAccounts(self):
        self.table_email_2.clear()
        self.table_email_2.setRowCount(0)
        i = 0
        for account in self.list_hostmail:
            self.table_email_2.insertRow(i)
            self.ShowTable(i, 0, account.split("|")[0])
            self.ShowTable(i, 1, account.split("|")[1])
            i += 1                

    def LDViewer(self):
        from Viewer import Ui_LDPlayerViewer
        global LDPlayerViewer
        LDPlayerViewer = QtWidgets.QWidget()
        self.view = Ui_LDPlayerViewer()
        self.view.setupUi(LDPlayerViewer)
        LDPlayerViewer.show()
        
    def Delay(self, countdelay):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(countdelay*1000), loop.quit)
        loop.exec()

    def ShowTable(self, row, column, text):
        self.table_email_2.setItem(row, column, QtWidgets.QTableWidgetItem(text))
        
    def ChangeTextSuccessAndError(self, check, row, mail, password):
        time.sleep(5)
        # if check:
        #     self.success.setText(f"<p><span style=\" color:#00aa00;\">Success: {self.indexsuccess}</span></p>")
        # else:
        #     self.error.setText(f"<p><span style=\" color:#ff0000;\">Error: {self.indexerror}</span></p>")
        
        self.runCount -= 1
        self.StartReg()
            
    def StartReg(self):
        if self.btn_start_3.text() == "Start":
            print('self.index', self.index)
            if len(self.list_hostmail) > self.index:
                for vm in self.list_hostmail:
                    if self.runCount < int(self.threadCount.text())  and len(self.list_hostmail) > self.index:
                        mailInfo = self.list_hostmail[self.index]
                        self.threadreg = StartQ(self, self.index, mailInfo.split("|")[0], mailInfo.split("|")[1])
                        self.threadreg.start()
                        self.threadreg.show.connect(self.ShowTable)
                        self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                        self.listthread.append(self.threadreg)
                        self.index += 1
                        self.runCount += 1
                        time.sleep(1)
                        print('self', self.index, self.runCount)
              
        else:
            for thread in self.listthread: thread.Stop()
            self.btn_start_3.setText('Start')


class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str, str)
    def __init__(self, ref, index, mail, password) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.mail = mail
        self.password = password

    def run(self):
        self.reg = GmailSelenium(self.index, self.mail, self.password)
        self.reg.ref = self
        self.reg.run()
        time.sleep(0.1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RegTikTok = QtWidgets.QMainWindow()
    RegTikTok.setWindowIcon(QtGui.QIcon('icon.ico'))
    ui = GmailTool()
    ui.setupUi(RegTikTok)
    RegTikTok.show()
    sys.exit(app.exec_())
# 7h15