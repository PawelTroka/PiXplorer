#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ntpath
import os


class ImagesManager(object):
    """description of class"""
    def __init__(self):
        self.__currentDirectory=""
        self.__currentImageIndex = 0
        self.__imageFileNames = []
        self.allowedExtensions = [".png", ".jpg" ,".jpeg" ".tiff" ,".tif", ".bmp"]

    def Next(self):
        if len(self.__imageFileNames) > 0:
            self.__currentImageIndex = (self.__currentImageIndex + 1)% len(self.__imageFileNames)

    def Prev(self):
        if len(self.__imageFileNames) > 0:
            self.__currentImageIndex = (self.__currentImageIndex - 1)%len(self.__imageFileNames)


    def __setImageListFromCurrentDirectory__(self):
        self.__imageFileNames = []
        for file in os.listdir(self.__currentDirectory):
            if file.lower().endswith(tuple(self.allowedExtensions)):
                self.__imageFileNames.append(file)


    def setFilePath(self, filePath):
        self.__currentDirectory = os.path.dirname(filePath)
        fileName = ntpath.basename(filePath)
        self.__setImageListFromCurrentDirectory__()
        self.__currentImageIndex = self.__imageFileNames.index(fileName)


    def getCurrentImagePath(self):
        if len(self.__imageFileNames) > 0:
            return os.path.join(self.__currentDirectory,self.__imageFileNames[self.__currentImageIndex])
        else:
            return None