from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel


class Pic(QtWidgets.QWidget):
    def __init__(self, pos, path, size,  parent=None):
        super().__init__(parent)
        self.pos = pos

        self.acceptDrops()

        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap(path)
        self.scaled_pixmap = self.pixmap.scaled(*size)
        # adding image to label
        self.label.setPixmap(self.scaled_pixmap)
        self.label.setGeometry(QtCore.QRect(*self.pos))

        # Optional, resize label to image size
        # self.label.resize(self.pixmap.width(),
        #                   self.pixmap.height())

