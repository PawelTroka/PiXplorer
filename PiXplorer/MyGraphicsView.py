#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.Qt import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ImagesManager

class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super(MyGraphicsView, self).__init__()
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self._isPanning = False
        self._mousePressed = False
        self.__imageManager = ImagesManager.ImagesManager()
        #self.setBackgroundBrush(QBrush(Qt.black))
        self.isFullScreen = False

    def setImage(self,imagePath):
        self.__imageManager.setFilePath(imagePath)
        self.showImage()

    def showImage(self):
        qpixmap = QPixmap(self.__imageManager.getCurrentImagePath())
        if qpixmap:
            self.resetMatrix()
            scene = QGraphicsScene()
            graphicsPixmapItem = QGraphicsPixmapItem(qpixmap)
            scene.addItem(graphicsPixmapItem)
            self.setScene(scene)
            if self.isFullScreen:
                if self.width() < qpixmap.width() or self.height() < qpixmap.height():#self.sceneRect().contains(qpixmap.width(),qpixmap.height()):#
                    self.fitInView(self.sceneRect(),Qt.KeepAspectRatio)

    def mousePressEvent(self,  event):
        if event.button() == Qt.LeftButton:
            self._mousePressed = True
            if self._isPanning:
                self.setCursor(Qt.ClosedHandCursor)
                self._dragPos = event.pos()
                event.accept()
            else:
                super(MyGraphicsView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._mousePressed and self._isPanning:
            newPos = event.pos()
            diff = newPos - self._dragPos
            self._dragPos = newPos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diff.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diff.y())
            event.accept()
        else:
            super(MyGraphicsView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.modifiers() & Qt.ControlModifier:
                self.setCursor(Qt.OpenHandCursor)
            else:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
            self._mousePressed = False
        super(MyGraphicsView, self).mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event): pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control and not self._mousePressed:
            self._isPanning = True
            self.setCursor(Qt.OpenHandCursor)

        elif event.key() == Qt.Key_Plus and not self.isFullScreen:
            factor = 1.2;
            self.scale(factor, factor)
        elif event.key() == Qt.Key_Minus and not self.isFullScreen:
            factor = 1.2;
            factor = 1.0 / factor
            self.scale(factor, factor)
        elif event.key() == Qt.Key_Right and self.isFullScreen:
            self.__imageManager.Next()
            self.showImage()
        elif event.key() == Qt.Key_Left and self.isFullScreen:
            self.__imageManager.Prev()
            self.showImage()
        else:
            super(MyGraphicsView, self).keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            if not self._mousePressed:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
        else:
            super(MyGraphicsView, self).keyPressEvent(event)


    #def wheelEvent(self,  event):
    #    factor = 1.2;
    #    if event.delta() < 0:
    #        factor = 1.0 / factor
    #    self.scale(factor, factor)


