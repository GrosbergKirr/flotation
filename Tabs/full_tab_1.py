from PyQt5.QtWidgets import QWidget

from connection_maker import Arrow, connectionWidget, connectionParam
from pictures_widgets.side_pictures import *
from tables_wigets.side_tables import *
from tables_wigets.tables import *



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
        self.mainTables[0].buttons[0].clicked.connect(lambda: self.connWid.arrows[2].set_color(QtGui.QColor(255, 0, 0, 128)))
        self.mainTables[0].buttons[0].clicked.connect(lambda: self.connWid.update())
        """----------------------------------------------------"""

        print(self.mainTables[0].buttons[0].objectName())

    def sideTableCreate(self):
        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.05, 0.12)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.60, 0.30),
                                 (0.60, 0.47),
                                 (0.60, 0.64),
                                 (0.77, 0.30),
                                 (0.77, 0.47),
                                 (0.77, 0.64),
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
        sideTablesCoordinates = ((0.67, 0.30),
                                 (0.67, 0.47),
                                 (0.67, 0.64),
                                 (0.84, 0.30),
                                 (0.84, 0.47),
                                 (0.84, 0.64),
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
                                 (0.50, 0.37),
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
        picPath1 = r"data/pic1.png"
        PicturesCoordinates1 = (0.63, 0.20)
        PicturesSize1 = (0.05, 0.07)
        self.pic1 = Pic(picPath1, PicturesCoordinates1, PicturesSize1,
                       self.screen_width, self.screen_height, self.tab1)

        PicturesCoordinates1_1 = (0.80, 0.20)
        PicturesSize1_1 = (0.05, 0.07)
        self.pic1_1 = Pic(picPath1, PicturesCoordinates1_1, PicturesSize1_1,
                       self.screen_width, self.screen_height, self.tab1)

        picPath2 = r"data/pic2.png"
        PicturesCoordinates2 = (0.72, 0.21)
        PicturesSize2 = (0.04, 0.06)
        self.pic2 = Pic(picPath2, PicturesCoordinates2, PicturesSize2,
                       self.screen_width, self.screen_height, self.tab1)

        picPath3 = r"data/pic3.png"
        PicturesCoordinates3 = (0.5, 0.5)
        PicturesSize3 = (0.045, 0.067)
        self.pic3 = Pic(picPath3, PicturesCoordinates3, PicturesSize3,
                       self.screen_width, self.screen_height, self.tab1)

        picPath4 = r"data/pic4.png"
        PicturesCoordinates4 = (0.515, 0.72)
        PicturesSize4 = (0.045, 0.067)
        self.pic4 = Pic(picPath4, PicturesCoordinates4, PicturesSize4,
                       self.screen_width, self.screen_height, self.tab1)

        picPath5 = r"data/pic5.png"
        PicturesCoordinates5 = (0.485, 0.75)
        PicturesSize5 = (0.02, 0.03)
        self.pic5 = Pic(picPath5, PicturesCoordinates5, PicturesSize5,
                       self.screen_width, self.screen_height, self.tab1)

        PicturesCoordinates5_1 = (0.479, 0.76)
        PicturesSize5_1 = (0.02, 0.03)
        self.pic5_1 = Pic(picPath5, PicturesCoordinates5_1, PicturesSize5_1,
                        self.screen_width, self.screen_height, self.tab1)

        picPath6 = r"data/pic6.png"
        PicturesCoordinates6 = (0.06, 0.18)
        PicturesSize6 = (0.05, 0.08)
        self.pic6 = Pic(picPath6, PicturesCoordinates6, PicturesSize6,
                        self.screen_width, self.screen_height, self.tab1)

        picPath7 = r"data/pic7.png"
        PicturesCoordinates7 = (0.27, 0.50)
        PicturesSize7 = (0.08, 0.11)
        self.pic7 = Pic(picPath7, PicturesCoordinates7, PicturesSize7,
                        self.screen_width, self.screen_height, self.tab1)


    def connectionCreate(self):
        # Создаем виджет под все стрелки
        self.connWid = connectionWidget(self.tab1)
        self.connWid.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.connParams = []
        # Первая стрелка
        conn1 = connectionParam((0.073, 0.2), (0.822, 0.21), "arrow_1", [(0.073, 0.03), (0.822, 0.03)], color=QtCore.Qt.gray)
        self.connParams.append(conn1)
        # Вторая стрелка
        conn2 = connectionParam((0.098, 0.2), (0.652, 0.21), "arrow_2", [(0.098, 0.045), (0.652, 0.045)], color=QtCore.Qt.gray)
        self.connParams.append(conn2)
        conn3 = connectionParam((0.489, 0.76), (0.736, 0.22), "arrow_3", [(0.489, 0.07), (0.736, 0.07)],
                                color=QtCore.Qt.gray)
        self.connParams.append(conn3)
        conn3 = connectionParam((0.495, 0.753), (0.736, 0.22), "arrow_3", [(0.495, 0.07), (0.736, 0.07)],
                                color=QtCore.Qt.gray)
        self.connParams.append(conn3)

        for i in self.connParams:
            arrow = Arrow(i.start, i.end, self.screen_width, self.screen_height, i.color)
            arrow.set_name(i.name)
            arrow.set_bend_points(i.bends)
            self.connWid.add_arrow(arrow)












