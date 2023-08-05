from PyQt5 import QtCore, QtGui, QtWidgets
from facebookSelenium import FacebookSelenium
import os, time, subprocess
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 781, 321))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setGeometry(QtCore.QRect(110, 10, 101, 21))
        self.success.setObjectName("success")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.error.setObjectName("error")
        self.counthotmail = QtWidgets.QLabel(self.centralwidget)
        self.counthotmail.setGeometry(QtCore.QRect(320, 10, 101, 21))
        self.counthotmail.setObjectName("counthotmail")
        RegTikTok.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegTikTok)
        QtCore.QMetaObject.connectSlotsByName(RegTikTok)

    def retranslateUi(self, RegTikTok):
        _translate = QtCore.QCoreApplication.translate
        RegTikTok.setWindowTitle(_translate("Facebook", "Facebook Facebook"))
        self.startreg.setText(_translate("Facebook", "Start"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RegTikTok", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RegTikTok", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RegTikTok", "Hotmail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RegTikTok", "Status"))
        self.success.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Success: 0</span></p>"))
        self.error.setText(_translate("RegTikTok", "<p><span style=\" color:#ff0000;\">Error: 0</span></p>"))
        self.counthotmail.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Hotmail: 0</span></p>"))
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []

        self.startreg.clicked.connect(self.StartReg)
    def closeEvent(self, event):
        sys.exit()
    
    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()
        
  
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
    def ChangeTextSuccessAndError(self, check, mail):
        if check:
            self.indexsuccess += 1
            self.success.setText(f"<p><span style=\" color:#00aa00;\">Success: {self.indexsuccess}</span></p>")
        else:
            self.indexerror += 1
            self.error.setText(f"<p><span style=\" color:#ff0000;\">Error: {self.indexerror}</span></p>")
            
    def StartReg(self):
        if self.startreg.text() == "Start":
            index = 0
            self.listmail = [{'mail': 'quytest@gmail.com', 'password': 'dqwdqwdwq'}]
            self.startreg.setText("Stop")
            for vm in self.listmail:
                self.threadreg = StartQ(self, index, vm['mail'], vm['password'])
                self.threadreg.start()
                self.threadreg.show.connect(self.ShowTable)
                # self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                self.listthread.append(self.threadreg)
                index += 1
                # index2 += 1
                self.Delay(0.01)
        else:
            for thread in self.listthread: thread.Stop()
            self.startreg.setText('Start')
class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, str)
    def __init__(self, ref, index, mail, password) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.mail = mail
        self.password = password
    def Stop(self):
        try:
            self.reg.Stop()
        except: pass
        self.terminate()
    def run(self):
        row = self.ref.tableWidget.rowCount()
        self.ref.tableWidget.insertRow(row)
        self.reg = FacebookSelenium(self.index, self.mail, self.password, row)
        self.reg.ref = self
        self.reg.run()
        time.sleep(10)

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