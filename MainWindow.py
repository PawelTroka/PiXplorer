# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(615, 543)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuWidok = QtGui.QMenu(self.menubar)
        self.menuWidok.setObjectName(_fromUtf8("menuWidok"))
        self.menuProgram = QtGui.QMenu(self.menubar)
        self.menuProgram.setObjectName(_fromUtf8("menuProgram"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOtw_rz = QtGui.QAction(MainWindow)
        self.actionOtw_rz.setObjectName(_fromUtf8("actionOtw_rz"))
        self.actionZamknij = QtGui.QAction(MainWindow)
        self.actionZamknij.setObjectName(_fromUtf8("actionZamknij"))
        self.actionPe_en_ekran = QtGui.QAction(MainWindow)
        self.actionPe_en_ekran.setCheckable(True)
        self.actionPe_en_ekran.setObjectName(_fromUtf8("actionPe_en_ekran"))
        self.actionInformacje = QtGui.QAction(MainWindow)
        self.actionInformacje.setObjectName(_fromUtf8("actionInformacje"))
        self.menuPlik.addAction(self.actionOtw_rz)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionZamknij)
        self.menuWidok.addAction(self.actionPe_en_ekran)
        self.menuProgram.addAction(self.actionInformacje)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuWidok.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionZamknij, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PiXplorer", None))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik", None))
        self.menuWidok.setTitle(_translate("MainWindow", "Widok", None))
        self.menuProgram.setTitle(_translate("MainWindow", "O programie", None))
        self.actionOtw_rz.setText(_translate("MainWindow", "Otwórz", None))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij", None))
        self.actionZamknij.setShortcut(_translate("MainWindow", "Esc", None))
        self.actionPe_en_ekran.setText(_translate("MainWindow", "Pełen ekran", None))
        self.actionPe_en_ekran.setShortcut(_translate("MainWindow", "Return", None))
        self.actionInformacje.setText(_translate("MainWindow", "Informacje", None))

