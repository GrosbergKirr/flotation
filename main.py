import os
import sys

from PyQt5.QtWidgets import QWidget, QTabWidget

from objects.Tabs.full_tab_1 import *
from objects.Tabs.full_tab_2 import *
from objects.Tabs.full_tab_3 import *
from configuration.logger import SetLogger
from objects.wigets.tables.side_tables import *
from configuration.config import LoadConfig
from service.load_and_update import LoadAndUpdateService
from storage.connector import *



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, screenSize):
        super().__init__()
        self.setWindowTitle("MainWindow")
        self.screen_width = screenSize.width()
        self.screen_height = screenSize.height()
        self.resize(self.screen_width, self.screen_height)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Вкладка 1")
        Tab1(self.screen_width, self.screen_height, self.tab1)

        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Вкладка 2")
        Tab2(self.screen_width, self.screen_height, self.tab2)

        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Вкладка 3")
        Tab3(self.screen_width, self.screen_height, self.tab3)

        self.setCentralWidget(self.tabs)

        # LoadAndUpdateService(Tab1, )

if __name__ == "__main__":
    # cfg = LoadConfig("config.yml")
    # log = SetLogger(cfg.service)
    # log.info("Set logger and config successful")
    # engine = connectToDb(cfg.database, log)
    # data = fetch_all_to_dataframe(engine, "data", log)
    # if data is not None:
    #     log.info("get data from db successful")
    #     log.debug(f"Top of DataFrame:\n{data.head()}")
    # else:
    #     log.warning("no data fetched")
    #     os.exit(1)

    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_size = screen.size()
    window = MainWindow(screen_size)
    window.showMaximized()
    sys.exit(app.exec_())