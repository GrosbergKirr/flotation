import math

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPolygon, QBrush, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Arrow(QWidget):
    def __init__(self, start_point, end_point, width, height, color, parent=None):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.start_point = QtCore.QPoint(int(start_point[0]*self.width), int(start_point[1]*self.height))
        self.end_point = QtCore.QPoint(int(end_point[0]*self.width), int(end_point[1]*self.height))
        self.arrow_color = color
        self.path = []

    # Метод для смены цвета
    def set_color(self, color):
        """Изменить цвет стрелки."""
        self.color = color
        self.update()

    # Создаем метод для задавания точек изгиба
    def set_bend_points(self, points):
        """Устанавливаем точки изгиба для прямой."""
        pointsQt = []
        for point in points:
            pointsQt.append(QtCore.QPoint(int(point[0]*self.width), int(point[1]*self.height)))
        self.path = pointsQt
        self.update()


    # Рисуем наконечник стрелки
    def draw_arrow_head(self, painter, start_point, end_point):
        # Вычисляем угол линии
        dx = end_point.x() - start_point.x()
        dy = end_point.y() - start_point.y()
        angle = math.atan2(dy, dx)

        arrow_size = 15

        # Острее углы стрелки
        p1 = QPoint(
            int(end_point.x() - arrow_size * math.cos(angle - math.pi / 10)),
            int(end_point.y() - arrow_size * math.sin(angle - math.pi / 10))
        )
        p2 = QPoint(
            int(end_point.x() - arrow_size * math.cos(angle + math.pi / 10)),
            int(end_point.y() - arrow_size * math.sin(angle + math.pi / 10))
        )
        p3 = end_point

        # Создаем треугольник (головку стрелки)
        arrow_head = QPolygon([p1, p2, p3])

        # Закрашиваем треугольник внутри
        painter.setBrush(QBrush(self.arrow_color, Qt.SolidPattern))
        painter.drawPolygon(arrow_head)

    """Отрисовываем стрелку."""
    def draw(self, painter):

        painter.setPen(QtGui.QPen(self.arrow_color, 2))

        current_point = self.start_point
        for point in self.path:
            painter.drawLine(current_point, point)
            current_point = point

        painter.drawLine(current_point, self.end_point)

        # Вызов функции для рисования наконечника
        self.draw_arrow_head(painter, current_point, self.end_point)

    # Метод вызывающий рисование (наследуется от родителя)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Включаем сглаживание

        # Настройка пера с выбранным цветом, тоньше для более "строгого" вида и поставновка карандаша на экран
        pen = QPen(self.arrow_color, 2, Qt.SolidLine)
        painter.setPen(pen)

        # Вызываем функцию которая рисует всю стрелку целиком с изгибами и наконечником
        self.draw(painter)


        # # Рисуем линию
        # painter.drawLine(self.start_point, self.end_point)
        # # Рисуем треугольник для стрелки на конце линии
        # self.draw_arrow_head(painter, self.start_point, self.end_point)
