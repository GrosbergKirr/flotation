from PyQt5 import QtWidgets, QtCore


class MainTableParam(QtWidgets.QWidget):
    def __init__(self, buttons_names, buttons_texts, pos, tableNum, parent=None):
        super().__init__(parent)
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
        self.table.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.table.setContentsMargins(0, 0, 0, 0)
        self.table.setSpacing(0)
        self.table.setObjectName(f"table1_{self.tableNum}")

        self.setStyleSheet("""
                QToolButton {
                    color: rgb(134, 013, 200);
                    border: 1px solid black;
                    padding: 5px;
                    background-color: white;
                }
                QLabel {
                    border: 1px solid black;
                    padding: 5px;
                }
            """)


        # Добавляем кнопки и лейблы в лэйаут
        # TODO: переделать на мапу
        self.buttons = []
        for j in range(9):
            button = QtWidgets.QToolButton(self)
            button.setObjectName(self.buttons_names[j])
            button.setText(self.buttons_texts[j])
            button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            button.clicked.connect(self.clk)
            self.table.addWidget(button, j // 3 + 1, j % 3 + 1)
            self.buttons.append(button)


        # Добавляем лейблы
        verticalIndex = ["Выход", "P2O5\nпрогноз", "P2O5"]
        horizontalIndex = ["т/ч", "%", "E,%"]
        for i, text in enumerate(verticalIndex):
            label = QtWidgets.QLabel(self)
            label.setObjectName(f"labelVert{i+1}")
            label.setText(text)
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.addWidget(label, i + 1, 0, 1, 1)
        for i, text in enumerate(horizontalIndex):
            label = QtWidgets.QLabel(self)
            label.setObjectName(f"labelHor{i+1}")
            label.setText(text)
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.addWidget(label, 0, i + 1, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)

    def clk(self):
        print("clicked")