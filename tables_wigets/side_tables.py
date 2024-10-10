from PyQt5 import QtWidgets, QtCore


class SideTableParam1(QtWidgets.QWidget):
    def __init__(self, buttons_texts, buttons_names, pos,tableNum, parent=None):
        super().__init__(parent)
        self.buttons_texts = buttons_texts
        self.buttons_names = buttons_names
        self.pos = pos
        self.tableNum = tableNum
        self.init_ui()

    def init_ui(self):
        # Создаем виджет
        self.setGeometry(QtCore.QRect(*self.pos))
        # Создаем лэйаут
        self.table = QtWidgets.QGridLayout(self)
        self.table.setContentsMargins(0, 0, 0, 0)
        self.table.setSpacing(0)
        self.table.setObjectName(f"table2_{self.tableNum}")

        # Добавляем кнопки и лейблы в лэйаут
        # TODO: переделать на мапу
        self.buttons1 = []
        for i in range(2):
            button1 = QtWidgets.QPushButton(self)
            button1.setObjectName(self.buttons_names[i])
            button1.setText(self.buttons_texts[i])
            button1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.table.addWidget(button1, i, 1, 1, 1)
            self.buttons1.append(button1)

        # Добавляем лейблы
        labelName = "ДМВК,\nт/ч"
        for i in range(2):
            label = QtWidgets.QLabel(self)
            label.setObjectName(f"label{i + 1}")
            label.setText(labelName)
            label.setStyleSheet("font-size: 10px;")
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.table.addWidget(label, i, 2, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)

class SideTableParam2(QtWidgets.QWidget):
    def __init__(self, buttons_texts, buttons_names, pos, tableNum, numOfRows, parent=None):
        super().__init__(parent)
        self.numOfRows = numOfRows
        self.buttons_texts = buttons_texts
        self.buttons_names = buttons_names
        self.pos = pos
        self.tableNum = tableNum
        self.init_ui()

    def init_ui(self):
        # Создаем виджет
        self.setGeometry(QtCore.QRect(*self.pos))
        # self.setObjectName(f"gridLayoutWidget_2")
        # Создаем лэйаут
        self.table = QtWidgets.QGridLayout(self)
        # self.table.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.table.setContentsMargins(0, 0, 0, 0)
        self.table.setSpacing(0)
        self.table.setObjectName(f"table2_{self.tableNum}")

        # Добавляем кнопки и лейблы в лэйаут
        # TODO: переделать на мапу
        self.buttons = []
        for i in range(self.numOfRows):
            button = QtWidgets.QPushButton(self)
            button.setObjectName(self.buttons_names[i])
            button.setText(self.buttons_texts[i])
            button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.table.addWidget(button, i, 1, 1, 1)
            self.buttons.append(button)

        # Добавляем лейблы
        labelName = "ДМВК,\nт/ч"
        for i in range(self.numOfRows):
            label = QtWidgets.QLabel(self)
            label.setObjectName(f"label{i + 1}")
            label.setText(labelName)
            label.setStyleSheet("font-size: 10px;")
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.table.addWidget(label, i, 2, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)