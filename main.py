import sys

from PyQt5.QtGui import QPalette

from Tabs.full_tab_1 import *
from Tabs.full_tab_2 import *
from tables_wigets.tables import *
from tables_wigets.side_tables import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, screen_size):
        super().__init__()
        self.setWindowTitle("MainWindow")

        # Настройка основного виджета и размера экрана
        self.screen_width = screen_size.width()
        self.screen_height = screen_size.height()
        self.resize(self.screen_width, self.screen_height)


        # Создаем QTabWidget для вкладок
        self.tabs = QTabWidget()

        '''Первая вкладка'''
        # Виджет для вкладки
        self.tab1 = QWidget()
        # Добавляем виджет вкладки в общий виджет вкладок
        self.tabs.addTab(self.tab1, "Вкладка 1")
        # Все наполнение вкладки в классе Tab1
        Tab1(self.screen_width, self.screen_height, self.tab1)

        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Вкладка 2")
        Tab2(self.screen_width, self.screen_height, self.tab2)

        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Вкладка 3")




        self.setCentralWidget(self.tabs)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#FAFEF8"))
        self.setPalette(palette)

        # self.mainTableCreate()
        # self.sideTableCreate()
        # self.picturesCreate()







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
