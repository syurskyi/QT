from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Line")
        self.setGeometry(100,100, 680,500)

        self.show()

        self.create_linechart()



    def create_linechart(self):

        series = QLineSeries(self)
        series.append(0,6)
        series.append(2, 4)
        series.append(3, 8)
        series.append(7, 4)
        series.append(10, 5)

        series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 2)


        chart =  QChart()

        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())