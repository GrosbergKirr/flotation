from PyQt5 import QtGui, QtCore

from objects.wigets.connections.connection_maker import connectionWidget, connectionParam, Arrow
from objects.wigets.pictures_widgets.side_pictures import Pic
from objects.wigets.tables.side_tables import SideTableParam1, SideTableParam2
from objects.wigets.tables.tables import MainTableParam


class Tab1:
    def __init__(self, width, height, tab):
        self.tab1 = tab
        self.screen_width = width
        self.screen_height = height

        self.picturesCreate()
        self.connectionCreate()
        self.mainTableCreate()
        self.sideTableCreate()
        self.miniTableCreate()





    def mainTableCreate(self):
        # TODO: Переделать со списка на мапу
        '''Создаем основные таблицы!!'''
        self.mainTables = []
        # Размеры основных таблиц
        mainTablesSize = (0.11, 0.09)
        # Относительные (относительно экрана) координаты основных таблиц
        tablesCoordinates = ((0.01, 0.3),
                             (0.20, 0.1),
                             (0.36, 0.1),
                             (0.52, 0.1),
                             (0.36, 0.3),
                             (0.36, 0.5),
                             (0.36, 0.70),
                             (0.20, 0.70),
                             (0.85, 0.1),
                             )
        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(tablesCoordinates):
            buttonsNames = (f"bt{j + 1}_1", f"bt{j + 1}_2", f"bt{j + 1}_3", f"bt{j + 1}_4",
                            f"bt{j + 1}_5", f"bt{j + 1}_6", f"bt{j + 1}_7", f"bt{j + 1}_8", f"bt{j + 1}_9")
            buttonsTexts = (f"bt{j + 1}_1", f"bt{j + 1}_2", f"bt{j + 1}_3", f"bt{j + 1}_4",
                            f"bt{j + 1}_5", f"bt{j + 1}_6", f"bt{j + 1}_7", f"bt{j + 1}_8", f"bt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(mainTablesSize[0] * self.screen_width), int(mainTablesSize[1] * self.screen_height))
            self.table = MainTableParam(buttonsNames, buttonsTexts, pos0, j + 1, self.tab1)
            self.table.setObjectName(f"table{j + 1}")
            self.mainTables.append(self.table)

            """СТРОКИ СМЕНЫ ЦВЕТА СТРЕЛКИ ПО КНОПКЕ"""
        self.mainTables[0].buttons[0].clicked.connect(lambda: self.connWid.color_arrows([1,2,3,4, 5], QtGui.QColor(255, 0, 0)))
        # self.mainTables[0].buttons[0].clicked.connect(lambda: self.connWid.update())
        """----------------------------------------------------"""


    def sideTableCreate(self):
        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.05, 0.12)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.625, 0.30),
                                 (0.625, 0.47),
                                 (0.625, 0.64),
                                 (0.795, 0.30),
                                 (0.795, 0.47),
                                 (0.795, 0.64),
                                 )

        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))
            self.table = SideTableParam1(sideButtonsNames, sideButtonsTexts, pos0, j + 1, self.tab1)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)

        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.05, 0.12)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.70, 0.30),
                                 (0.70, 0.47),
                                 (0.70, 0.64),
                                 (0.87, 0.30),
                                 (0.87, 0.47),
                                 (0.87, 0.64),
                                 )
        numOfRows = 5
        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))

            self.table = SideTableParam2(sideButtonsNames, sideButtonsTexts, pos0, j + 1, numOfRows, self.tab1)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)


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
            self.table = SideTableParam2(sideButtonsNames, sideButtonsTexts, pos0, j + 1, numOfRows,  self.tab1)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)

    def picturesCreate(self):
        picPath1 = r"data/pictures/pic1.png"
        PicturesCoordinates1 = (0.63, 0.20)
        PicturesSize1 = (0.05, 0.07)
        self.pic1 = Pic(picPath1, PicturesCoordinates1, PicturesSize1,
                       self.screen_width, self.screen_height, self.tab1)

        PicturesCoordinates1_1 = (0.798, 0.20)
        PicturesSize1_1 = (0.05, 0.07)
        self.pic1_1 = Pic(picPath1, PicturesCoordinates1_1, PicturesSize1_1,
                       self.screen_width, self.screen_height, self.tab1)

        picPath2 = r"data/pictures/pic2.png"
        PicturesCoordinates2 = (0.72, 0.21)
        PicturesSize2 = (0.04, 0.06)
        self.pic2 = Pic(picPath2, PicturesCoordinates2, PicturesSize2,
                       self.screen_width, self.screen_height, self.tab1)

        picPath3 = r"data/pictures/pic3.png"
        PicturesCoordinates3 = (0.52, 0.49)
        PicturesSize3 = (0.045, 0.067)
        self.pic3 = Pic(picPath3, PicturesCoordinates3, PicturesSize3,
                       self.screen_width, self.screen_height, self.tab1)

        picPath4 = r"data/pictures/pic4.png"
        PicturesCoordinates4 = (0.515, 0.72)
        PicturesSize4 = (0.045, 0.067)
        self.pic4 = Pic(picPath4, PicturesCoordinates4, PicturesSize4,
                       self.screen_width, self.screen_height, self.tab1)

        picPath5 = r"data/pictures/pic5.png"
        PicturesCoordinates5 = (0.485, 0.75)
        PicturesSize5 = (0.02, 0.03)
        self.pic5 = Pic(picPath5, PicturesCoordinates5, PicturesSize5,
                       self.screen_width, self.screen_height, self.tab1)

        PicturesCoordinates5_1 = (0.479, 0.76)
        PicturesSize5_1 = (0.02, 0.03)
        self.pic5_1 = Pic(picPath5, PicturesCoordinates5_1, PicturesSize5_1,
                        self.screen_width, self.screen_height, self.tab1)

        picPath6 = r"data/pictures/pic6.png"
        PicturesCoordinates6 = (0.06, 0.18)
        PicturesSize6 = (0.05, 0.08)
        self.pic6 = Pic(picPath6, PicturesCoordinates6, PicturesSize6,
                        self.screen_width, self.screen_height, self.tab1)

        picPath7 = r"data/pictures/pic7.png"
        PicturesCoordinates7 = (0.27, 0.50)
        PicturesSize7 = (0.08, 0.11)
        self.pic7 = Pic(picPath7, PicturesCoordinates7, PicturesSize7,
                        self.screen_width, self.screen_height, self.tab1)

    def connectionCreate(self):
        # Создаем виджет под все стрелки
        self.connWid = connectionWidget(self.tab1)
        self.connWid.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.connParams = []

        # Список параметров для стрелок (начало, конец, имя, изгибы, цвет, наличие стрелки)
        arrows_data = [
            ((0.085, 0.30), (0.085, 0.26), "arrow_0", [], QtCore.Qt.gray, 5),
            ((0.073, 0.2), (0.822, 0.21), "arrow_1", [(0.073, 0.03), (0.822, 0.03)], QtCore.Qt.gray, 5),
            ((0.098, 0.2), (0.652, 0.21), "arrow_2", [(0.098, 0.045), (0.652, 0.045)], QtCore.Qt.gray, 5),
            ((0.489, 0.76), (0.736, 0.09), "arrow_3", [(0.489, 0.07), (0.736, 0.07)], QtCore.Qt.gray, 5, False),
            ((0.495, 0.753), (0.736, 0.09), "arrow_4", [(0.495, 0.09)], QtCore.Qt.gray, 5, False),
            ((0.736, 0.09), (0.736, 0.22), "arrow_5", [], QtCore.Qt.gray, 5),
            ((0.722, 0.245), (0.671, 0.245), "arrow_6", [], QtCore.Qt.gray,3),
            ((0.75, 0.245), (0.803, 0.245), "arrow_7", [], QtCore.Qt.gray,3),
            ((0.651, 0.265), (0.651, 0.30), "arrow_8", [], QtCore.Qt.gray,3),
            ((0.8205, 0.265), (0.8205, 0.30), "arrow_9", [], QtCore.Qt.gray,3),
            # Блок стрелок между 1 и 2 побочными таблицами (по вертикали)
            ((0.63, 0.33), (0.61, 0.39), "arrow_10", [(0.61, 0.33)], QtCore.Qt.gray, 5,False),
            ((0.63, 0.39), (0.61, 0.39), "arrow_11", [], QtCore.Qt.gray, 5, False),
            ((0.61, 0.39), (0.61, 0.44), "arrow_12", [], QtCore.Qt.gray, 5, False),
            ((0.61, 0.44), (0.61, 0.50), "arrow_13", [], QtCore.Qt.gray, 5, False),
            ((0.61, 0.50), (0.63, 0.50), "arrow_14", [], QtCore.Qt.gray, 5, False),
            ((0.61, 0.50), (0.63, 0.555), "arrow_15", [(0.61, 0.555)], QtCore.Qt.gray, 5,False),
            ########
            ((0.651, 0.41), (0.651, 0.47), "arrow_16", [], QtCore.Qt.gray, 5),
            ((0.8205, 0.41), (0.8205, 0.47), "arrow_17", [], QtCore.Qt.gray, 5),
            ((0.61, 0.44), (0.8205, 0.44), "arrow_18", [], QtCore.Qt.gray, 5, False),
            ((0.61, 0.44), (0.56, 0.49), "arrow_19", [(0.56, 0.44)], QtCore.Qt.gray, 5 ),
            # Блок стрелок между 4 и 5 побочными таблицами (по вертикали)
            ((0.80, 0.33), (0.78, 0.39), "arrow_20", [(0.78, 0.33)], QtCore.Qt.gray, 5, False),
            ((0.80, 0.39), (0.78, 0.39), "arrow_21", [], QtCore.Qt.gray, 5, False),
            ((0.78, 0.39), (0.78, 0.44), "arrow_22", [], QtCore.Qt.gray, 5, False),
            ((0.78, 0.44), (0.78, 0.50), "arrow_23", [], QtCore.Qt.gray, 5, False),
            ((0.78, 0.50), (0.80, 0.50), "arrow_24", [], QtCore.Qt.gray, 5, False),
            ((0.78, 0.50), (0.80, 0.555), "arrow_25", [(0.78, 0.555)], QtCore.Qt.gray, 5, False),
            ########
            ((0.651, 0.59), (0.651, 0.64), "arrow_26", [], QtCore.Qt.gray, 5),
            ((0.8205, 0.59), (0.8205, 0.64), "arrow_27", [], QtCore.Qt.gray, 5),
            ((0.78, 0.67), (0.61, 0.64), "arrow_28", [(0.78, 0.62), (0.61, 0.62)], QtCore.Qt.gray, 5, False),
            ((0.61, 0.64), (0.61, 0.67), "arrow_29", [], QtCore.Qt.gray,3, False),
            ((0.63, 0.67), (0.61, 0.67), "arrow_30", [], QtCore.Qt.gray,3, False),
            ((0.63, 0.72), (0.61, 0.67), "arrow_31", [(0.61, 0.72)], QtCore.Qt.gray, 5,False),
            ((0.80, 0.67), (0.78, 0.67), "arrow_32", [], QtCore.Qt.gray, 5, False),
            ((0.80, 0.72), (0.78, 0.67), "arrow_33", [(0.78, 0.72 )], QtCore.Qt.gray, 5, False),
            ((0.61, 0.64), (0.55, 0.72), "arrow_34", [(0.55, 0.64)], QtCore.Qt.gray, 5),
            ((0.31, 0.61), (0.54, 0.72), "arrow_35", [(0.31, 0.66), (0.54, 0.66)], QtCore.Qt.gray, 5),
            ((0.541, 0.511), (0.531, 0.47), "arrow_36", [(0.541, 0.47)], QtCore.Qt.gray, 5, False),
            ((0.531, 0.516), (0.531, 0.47), "arrow_37", [], QtCore.Qt.gray, 5, False),
            ((0.531, 0.47), (0.31, 0.54), "arrow_38", [(0.45,0.47), (0.45, 0.45), (0.31, 0.45)], QtCore.Qt.gray, 5),
            ((0.27, 0.56), (0.20, 0.74), "arrow_35", [(0.18, 0.56), (0.18, 0.74)], QtCore.Qt.gray, 5),
            # SUB ARROWS
            # Верхний ряд стрелок слева-направо
            ((0.258, 0.031), (0.284, 0.1), "sub_arrow_0", [(0.258, 0.076), (0.284, 0.076)], QtCore.Qt.cyan, 3, False),
            ((0.25, 0.047), (0.284, 0.1), "sub_arrow_1", [(0.25, 0.08), (0.284, 0.08)], QtCore.Qt.cyan, 3, False),

            ((0.3, 0.158), (0.36, 0.165), "sub_arrow_2", [(0.335, 0.158), (0.335, 0.165)], QtCore.Qt.cyan, 3, False),
            ((0.39, 0.2), (0.44, 0.3), "sub_arrow_3", [(0.39, 0.245), (0.44, 0.245)], QtCore.Qt.cyan, 3, False),
            # Правые верхние таблицы с кружочками
            ((0.55, 0.2), (0.6343, 0.245), "sub_arrow_4", [(0.55, 0.245)], QtCore.Qt.cyan, 3, False),
            ((0.71, 0.19), (0.66, 0.215), "sub_arrow_5", [(0.71, 0.21), (0.66, 0.21)], QtCore.Qt.cyan, 3, False),
            ((0.778, 0.19), (0.812, 0.215), "sub_arrow_6", [(0.778, 0.21), (0.812, 0.21)], QtCore.Qt.cyan, 3, False),
            ((0.88, 0.2), (0.838, 0.245), "sub_arrow_7", [(0.88, 0.245)], QtCore.Qt.cyan, 3, False),
            # Стрелки между большими центральными таблицами

            ((0.47, 0.355), (0.491, 0.33), "sub_arrow_8", [(0.48, 0.355), (0.48, 0.33)], QtCore.Qt.cyan, 3, False),
            ((0.319, 0.38), (0.43, 0.45), "sub_arrow_9", [(0.319, 0.42), (0.43, 0.42)], QtCore.Qt.cyan, 3, False),
            ((0.43, 0.45), (0.443, 0.5), "sub_arrow_10", [(0.43, 0.47), (0.443, 0.47)], QtCore.Qt.cyan, 3, False),
            ((0.43, 0.66), (0.443, 0.7), "sub_arrow_11", [(0.43, 0.68), (0.443, 0.68)], QtCore.Qt.cyan, 3, False),
            # Центральные мелкие стрелки

            ((0.493, 0.33), (0.5, 0.33), "sub_arrow_12", [], QtCore.Qt.blue, 3, False),
            ((0.493, 0.38), (0.5, 0.38), "sub_arrow_13", [], QtCore.Qt.blue, 3, False),
            # Тут 2 мелких дорисовать потом
            ((0.504, 0.765), (0.515, 0.765), "sub_arrow_16", [], QtCore.Qt.blue, 3, False),
            ((0.498, 0.775), (0.515, 0.775), "sub_arrow_17", [], QtCore.Qt.blue, 3, False),
            # Тут 1 мелких дорисовать потом

            # ПРАВЫЙ БЛОК КУЧИ МЕЛКИХ СИНИХ СТРЕЛОК
                # Левые верхние
            ((0.661, 0.263), (0.7, 0.316), "sub_arrow_18", [(0.688, 0.263), (0.688, 0.316)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.33), (0.7, 0.338), "sub_arrow_19", [(0.688, 0.33), (0.688, 0.338)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.373), (0.7, 0.361), "sub_arrow_20", [(0.688, 0.373), (0.688, 0.361)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.414), (0.7, 0.387), "sub_arrow_21", [(0.688, 0.414), (0.688, 0.387)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.414), (0.7, 0.407), "sub_arrow_22", [(0.688, 0.414), (0.688, 0.407)], QtCore.Qt.blue, 3, False),
                # Левые центральные
            ((0.675, 0.5), (0.7, 0.509), "sub_arrow_24", [(0.688, 0.5), (0.688, 0.509)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.55), (0.7, 0.533), "sub_arrow_25", [(0.688, 0.55), (0.688, 0.533)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.583), (0.7, 0.556), "sub_arrow_26", [(0.688, 0.583), (0.688, 0.556)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.583), (0.7, 0.572), "sub_arrow_27", [(0.688, 0.583), (0.688, 0.572)], QtCore.Qt.blue, 3, False),
                # Левые нижние
            ((0.675, 0.667), (0.7, 0.676), "sub_arrow_24", [(0.688, 0.667), (0.688, 0.676)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.717), (0.7, 0.7), "sub_arrow_25", [(0.688, 0.717), (0.688, 0.7)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.75), (0.7, 0.723), "sub_arrow_26", [(0.688, 0.75), (0.688, 0.723)], QtCore.Qt.blue, 3, False),
            ((0.675, 0.75), (0.7, 0.739), "sub_arrow_27", [(0.688, 0.75), (0.688, 0.739)], QtCore.Qt.blue, 3, False),
                # Правые верхние
            ((0.831, 0.263), (0.87, 0.316), "sub_arrow_18", [(0.858, 0.263), (0.858, 0.316)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.33), (0.87, 0.338), "sub_arrow_19", [(0.858, 0.33), (0.858, 0.338)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.373), (0.87, 0.361), "sub_arrow_20", [(0.858, 0.373), (0.858, 0.361)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.414), (0.87, 0.387), "sub_arrow_21", [(0.858, 0.414), (0.858, 0.387)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.414), (0.87, 0.407), "sub_arrow_22", [(0.858, 0.414), (0.858, 0.407)], QtCore.Qt.blue, 3, False),
                # Правые центральные
            ((0.845, 0.5), (0.87, 0.509), "sub_arrow_24", [(0.858, 0.5), (0.858, 0.509)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.55), (0.87, 0.533), "sub_arrow_25", [(0.858, 0.55), (0.858, 0.533)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.583), (0.87, 0.556), "sub_arrow_26", [(0.858, 0.583), (0.858, 0.556)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.583), (0.87, 0.572), "sub_arrow_27", [(0.858, 0.583), (0.858, 0.572)], QtCore.Qt.blue, 3, False),
                # Правые нижние
            ((0.845, 0.667), (0.87, 0.676), "sub_arrow_24", [(0.858, 0.667), (0.858, 0.676)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.717), (0.87, 0.7), "sub_arrow_25", [(0.858, 0.717), (0.858, 0.7)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.75), (0.87, 0.723), "sub_arrow_26", [(0.858, 0.75), (0.858, 0.723)], QtCore.Qt.blue, 3, False),
            ((0.845, 0.75), (0.87, 0.739), "sub_arrow_27", [(0.858, 0.75), (0.858, 0.739)], QtCore.Qt.blue, 3, False),
        ]

        # Добавляем все стрелки в список connParams
        for data in arrows_data:
            # Если head не указан в data, устанавливаем его в True по умолчанию
            if len(data) == 6:
                data = (*data, True)
            start, end, name, bends, color, sickness, head = data
            conn = connectionParam(start, end, name, bends, color, sickness, head)
            self.connParams.append(conn)

        # Создаем и добавляем стрелки в виджет
        for i in self.connParams:
            arrow = Arrow(i.start, i.end, self.screen_width, self.screen_height, i.color, i.sickness, i.head)
            arrow.set_name(i.name)
            arrow.set_bend_points(i.bends)
            self.connWid.add_arrow(arrow)













