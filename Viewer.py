from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LDPlayerViewer(object):
    def setupUi(self, LDPlayerViewer):
        LDPlayerViewer.setObjectName("LDPlayerViewer")
        LDPlayerViewer.setWindowIcon(QtGui.QIcon('ldicon.ico'))
        LDPlayerViewer.resize(1255, 600)
        LDPlayerViewer.setMinimumSize(QtCore.QSize(1255, 0))
        LDPlayerViewer.setMaximumSize(QtCore.QSize(1255, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(LDPlayerViewer)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(LDPlayerViewer)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 5018))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1197, 10000))
        self.frame.setMaximumSize(QtCore.QSize(1197, 10000))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hwnd = {}
        index = index1 = 0
        index2 = 1
        for i in range(200):
            if i == 5*index2:
                index = 0
                index1 += 1
                index2 += 1
            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(240*index, 390*index1, 235, 385))
            self.label.setMinimumSize(QtCore.QSize(235, 385))
            self.label.setMaximumSize(QtCore.QSize(235, 385))
            # self.label.setStyleSheet("background-color: rgb(85, 255, 0);")
            self.hwnd[i] = int(self.label.winId())
            index += 1
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.retranslateUi(LDPlayerViewer)
        QtCore.QMetaObject.connectSlotsByName(LDPlayerViewer)
    def retranslateUi(self, LDPlayerViewer):
        _translate = QtCore.QCoreApplication.translate
        LDPlayerViewer.setWindowTitle(_translate("LDPlayerViewer", "LDPlayerViewer"))

