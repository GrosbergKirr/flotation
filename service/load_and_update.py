import pandas as pd
from PyQt5.QtCore import QTimer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import config
from data.parameters.params import Params
from objects.Tabs.full_tab_1 import Tab1
from objects.Tabs.full_tab_2 import Tab2
from objects.Tabs.full_tab_3 import Tab3


class LoadAndUpdateService:
    def __init__(self, tab1: Tab1 | Tab2 | Tab3,
                 interval: int):
        self.tab1 = tab1
        self.df = pd.DataFrame()  # Инициализируем пустой DataFrame для хранения данных
        self.internal_var = 0  # Переменная для хранения вычисленного значения
        self.interval = interval  # Интервал обновления в секундах

        # Настраиваем синхронное подключение к базе данных через SQLAlchemy
        engine = create_engine('sqlite:///mydb.db')
        self.Session = sessionmaker(bind=engine)

        # Запускаем QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.getDataFromDb)
        self.timer.start(self.interval * 1000)  # Запуск таймера (каждая минута)

    def getDataFromDb(self):
        session = self.Session()  # Создаем сессию для работы с базой данных
        try:
            # Пример синхронного запроса
            query_result = session.execute("SELECT * FROM table")
            data = query_result.fetchall()

            # Обновляем DataFrame
            new_data = pd.DataFrame(data)
            self.df.update(new_data)
        finally:
            session.close()

    def updateParams(self):
        # Перебираем атрибуты класса Params
        for attr_name in Params.__dict__:
            if not attr_name.startswith("__"):
                value = getattr(Params, attr_name)
                print(f"{attr_name}: {value}")  

