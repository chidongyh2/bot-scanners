from PyQt5 import QtCore, QtGui, QtWidgets
from facebookSelenium import FacebookSelenium
import os, time, subprocess
import pathlib
class FacebookTool(object):
    def setupUi(self, RegTikTok):
        RegTikTok.setObjectName("Facebook change info")
        RegTikTok.resize(806, 446)
        RegTikTok.setMaximumSize(QtCore.QSize(806, 446))
        RegTikTok.closeEvent = lambda event:self.closeEvent(event)
        self.centralwidget = QtWidgets.QWidget(RegTikTok)
        self.centralwidget.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n""")
        self.centralwidget.setObjectName("centralwidget")
        self.startreg = QtWidgets.QPushButton(self.centralwidget)
        self.startreg.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.startreg.setObjectName("startreg")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 781, 351))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.totalFile = QtWidgets.QLabel(self.centralwidget)
        self.totalFile.setGeometry(QtCore.QRect(100, 10, 101, 21))
        self.totalFile.setObjectName("totalFile")
        
        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setGeometry(QtCore.QRect(150, 10, 101, 21))
        self.success.setObjectName("success")
        
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(250, 10, 91, 21))
        self.error.setObjectName("error")
        
        self.counthotmail = QtWidgets.QLabel(self.centralwidget)
        self.counthotmail.setGeometry(QtCore.QRect(320, 10, 101, 21))
        self.counthotmail.setObjectName("counthotmail")
        
        self.maxOpenLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxOpenLabel.setGeometry(QtCore.QRect(420, 10, 150, 21))
        self.maxOpenLabel.setObjectName("maxOpenLabel")
        self.maxOpen = QtWidgets.QSpinBox(self.centralwidget)
        self.maxOpen.setGeometry(QtCore.QRect(550, 10, 101, 21))
        self.maxOpen.setMinimum(0)
        self.maxOpen.setMaximum(1000)
        self.maxOpen.setProperty("value", 2)
        self.maxOpen.setObjectName("Số lượng thực hiện")
        
        RegTikTok.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegTikTok)
        QtCore.QMetaObject.connectSlotsByName(RegTikTok)

    def retranslateUi(self, RegTikTok):
        _translate = QtCore.QCoreApplication.translate
        RegTikTok.setWindowTitle(_translate("Facebook", "Facebook Facebook"))
        self.startreg.setText(_translate("Facebook", "Start"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RegTikTok", "FolderName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RegTikTok", "OldEmail"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RegTikTok", "NewEmail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RegTikTok", "NewPassWord"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("RegTikTok", "Status"))
        self.success.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Success: 0</span></p>"))
        self.error.setText(_translate("RegTikTok", "<p><span style=\" color:#ff0000;\">Error: 0</span></p>"))
        self.counthotmail.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Hotmail: 0</span></p>"))
        self.maxOpenLabel.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Số lượng thực hiện:</span></p>"))
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        self.listAccounts = []
        self.listAccountRunning = []
        self.list_hostmail = []
        self.runCount = 0
        self.index = 0
        self.startreg.clicked.connect(self.StartReg)
        self.LoadData()
        self.LoadHotMail()
    def closeEvent(self, event):
        sys.exit()
    
    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()

    def LoadData(self):        
        data = pathlib.Path('accounts')
        index = 0
        for item in data.iterdir():
            if item.is_dir():
                self.listAccounts.append(str(item).replace("accounts\\", ''))
                self.listAccountRunning.append(str(item).replace("accounts\\", ''))
                # self.tableWidget.insertRow(index)
                # self.ShowTable(index, 0, str(item).replace("accounts\\", ''))
                index += 1
        self.totalFile.setText(str(len(self.listAccounts)))
                
    def LoadHotMail(self):
        if os.path.exists("hotmail.txt"): 
            accountFile = open("hotmail.txt", 'r')
            if (accountFile): 
                for mail in accountFile.readlines():
                    if len(mail.split("|")) == 2:
                        self.list_hostmail.append(mail)
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
        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(text))
        
    def ChangeTextSuccessAndError(self, check, row, folderName, oldMail, mail, password):
        print('dzo check success')
        self.ShowTable(row, 0, folderName)
        self.ShowTable(row, 1, oldMail)
        self.ShowTable(row, 2, oldMail)
        self.ShowTable(row, 3, password)
        time.sleep(1)
        if check:
            self.indexsuccess += 1
            self.success.setText(f"<p><span style=\" color:#00aa00;\">Success: {self.indexsuccess}</span></p>")
            open("hotmail.txt", "w").close()    
            with open("hotmail.txt", 'w') as filedata:
                    for mail in self.list_hostmail:
                        filedata.write(f"{str(mail).strip()}|False\n") 
        else:
            self.indexerror += 1
            self.error.setText(f"<p><span style=\" color:#ff0000;\">Error: {self.indexerror}</span></p>")

                   
        self.runCount -= 1
        self.StartReg()
            
    def StartReg(self):
        if self.startreg.text() == "Start":
            removeIndex = 0
            for vm in self.listAccounts:
                if removeIndex == self.index and self.runCount < int(self.maxOpen.text()) and len(self.list_hostmail) > self.index:
                    mailInfo = self.list_hostmail[self.index]
                    self.threadreg = StartQ(self, self.index, vm, mailInfo.split("|")[0], mailInfo.split("|")[1])
                    self.threadreg.start()
                    self.threadreg.show.connect(self.ShowTable)
                    self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                    self.listthread.append(self.threadreg)
                    #self.listAccountRunning.pop(removeIndex)
                    self.index += 1
                    # index2 += 1
                    self.runCount += 1
                    #self.Delay(3)
                removeIndex += 1
        else:
            for thread in self.listthread: thread.Stop()
            self.startreg.setText('Start')
class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str, str, str, str)
    def __init__(self, ref, index, folderName, mail, password) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.mail = mail
        self.password = password
        self.folderName = folderName
    # def Stop(self):
    #     try:
    #         self.reg.Stop()
    #     except: pass
    #     self.terminate()
    def run(self):
        row = self.ref.tableWidget.rowCount()
        self.ref.tableWidget.insertRow(row)
        self.reg = FacebookSelenium(self.index, self.folderName, self.mail, self.password, row)
        self.reg.ref = self
        self.reg.run()
        time.sleep(3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RegTikTok = QtWidgets.QMainWindow()
    RegTikTok.setWindowIcon(QtGui.QIcon('icon.ico'))
    ui = FacebookTool()
    ui.setupUi(RegTikTok)
    RegTikTok.show()
    sys.exit(app.exec_())
# 7h15