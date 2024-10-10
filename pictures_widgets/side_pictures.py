from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel


class Pic(QtWidgets.QWidget):
    def __init__(self, path, PicturesCoordinates, PicturesSize, screen_width, screen_height, parent=None):
        super().__init__(parent)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pos = (int(PicturesCoordinates[0] * self.screen_width),
               int(PicturesCoordinates[1] * self.screen_height),
               int(PicturesSize[0] * self.screen_width),
               int(PicturesSize[1] * self.screen_height),
               )
        self.picSize = (int(PicturesSize[0] * self.screen_width),
                   int(PicturesSize[1] * self.screen_height))

        self.acceptDrops()

        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap(path)
        self.scaled_pixmap = self.pixmap.scaled(*self.picSize)
        # adding image to label
        self.label.setPixmap(self.scaled_pixmap)
        self.label.setGeometry(QtCore.QRect(*self.pos))

        # Optional, resize label to image size
        # self.label.resize(self.pixmap.width(),
        #                   self.pixmap.height())

