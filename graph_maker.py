import plotly
import plotly.graph_objects as go
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from scipy.signal import savgol_filter


# Класс для окна с графиком
class GraphMaker(QtWidgets.QWidget):
    def __init__(self, df):
        super().__init__()
        self.setWindowTitle("График")
        self.setGeometry(100, 100, 800, 600)

        # Создаем QWebEngineView для отображения графика
        self.browser = QWebEngineView(self)
        self.browser.setGeometry(0, 0, 700, 600)

        # Создаем график с помощью Plotly
        self.df = df
        self.param_name = df.columns[0] # В датафрейме одна целевая колонка
        self.createGraph()

    def createGraph(self):
        # some example data

        WINDOW = 60

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df.index, y=self.df[self.param_name], name=self.param_name))
        fig.add_trace(go.Scatter(x=self.df.index, y=savgol_filter(self.df[self.param_name], WINDOW, 5), line=dict(width=2),
                                 name='Усреднение по 5 порядку'))

        # we create html code of the figure
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        # we create an instance of QWebEngineView and set the html code
        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        # set the QWebEngineView instance as main widget

        # Отображаем HTML в QWebEngineView
        self.browser.setHtml(html)


# class Graph1(GraphMaker):
#     def __init__(self, df):
#         super().__init__()


