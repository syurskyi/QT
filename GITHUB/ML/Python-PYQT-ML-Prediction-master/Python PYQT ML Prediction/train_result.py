# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton


import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


import tkinter as tk
from tkinter import ttk

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import pandas as pd
from xlrd import open_workbook
file=None
p=None
q=None
qq=[]
qw=[]
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
def putinfo(string):
      global file
      file=string
      predict()
def predict():
            ###########normalization###################################
            def normalization(x):
                df=pd.DataFrame()
                for i in range(len(x.columns)):
                    df[i]=(x.iloc[:,i])/(np.max(x.iloc[:,i]))
                return df
            #################Activation function#########################
            def linear(x,a=1,derivative=False):
                if derivative==True:
                    return np.full((len(x), 1), a,dtype=np.float64)
                return a*x

            def sigmoid(x, derivative=False):
                if (derivative == True):
                    return x* (1 - x)
                return 1 / (1 + np.exp(-x))

            def tanh(x, derivative=False):
                if (derivative == True):
                    return (1 - (x ** 2))
                return np.tanh(x)
            ##################weight initialization#######################
            lr=0.12
            epoch=1000
            hiddenlayers=4
            activation=[locals()['sigmoid'],locals()['tanh'],locals()['sigmoid'],
                        locals()['tanh'],locals()['linear']]

            def initilization(inputsize,hiddenlayers):
                weights=[]
                bias=[]
                hiddenlayer_neurons=[6,7,8,9,1]
                np.random.seed(7)
                for i in range((hiddenlayers+1)):
                    #weight and bias initialization
                    if i==0:
                        wh=np.random.randn(inputsize,hiddenlayer_neurons[i])
                        bh=np.random.randn(1,hiddenlayer_neurons[i])
                        weights.append(wh)
                        bias.append(bh)
                    else:
                        wh=np.random.randn(hiddenlayer_neurons[i-1],hiddenlayer_neurons[i])
                        bh=np.random.randn(1,hiddenlayer_neurons[i])
                        weights.append(wh)
                        bias.append(bh)
                return weights,bias
            #######################forward propagation
            def forward(x,weights,bias,hiddenlayers):
                hiddenlayer_output=[]
                z=(np.dot(x,weights[0]))
                z=z+bias[0]
                z2=activation[0](z,derivative=False)
                hiddenlayer_output.append(z2)
                for i in range(hiddenlayers):
                    z3=(np.dot(hiddenlayer_output[i],weights[i+1]))
                    z3=z3+bias[i+1]
                    z4=activation[i+1](z3,derivative=False)
                    hiddenlayer_output.append(z4)
                return hiddenlayer_output
            ##################Back propagation
            def Backpropagation(x_train,y_train,hiddenlayer_output,hiddenlayers,lr):
                delta=[]
                error=(1/len(y_train))*np.sum(np.square(y_train-hiddenlayer_output[-1]))   
                #print(error)
                output_error=-(2/len(y_train))*(y_train-hiddenlayer_output[-1])
                output_delta=output_error*activation[-1](hiddenlayer_output[-1],derivative=True)
                delta.append(output_delta)
                for j in range(hiddenlayers,0,-1):
                    Error_at_hidden_layer=delta[hiddenlayers-j].dot(weights[(j-1)-hiddenlayers].T)
                    d_hiddenlayer=Error_at_hidden_layer*activation[-(2+(hiddenlayers-j))](hiddenlayer_output[-(2+(hiddenlayers-j))],derivative=True)
                    delta.append(d_hiddenlayer)
                weights[0] -=(x_train.T.dot(delta[-1]))*lr
                bias[0] -=np.sum(delta[-1],axis=0,keepdims=True)*lr
                for j in range(1,(hiddenlayers+1)):
                    weights[j] -=(hiddenlayer_output[j-1].T.dot(delta[-j-1]))*lr
                    bias[j] -=(np.sum(delta[-(2+(j-1))],axis=0,keepdims=True))*lr
                return weights,bias

            x=pd.read_csv(file)
            x=x.drop(x.columns[0:1],axis=1)
            y_max=max(x.iloc[:,2])
            x=normalization(x)
            y=x.iloc[:,2]
            y=y.shift(-1)
            x=x.drop(x.columns[2],axis=1)
            inputsize=len(x.columns)
            test_s=0.2
            stop=len(x)-round(len(x)*test_s)
            x_train=np.array(x[:stop])
            x_test=np.array(x[stop:])
            y_train=np.array([y[:stop]]).T
            y_test=np.array(y[stop:])

            weights,bias=initilization(inputsize,hiddenlayers)
            def training(x_train,y_train,w,b,hiddenlayer,epoch):
                    for i in range(epoch):
                        hiddenlayer_output=forward(x_train,w,b,hiddenlayers)
                        w,b=Backpropagation(x_train,y_train,hiddenlayer_output,hiddenlayers,lr)
                    return hiddenlayer_output,w,b

            hiddenlayer_output,w,b=training(x_train,y_train,weights,bias,hiddenlayers,epoch)
            df1,df2=[],[]
            for wts in w:
                df1.append(pd.DataFrame(wts))
            for bs in b:
                df2.append(pd.DataFrame(bs))

            dfs={}
            k=0
            for i,j in zip(df1,df2):
                dfs.update({'weights'+str(k):i})
                dfs.update({'bias'+str(k):j})
                k=k+1
            writer = pd.ExcelWriter('Tcsweights.xlsx', engine='xlsxwriter')
            for sheet_name in dfs.keys():
                dfs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
                
            writer.save()

            def predict(x,w,b):
                result=forward(x,w,b,hiddenlayers)
                return result[-1]
            pred=predict(x_test[:-2],w,b)
            global p
            p=pred*y_max
            global q
            i=1
            global qq
            global qw
            qw=y_test*y_max
            for s in p:
                for q in s:
                    qq.append(q)
                    i=i+1
            print(i)
            '''
            print("predicted output:\n"+str(p))
            print("actual output:\n"+str(y_test*y_max))
            print("predict "+str(qq))'''
            y_act=y_test*y_max
            #test_error=MSE(y_test[:-2],pred,len(y_test),derivative=False)
            heo()
'''
def heo():
            class Ui_Form(QMainWindow):
                he=None
                predict()
                def train_model(self):
                                 from train_model import Ui_Form
                                 self.qMainWindow = QtWidgets.QMainWindow()
                                 self.ui = Ui_Form()
                                 self.ui.setupUi(self.qMainWindow)
                                 self.hide()
                                 self.qMainWindow.show()      

                               
                def __init__(self):
                    super().__init__()
                    self._main = QtWidgets.QWidget()
                    self.setCentralWidget(self._main)
                    self.setObjectName("Form")
                    self.resize(1141, 629)
                    self.setStyleSheet("#Form\n"
            "{\n"
            "background:url(img/bg1.jpg) no-repeat center center fixed;\n"
            "}\n"
            "QFrame\n"
            "{\n"
            "background:#F1F1F1;\n"
            "border-radius:30px;\n"
            "\n"
            "}\n"
            "#frame_2{\n"
            "background:dodgerblue;\n"
            "border-radius:30px;\n"
            "\n"
            "}\n"
            "#label{\n"
            "background:dodgerblue;\n"
            "font-size:30px;\n"
            "}\n"
            "#label_2{\n"
            "background:dodgerblue;\n"
            "font-size:15px;\n"
            "}\n"
            "#label_3{\n"
            "background:dodgerblue;\n"
            "font-size:20px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "background:dodgerblue;\n"
            "border-radius:30px;\n"
            "\n"
            "}")
                    self.frame = QtWidgets.QFrame(self)
                    self.frame.setGeometry(QtCore.QRect(40, 50, 1051, 521))
                    self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.frame.setObjectName("frame")
                    self.frame_2 = QtWidgets.QFrame(self.frame)
                    self.frame_2.setGeometry(QtCore.QRect(10, 10, 1001, 61))
                    self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.frame_2.setObjectName("frame_2")
                    self.label = QtWidgets.QLabel(self.frame_2)
                    self.label.setGeometry(QtCore.QRect(40, 10, 561, 41))
                    self.label.setObjectName("label")
                    self.label.setText("STOCK PREDICTION USING ML")
                    self.label_2 = QtWidgets.QLabel(self.frame_2)
                    self.label_2.setGeometry(QtCore.QRect(520, 30, 151, 20))
                    self.label_2.setObjectName("label_2")
                    self.label_2.setText("Developed By :-")
                    self.label_3 = QtWidgets.QLabel(self.frame_2)
                    self.label_3.setGeometry(QtCore.QRect(630, 20, 201, 41))
                    self.label_3.setObjectName("label_3")
                    self.label_3.setText("Abhay Bhadouriya")
                    self.pushButton = QtWidgets.QPushButton(self.frame_2)
                    self.pushButton.setGeometry(QtCore.QRect(910, 0, 75, 61))
                    self.pushButton.setText("")
                    
                    self.widget1 = QtWidgets.QWidget()
                    self.widget1.setGeometry(QtCore.QRect( 100,150, 1001, 500))
                    self.widget1.setObjectName("widget")
                    
                    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
                 
                    vlay = QVBoxLayout(self.widget1)
                    self.setCentralWidget(self.widget1)
                    vlay.addWidget(static_canvas)
                    static_canvas.setFixedWidth(1001)
                    static_canvas.setFixedHeight(400)
                    vlay.setAlignment(static_canvas, Qt.AlignCenter)

                    #self._static_ax = static_canvas.figure.subplots()
                    #t = np.linspace(1, 1000, 10)
                    #self._static_ax.plot(t, np.tan(t), ".")
                    self._static_ax= static_canvas.figure.subplots()
                    #t = np.linspace(1,249000, 249)
                    t=[]
                    j=250
                    for i in qw:
                        t.append(1000)
                    self._static_ax.plot(qw, 'r-', label = "Actual Output")
                    self._static_ax.legend()
                    self._static_ax.plot(qq, 'g-', label = "Predicted Output")
                    self._static_ax.legend()

                    self._static_ax.figure.canvas.draw()
                    
                    
                      
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.pushButton.setIcon(icon)
                    self.pushButton.setIconSize(QtCore.QSize(50, 50))
                    self.pushButton.setObjectName("pushButton")

                    self.pushButton.clicked.connect(self.train_model)

          
            class WidgetPlot(QWidget):
                def __init__(self, *args, **kwargs):
                    QWidget.__init__(self, *args, **kwargs)
                    self.setLayout(QVBoxLayout())
                    self.canvas = PlotCanvas(self, width=10, height=8)
                    self.toolbar = NavigationToolbar(self.canvas,self)
                    self.layout().addWidget(self.toolbar)
                    self.layout().addWidget(self.canvas)

            class PlotCanvas(FigureCanvas):
                def __init__(self, parent=None, width=10, height=8, dpi=100):
                    fig = Figure(figsize=(width, height), dpi=dpi)
                    FigureCanvas.__init__(self, fig)
                    self.setParent(parent)
                    FigureCanvas.setSizePolicy(self, 900, 500)
                    FigureCanvas.updateGeometry(self)
                    self.plot()

                def plot(self):
                    data = [random.random() for i in range(250)]
                    ax = self.figure.add_subplot(111)
                    ax.plot(data, 'r-', linewidth = .5)
                    ax.set_title('PyQt Matplotlib Example')
                    self.draw()




            if __name__ == "__main__":
                        import sys
                        app =QApplication(sys.argv)
                        MainWindow = Ui_Form()
                        MainWindow.show()
                        sys.exit(app.exec_())
             
'''
def heo():
            root = tkinter.Tk()

            fig = Figure(figsize=(5, 4), dpi=100)
            t = np.arange(0, 3, .01)
            fig.add_subplot(111).plot(qw, 'r-', label = "Actual Output")
            fig.add_subplot(111).legend()
            fig.add_subplot(111).plot(qq, 'b-', label = "Predicted Output")
            fig.add_subplot(111).legend()

            canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

            toolbar = NavigationToolbar2Tk(canvas, root)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)


            canvas.mpl_connect("key_press_event", on_key_press)


            def _quit():
                root.quit()     # stops mainloop
                root.destroy()  # this is necessary on Windows to prevent
                                # Fatal Python Error: PyEval_RestoreThread: NULL tstate


            button = tkinter.Button(master=root, text="Quit", command=_quit)
            button.pack(side=tkinter.BOTTOM)

            tkinter.mainloop()
