from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QLabel


class Circle():
    def __init__(self, center, radius, name, borderColor, fillColor, value, width, height):
        self.width = width
        self.height = height
        self.center = QPoint(int(center[0] * self.width), (int(center[1] * self.width)))
        self.radius = int(self.width* radius)
        self.name = name
        self.borderColor = borderColor
        self.fillColor = fillColor
        self.value = value
        self.labelValue = value

    def draw(self, painter):

        painter.setRenderHint(QPainter.Antialiasing)
        # Устанавливаем цвета для круга
        painter.setPen(QPen(self.borderColor, 2))
        painter.setBrush(self.fillColor)

        # Рисуем круг
        painter.drawEllipse(self.center, self.radius, self.radius)

    def setColor(self, color):
        """Устанавливает цвет заливки круга."""
        self.fillColor = color

class circleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self, circle):
        """Добавляем стрелку в список и обновляем виджет."""
        self.circles.append(circle)
        # Создали лэйбл
        self.label = QLabel(circle.value, self)
        self.label.setStyleSheet("background-color: none;")  # Убираем фон у QLabel
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(circle.center.x() - circle.radius, circle.center.y() - circle.radius)
        self.label.resize(2 * circle.radius, 2 * circle.radius)  # Размер QLabel под радиус круга
        self.update()  # Обновление для перерисовки

    def paintEvent(self, event):
        """Отрисовка стрелок поверх виджета."""
        super().paintEvent(event)  # Вызов оригинальной отрисовки виджета
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # Рисуем все круги
        for circle in self.circles:
            circle.draw(painter)

    def setFillColor(self, name, color):
        """Меняет цвет заливки круга по имени."""
        print(len(self.circles))
        for circle in self.circles:
            if circle.name == name:
                print(name)
                circle.setColor(color)
                self.update()  # Обновление виджета для перерисовки

class circleParam:
    def __init__(self, center, radius, name, borderColor, fillColor, value):
        self.center = center
        self.radius = radius
        self.name = name
        self.borderColor = borderColor
        self.fillColor = fillColor
        self.value = value
