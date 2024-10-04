import sys

from PyQt5.QtGui import QPalette, QColor

from side_pictures import Pic
from tables import *
from side_tables import *
from load_and_process import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, screen_size):
        super().__init__()
        self.setWindowTitle("MainWindow")

        # Настройка основного виджета и размера экрана
        self.screen_width = screen_size.width()
        self.screen_height = screen_size.height()
        self.resize(self.screen_width, self.screen_height)

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        palette = self.palette()
        # palette.setColor(QPalette.Window, QColor("#FAFEF8"))
        self.setPalette(palette)

        self.mainTableCreate()
        self.sideTableCreate()
        self.picturesCreate()

    def mainTableCreate(self):
        # TODO: Переделать со списка на мапу
        '''Создаем основные таблицы!!'''
        self.mainTables = []
        # Размеры основных таблиц
        mainTablesSize = (0.13, 0.11)
        # Относительные (относительно экрана) координаты основных таблиц
        tablesCoordinates = ((0.01, 0.3),
                             (0.22, 0.1),
                             (0.38, 0.1),
                             (0.54, 0.1),
                             (0.38, 0.3),
                             (0.38, 0.5),
                             (0.38, 0.70),
                             (0.22, 0.70),
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
            self.table = MainTableParam(buttonsNames, buttonsTexts, pos0, j + 1, self.central_widget)
            self.table.setObjectName(f"table{j + 1}")
            self.mainTables.append(self.table)

    def sideTableCreate(self):
        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.07, 0.14)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.57, 0.28),
                                 (0.57, 0.45),
                                 (0.57, 0.62),
                                 (0.77, 0.28),
                                 (0.77, 0.45),
                                 (0.77, 0.62),
                                 )

        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))
            self.table = SideTableParam1(sideButtonsNames, sideButtonsTexts, pos0, j + 1, self.central_widget)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)

        '''Создаем побочные таблицы'''
        self.sideTables = []
        # Размеры основных таблиц
        sideTablesSize = (0.07, 0.14)
        # Относительные (относительно экрана) координаты побочных таблиц
        sideTablesCoordinates = ((0.65, 0.28),
                                 (0.65, 0.45),
                                 (0.65, 0.62),
                                 (0.85, 0.28),
                                 (0.85, 0.45),
                                 (0.85, 0.62),
                                 )

        # j + 1 чтобы таблицы нумеровались с единицы
        for j, i in enumerate(sideTablesCoordinates):
            sideButtonsNames = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            sideButtonsTexts = (f"sbt{j + 1}_1", f"sbt{j + 1}_2", f"sbt{j + 1}_3", f"sbt{j + 1}_4",
                                f"sbt{j + 1}_5", f"sbt{j + 1}_6", f"sbt{j + 1}_7", f"sbt{j + 1}_8", f"sbt{j + 1}_9")
            pos0 = (int(i[0] * self.screen_width), int(i[1] * self.screen_height),
                    int(sideTablesSize[0] * self.screen_width), int(sideTablesSize[1] * self.screen_height))
            self.table = SideTableParam2(sideButtonsNames, sideButtonsTexts, pos0, j + 1, self.central_widget)
            self.table.setObjectName(f"sideTable{j + 1}")
            self.sideTables.append(self.table)

    def picturesCreate(self):
        picPath1 = r"C:\Users\grosy\OneDrive\Pictures\power.png"
        sidePicturesCoordinates1 = (0.07, 0.12)
        #относительные раземры кратинки
        mainPicturesSize1 = (0.055, 0.075)
        pos = (int(sidePicturesCoordinates1[0] * self.screen_width),
               int(sidePicturesCoordinates1[1] * self.screen_height),
               int(mainPicturesSize1[0] * self.screen_width),
               int(mainPicturesSize1[1] * self.screen_height),
               )
        picSize = (int(mainPicturesSize1[0] * self.screen_width),
                   int(mainPicturesSize1[1] * self.screen_height))
        self.pic = Pic(pos, picPath1, picSize, self.central_widget)
    #
    #     picPath2 = r"C:\Users\grosy\OneDrive\Pictures\power2.png"
    #     sidePicturesCoordinates2 = (0.25, 0.47)
    #     # относительные раземры кратинки
    #     mainPicturesSize2 = (0.1, 0.13)
    #     pos = (int(sidePicturesCoordinates2[0] * self.screen_width),
    #            int(sidePicturesCoordinates2[1] * self.screen_height),
    #            int(mainPicturesSize2[0] * self.screen_width),
    #            int(mainPicturesSize2[1] * self.screen_height),
    #            )
    #     picSize = (int(mainPicturesSize2[0] * self.screen_width),
    #                int(mainPicturesSize2[1] * self.screen_height))
    #     self.pic = Pic(pos, picPath2, picSize, self.central_widget)
    #
    #     picPath3 = r"C:\Users\grosy\OneDrive\Pictures\pic1.png"
    #     sidePicturesCoordinates3 = (0.4, 0.47)
    #     # относительные раземры кратинки
    #     mainPicturesSize3 = (0.1, 0.13)
    #     pos = (int(sidePicturesCoordinates3[0] * self.screen_width),
    #            int(sidePicturesCoordinates3[1] * self.screen_height),
    #            int(mainPicturesSize3[0] * self.screen_width),
    #            int(mainPicturesSize3[1] * self.screen_height),
    #            )
    #     picSize = (int(mainPicturesSize3[0] * self.screen_width),
    #                int(mainPicturesSize3[1] * self.screen_height))
    #     self.pic = Pic(pos, picPath3, picSize, self.central_widget)


if __name__ == "__main__":
    # Читаем данные
    # print("read data...")
    # df = load_df('short_df.xlsx')
    # print("read data success!")
    # # Запускаем приложение и берем разрешение экрана
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_size = screen.size()
    # открываем главное окно
    window = MainWindow(screen_size)
    window.showMaximized()
    sys.exit(app.exec_())
