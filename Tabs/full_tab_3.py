from wigets.tables.tables import MainTableParam


class Tab3:
    def __init__(self, width, height, tab):
        self.tab1 = tab
        self.screen_width = width
        self.screen_height = height


        self.mainTableCreate()
        # self.sideTableCreate()
        # self.picturesCreate()

    def mainTableCreate(self):
        # TODO: Переделать со списка на мапу
        '''Создаем основные таблицы!!'''
        self.mainTables = []
        # Размеры основных таблиц
        mainTablesSize = (0.11, 0.09)
        # Относительные (относительно экрана) координаты основных таблиц
        tablesCoordinates = ((0.01, 0.3),
                             (0.13, 0.08),
                             (0.27, 0.08),
                             (0.57, 0.08),
                             (0.71, 0.08),
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