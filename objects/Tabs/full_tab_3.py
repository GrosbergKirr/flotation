from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor

from objects.wigets.circles.circle_widget import *
from objects.wigets.connections.connection_maker import *
from objects.wigets.pictures_widgets.side_pictures import Pic
from objects.wigets.tables.side_tables import *
from objects.wigets.tables.tables import *


class Tab3:
    def __init__(self, width, height, tab):
        self.tab3 = tab
        self.screen_width = width
        self.screen_height = height

        self.pictureCreate()
        self.circleCreate()
        self.connectionCreate()
        self.mainTableCreate()
        self.sideTableCreate()




    def mainTableCreate(self):
        # TODO: Переделать со списка на мапу
        '''Создаем основные таблицы!!'''
        self.mainTables = []
        # Размеры основных таблиц
        mainTablesSize = (0.11, 0.09)
        # Относительные (относительно экрана) координаты основных таблиц
        tablesCoordinates = ((0.02, 0.65),
                             (0.2, 0.72),
                             (0.32, 0.08),
                             (0.53, 0.08),
                             (0.781, 0.65),
                             )
        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(tablesCoordinates):
            buttonsNames = (f"bt{j + 1}_1", f"bt{j + 1}_2", f"bt{j + 1}_3", f"bt{j + 1}_4",
                            f"bt{j + 1}_5", f"bt{j + 1}_6", f"bt{j + 1}_7", f"bt{j + 1}_8", f"bt{j + 1}_9")
            buttonsTexts = (f"bt{j + 1}_1", f"bt{j + 1}_2", f"bt{j + 1}_3", f"bt{j + 1}_4",
                            f"bt{j + 1}_5", f"bt{j + 1}_6", f"bt{j + 1}_7", f"bt{j + 1}_8", f"bt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(mainTablesSize[0] * self.screen_width), int(mainTablesSize[1] * self.screen_height))

            self.table = MainTableParam(buttonsNames, buttonsTexts, pos0, j + 1, self.tab3)
            self.table.setObjectName(f"table{j + 1}")
            self.mainTables.append(self.table)

        self.mainTables[0].buttons[0].clicked.connect(lambda: self.circleWid.setFillColor("circle_1", QtGui.QColor(255, 100, 100)))

    def sideTableCreate(self):
        '''Создаем побочные таблицы'''
        self.sideTables1 = []
        # Размеры основных таблиц
        sideTablesSize = (0.045, 0.065)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.17, 0.06),
                                 (0.25, 0.06),
                                 (0.17, 0.13),
                                 (0.25, 0.13),
                                 (0.665, 0.06),
                                 (0.745, 0.06),
                                 (0.665, 0.13),
                                 (0.745, 0.13),
                                 )

        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))
            self.table = SideTableParam1(sideButtonsNames, sideButtonsTexts, pos0, j + 1, self.tab3)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables1.append(self.table)

        '''Создаем побочные таблицы ВТОРОГО ТИПА'''
        self.sideTables2 = []
        # Размеры основных таблиц
        sideTablesSize = (0.05, 0.12)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.07, 0.23), # левые сайдтейблс
                                 (0.345, 0.23),
                                 (0.07, 0.4),
                                 (0.345, 0.4),
                                 (0.555, 0.23), # правый сайдтейблс
                                 (0.845, 0.23),
                                 (0.555, 0.4),
                                 (0.845, 0.4),
                                 )
        numOfRows = 4
        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))

            self.table = SideTableParam2(sideButtonsNames, sideButtonsTexts, pos0, j + 1, numOfRows, self.tab3)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables2.append(self.table)

    def miniTableCreate(self):
        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.05, 0.072)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.68, 0.12),
                                 (0.75, 0.12),
                                 (0.29, 0.32),
                                 (0.50, 0.32),
                                 )
        numOfRows = 3
        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"mbt{j + 1}_1", f"mbt{j + 1}_2", f"mbt{j + 1}_3", f"mbt{j + 1}_4",
                                f"mbt{j + 1}_5", f"mbt{j + 1}_6", f"mbt{j + 1}_7", f"mbt{j + 1}_8", f"mbt{j + 1}_9")
            sideButtonsTexts = (f"mbt{j + 1}_1", f"mbt{j + 1}_2", f"mbt{j + 1}_3", f"mbt{j + 1}_4",
                                f"mbt{j + 1}_5", f"mbt{j + 1}_6", f"mbt{j + 1}_7", f"mbt{j + 1}_8", f"mbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))
            self.table = SideTableParam2(sideButtonsNames, sideButtonsTexts, pos0, j + 1, numOfRows, self.tab3)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)


    def pictureCreate(self):
        picPath1 = r"data/pictures/pic6.png"
        PicturesCoordinates1 = (0.2184, 0.37)
        PicturesSize1 = (0.03, 0.053)
        self.pic1 = Pic(picPath1, PicturesCoordinates1, PicturesSize1,
                        self.screen_width, self.screen_height, self.tab3)

        picPath2 = r"data/pictures/pic6.png"
        PicturesCoordinates2 = (0.713, 0.37)
        PicturesSize2 = (0.03, 0.053)
        self.pic2 = Pic(picPath2, PicturesCoordinates2, PicturesSize2,
                        self.screen_width, self.screen_height, self.tab3)
    def circleCreate(self):
        # Список параметров для ОТРИСОВАННЫХ кругов колонн(центр, радиус, имя, цвет контура, цвет заливки, значение переменной)

        self.circleParams = []

        circles = [
            # блок левых кругов
            ((0.165, 0.17), 0.022, "circle_1", QColor("gray"), QColor("lightgray"), "var"),
            ((0.295, 0.17), 0.022, "circle_2", QColor("gray"), QColor("lightgray"), "var"),
            ((0.165, 0.27), 0.022, "circle_1", QColor("gray"), QColor("lightgray"), "var"),
            ((0.295, 0.27), 0.022, "circle_2", QColor("gray"), QColor("lightgray"), "var"),

            # блок правых кругов
            ((0.66, 0.17), 0.022, "circle_1", QColor("gray"), QColor("lightgray"), "var"),
            ((0.79, 0.17), 0.022, "circle_2", QColor("gray"), QColor("lightgray"), "var"),
            ((0.66, 0.27), 0.022, "circle_1", QColor("gray"), QColor("lightgray"), "var"),
            ((0.79, 0.27), 0.022, "circle_2", QColor("gray"), QColor("lightgray"), "var")
        ]
        for data in circles:
            center, radius, name, borderColor, fillColor, value = data
            circle = circleParam(center, radius, name, borderColor, fillColor, value)
            self.circleParams.append(circle)

        self.circleWid = circleWidget(self.tab3)
        self.circleWid.setGeometry(0, 0, self.screen_width, self.screen_height)

        for i in self.circleParams:
            circ = Circle(i.center, i.radius, i.name, i.borderColor, i.fillColor, i.value, self.screen_width, self.screen_height)
            self.circleWid.add_circle(circ)

    def connectionCreate(self):
        # Список параметров для стрелок (начало, конец, имя, изгибы, цвет, наличие стрелки)
        arrows_data = [
            ((0.233, 0.07), (0.233, 0.367), "arrow_0", [], QtCore.Qt.gray, 3),
            ((0.727, 0.07), (0.727, 0.367), "arrow_0", [], QtCore.Qt.gray, 3),

        ]

        self.connParams = []

        # Добавляем все стрелки в список connParams
        for data in arrows_data:
            # Если head не указан в data, устанавливаем его в True по умолчанию
            if len(data) == 6:
                data = (*data, True)
            start, end, name, bends, color, sickness, head = data
            conn = connectionParam(start, end, name, bends, color, sickness, head)
            self.connParams.append(conn)

        # Создаем виджет под все стрелки
        self.connWid = connectionWidget(self.tab3)
        self.connWid.setGeometry(0, 0, self.screen_width, self.screen_height)

        # Создаем и добавляем стрелки в виджет
        for i in self.connParams:
            arrow = Arrow(i.start, i.end, self.screen_width, self.screen_height, i.color, i.sickness, i.head)
            arrow.set_name(i.name)
            arrow.set_bend_points(i.bends)
            self.connWid.add_arrow(arrow)
