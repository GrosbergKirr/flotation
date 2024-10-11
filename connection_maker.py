import math

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPolygon, QBrush, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Arrow:
    def __init__(self, start_point, end_point, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.start_point = QtCore.QPoint(int(start_point[0]*self.width), int(start_point[1]*self.height))
        self.end_point = QtCore.QPoint(int(end_point[0]*self.width), int(end_point[1]*self.height))
        self.arrow_color = color
        self.path = []
        self.name = None

    # Метод для смены цвета


    # Создаем метод для задавания точек изгиба
    def set_bend_points(self, points):
        """Устанавливаем точки изгиба для прямой."""
        pointsQt = []
        for point in points:
            pointsQt.append(QtCore.QPoint(int(point[0]*self.width), int(point[1]*self.height)))
        self.path = pointsQt
        # self.update()

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.arrow_color = color

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

"""Создаем отдельный виджет для стрелок, чтобы не плодить виджеты под каждую стрелку"""
class connectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.arrows = []

    def add_arrow(self, arrow):
        """Добавляем стрелку в список и обновляем виджет."""
        self.arrows.append(arrow)
        self.update()  # Обновление для перерисовки

    def paintEvent(self, event):
        """Отрисовка стрелок поверх виджета."""
        super().paintEvent(event)  # Вызов оригинальной отрисовки виджета
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Рисуем все стрелки
        for arrow in self.arrows:
            arrow.draw(painter)


class connectionParam:
    def __init__(self, start, end, name, bends, color):
        self.start = start
        self.end = end
        self.name = name
        self.bends = bends
        self.color = color

