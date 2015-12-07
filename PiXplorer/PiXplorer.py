#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import expanduser
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.Qt import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtMultimedia import *
from PyQt4.QtOpenGL import *
from sys import argv
import ntpath
import os
import MyGraphicsView
import HelpDialog

class MainWindow(QMainWindow):
    def __init__( self ):
        super( QMainWindow,self ).__init__()
        self.resize(615, 543)
        self.centralwidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.graphicsView = MyGraphicsView.MyGraphicsView()
        self.verticalLayout.addWidget(self.graphicsView)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuProgram = QtGui.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(self)
        self.actionOpen.triggered.connect( self.openFile )
        self.actionClose = QtGui.QAction(self)
        self.actionFullScreen = QtGui.QAction(self)
        self.actionFullScreen.setCheckable(True)
        self.actionFullScreen.triggered.connect(self.enterFullScreen)
        self.actionInformacje = QtGui.QAction(self)
        self.actionInformacje.triggered.connect(self.aboutApp)

        self.actionPomoc = QtGui.QAction(self)
        self.actionPomoc.triggered.connect((HelpDialog.HelpDialog(self)).show)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionFullScreen)
        self.menuProgram.addAction(self.actionInformacje)
        self.menuProgram.addAction(self.actionPomoc)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())

        self.setNames()
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def aboutApp(self):
        QMessageBox.about(self,"O programie","PiXplorer ®\nPaweł Troka © 2015\nJęzyki skryptowe i ich zastosowania")

    def setNames(self):
        self.setWindowTitle("PiXplorer")
        self.menuFile.setTitle("Plik")
        self.menuView.setTitle("Widok")
        self.menuProgram.setTitle("O programie")
        self.actionOpen.setText("Otwórz")
        self.actionClose.setText("Zamknij")
        self.actionClose.setShortcut("Esc")
        self.actionFullScreen.setText("Pełny ekran")
        self.actionFullScreen.setShortcut("Return")
        self.actionInformacje.setText("Informacje")
        self.actionPomoc.setText("Pomoc...")

    def enterFullScreen(self):
        if self.actionFullScreen.isChecked():
            self.showFullScreen()
            self.graphicsView.isFullScreen=True
            self.graphicsView.showImage()
        else:
            self.showNormal()
            self.graphicsView.isFullScreen=False
            self.graphicsView.showImage()

    def openFile(self):
        filePath = QFileDialog.getOpenFileName(self,"Wybierz obrazek",expanduser( "~" ), "Pliki graficzne (*.png *.jpg *.jpeg *.tiff *.tif *.bmp)")
        if filePath:
             self.graphicsView.setImage(filePath)

# treść programu, m.in. definicja głównego okna

app = QtGui.QApplication( argv )
# utworzenie i wyświetlenie głównego okna
mainWindow = MainWindow()
mainWindow.show()
# uruchomienie aplikacji
app.exec_()