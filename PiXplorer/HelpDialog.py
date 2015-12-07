#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.Qt import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HelpDialog(QDialog):
    def __init__( self,owner ):
        super( QDialog,self ).__init__(owner)
        self.resize(730, 600)
        self.setMinimumSize(730, 600)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.tabWidget = QtGui.QTabWidget(self)
        self.tab = QtGui.QWidget()
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setReadOnly(True)
        self.horizontalLayout.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab, "Otwieranie plików")
        self.tab_2 = QtGui.QWidget()
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_2, "Tryb pełnoekranowy")
        self.tab_3 = QtGui.QWidget()
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_3)
        self.textEdit_3 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_3.setReadOnly(True)
        self.horizontalLayout_3.addWidget(self.textEdit_3)
        self.tabWidget.addTab(self.tab_3, "Nawigacja")
        self.verticalLayout.addWidget(self.tabWidget)

        self.setNames()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def setNames(self):
        self.setWindowTitle("Pomoc")
        self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p1, li { white-space: pre-wrap; }</style></head>"
"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
"<span style=\" font-size:14pt;\">"
"<h1>Otwieranie plików - krok po kroku</h1>"
"W niniejszej części pomocy zajmiemy się otwieraniem plików graficznych w programie PiXplorer. Proces ten jest banalnie prosty, a pozwala nam zarówno na wczytanie pojedynczego pliku graficznego, jak i późniejsze przeglądanie wszystkich plików graficznych z katalogu. Mechanizm ten jest wzorowany na programie IrfanView."
"<h2>Krok 1</h2>"
"<br />Wybierz z górnego menu opcję Plik - Otwórz"
"<br /><img src=\"help/open1.jpg\" /><br />"
"<h2>Krok 2</h2>"
"<br />Po ukazaniu się okna dialogowego z możliwością wyboru pliku graficznego nawiguj do porządanej lokalizacji, gdzie znajduje się plik, który chcesz otworzyć."
"<br /><img src=\"help/open2.jpg\" /><br />"
"<h2>Krok 3</h2>"
"<br />Po wybraniu pliku graficznego przyciskiem Otwórz w poprzednim kroku, naszym oczom ukazuje się otwarta grafika. Teraz możemy przeglądać ją w naturalnej skali 1:1 po prostu używając pasków (scrolli) znajdujących się w prawej i dolnej częsci ekranu"
"<br /><img src=\"help/open3.jpg\" /><br />"
"<br />Żeby nawigować po innych plikach w katalogu, należy włączyć tryb pełnoekranowy, co jest opisane w dalszej częsci pomocy."
"</span></p></body></html>")


        self.textEdit_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p1, li { white-space: pre-wrap; }</style></head>"
"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
"<span style=\" font-size:14pt;\">"
"<h1>Tryb pełnoekranowy - krok po kroku</h1>"
"Poniżej przedstawiono krok po kroku, jak należy postępować, aby uzyskać tryb pełnoekranowy w programie PiXplorer. Generalnie jest to banalnie proste i sprowadza się do wybrania obrazka i naciśnięcia przycisku enter na klawiaturze."
"<br />Alternatywnie można wybrać tą opcję z górnego menu Widok - Pełny Ekran. Nie musimy też wczytywać obrazka, można zrobić to po wejściu w tryb pełnoekranowy, wybierając opcję z (nadal widocznego) górnego menu"
"<h2>Krok 1</h2>"
"<br />Wybierz z górnego menu opcję Widok - Pełen ekran (alternatywnie skrót klawiszowy Enter może przyśpieszyć ten proces). Obrazek możesz wczytać wcześniej zgodnie z częścią instrukcji temu poświęconej lub później korzystając z odpowiedniej opcji górnego menu."
"<br /><img src=\"help/fullscreen1.jpg\" /><br />"
"<h2>Krok 2</h2>"
"<br />Po wybraniu opcji Widok - Pełen Ekran naszym oczom ukaże się aplikacja w trybie pełnoekranowym, wykorzystująca całą dostępną na ekranie przestrzeń. Jeżeli wczytaliśmy lub wczytamy obrazek, to zostanie on przeskalowany tak, aby się zmieścił na ekranie w całości (oczywiście z zachowaniem proporcji i oczywiście skalowanie działa tylko w dół - pomniejszanie)"
"<br /><img src=\"help/fullscreen2.jpg\" /><br />"
"<br />Aby wyjść z trybu pełnoekranowego należy wybrać ponownie opcję Wdok Tryb Pełnoekranowy lub po prostu nacisnąć Enter."
"</span></p></body></html>")


        self.textEdit_3.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p1, li { white-space: pre-wrap; }</style></head>"
"<body style=\" font-family:\'Verdana\'; font-size:8.25pt; font-weight:400; font-style:normal;\">"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
"<span style=\" font-size:14pt;\">"
"<h1>Nawigacja po obrazach w katalogu - krok po kroku</h1>"
"Aby przeglądać kolejne pliki graficzne z danego katalogu należy najpierw wczytać dowolny plik graficzny z katalogu, który opisano już w innej części instrukcji jak i wejść w tryb pełnoekranowy (również opisane w innej części instrukcji)."
"<h2>Krok 1</h2>"
"<br />Zakładając, że wczytaliśmy już obrazek z porządanego katalogu i weszliśmy w tryb pełnoekranowy, żeby wyświetlić następny obrazek wybieramy strzałkę w prawo z klawiatury (→) (poprzedni obrazek - strzałka w lewo ←)"
"<br /><img src=\"help/navigation1.jpg\" /><br />"
"<h2>Krok 2</h2>"
"<br />Po kliknięciu w strzałkę w lewo lub w prawo na klawiaturze obrazek ulega zmianie na odpowiednio następny lub poprzedni z katalogu."
"<br /><img src=\"help/navigation2.jpg\" /><br />"
"<br />Jeżeli chcemy zmienić katalog, to po prostu jeszcze raz wczytujemy obrazek z porządanego katalogu."
"</span></p></body></html>")