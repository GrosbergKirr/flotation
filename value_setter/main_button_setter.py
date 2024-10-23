from PyQt5.QtCore import QTimer
import random


class ButtonValueUpdater:
    def __init__(self, buttons, interval=5):
        self.buttons = buttons  # Список кнопок
        self.interval = interval  # Интервал обновления (в секундах)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_button_texts)
        self.timer.start(self.interval * 1000)

    def update_button_texts(self):
        '''Функция для обновления текста кнопок'''
        for i, button in enumerate(self.buttons):
            num = random.random() * 100
            new_text = f"{int(num)}"
            button.setText(new_text)