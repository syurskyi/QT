from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DonutChart Example")
        self.setGeometry(100,100, 1280,600)

        self.show()

        self.create_donutchart()



    def create_donutchart(self):

        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append("Protein 4.2%", 4.2)
        slice = QPieSlice()
        slice = series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Other 23.8%", 23.8);
        series.append("Carbs 56.4%", 56.4);





        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("DonutChart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)



        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)


        self.setCentralWidget(chartview)







App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())