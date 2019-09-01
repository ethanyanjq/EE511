# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import numpy as np

from Ui_mainWindow import Ui_MainWindow
from pyplot import PyPlot

def flip_coin(iterations, times, prob):
    binary_list = []
    for k in range(iterations):
        rational_result = np.random.rand(times)
        f = 0
        for i in rational_result:
            if (i>=prob):
                f += 1
        binary_list.append(f)
    return binary_list

class MainWindow(QMainWindow, Ui_MainWindow, PyPlot):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

    
    @pyqtSlot()
    def on_pushButton_clicked(self):

        self.PyPlot.clear_plot()
        times = int(self.lineEdit.text())
        prob = float(self.lineEdit_2.text())
        iterations = int(self.lineEdit_3.text())
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            head_array = flip_coin(iterations, times, prob)
            self.PyPlot.plot_hist(head_array, times)
        elif(self.radioButton_3.isChecked()):
            flip_100times = np.random.rand(100)
            for i in range(times):
                if (flip_100times[i]>=prob):
                    flip_100times[i] = 1
                else:
                    flip_100times[i] = 0
            self.PyPlot.plot(flip_100times)
        elif(self.radioButton_4.isChecked()):
            
            
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.PyPlot.clear_plot()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.textBrowser.clear()
        
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.on_pushButton_2_clicked()        
        self.lineEdit_2.setText("0.8")
        
    @pyqtSlot()
    def on_radioButton_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit.setText("50")
        
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit_3.setText("1")
        self.lineEdit.setText("100") 
        
    
    @pyqtSlot()
    def on_radioButton_4_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit_4.setText("Input user-specified number of heads here")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
