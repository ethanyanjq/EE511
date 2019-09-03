# -*- coding: utf-8 -*-


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
    if (iterations == 1):
        runs = longest_run(rational_result)
        ui.textBrowser.append("The longest run of heads is %d" %(max(runs)))
        f = 0
        freq = []
        for i in range(len(rational_result)):
            if (rational_result[i] >= (1 - prob)):
                f += 1
            freq.append(f/(i+1))
        binary_list = freq
    return binary_list
    
def longest_run(data):
    i = j = 0
    result = []
    while(i<len(data) and j<len(data)):
        if (round(data[i]) == 1):
            j = i+1
            counts = 1
            while (j<len(data)):
                if (round(data[j]) == 1):
                    counts += 1
                    j += 1
                else:
                    i = j
                    break
            result.append(counts)
        else:
            i += 1
    return result

class MainWindow(QMainWindow, Ui_MainWindow, PyPlot):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.radioButton_4.isChecked()):
            self.PyPlot.clear_plot()
            specified_num = int(self.lineEdit_4.text())
            k = i = 0
            while (i<=100000 and k<specified_num):
                random_num = np.random.uniform()
                if (random_num>=0.5): k += 1
                i += 1
            else:
                self.textBrowser.append("Reached user-specified number of head after %d times of tossing" %(i))
        else:
            self.PyPlot.clear_plot()
            times = int(self.lineEdit.text())
            prob = 1-float(self.lineEdit_2.text())
            iterations = int(self.lineEdit_3.text())
            if ((self.radioButton.isChecked() )or self.radioButton_2.isChecked()):
                head_array = flip_coin(iterations, times, prob)
                if (iterations == 1):
                    self.PyPlot.plot(head_array)
                else:
                    self.PyPlot.plot_hist(head_array, times)
            elif(self.radioButton_3.isChecked()):
                flip_100times = np.random.rand(100)
                array1 = longest_run(flip_100times)
                self.PyPlot.plot_hist(array1, 100)
            
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.PyPlot.clear_plot()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.textBrowser.clear()
        
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.on_pushButton_2_clicked()        
        self.lineEdit_2.setText("0.8")
        self.lineEdit_2.setReadOnly(True)
        
    @pyqtSlot()
    def on_radioButton_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit.setText("50")
        self.lineEdit.setReadOnly(True)
        
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit_3.setText("1")
        self.lineEdit.setText("100")
        self.lineEdit_2.setText("0.5") 
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        
    
    @pyqtSlot()
    def on_radioButton_4_clicked(self):
        self.on_pushButton_2_clicked()
        self.lineEdit_4.setText("Input user-specified number of heads here")
        self.textBrowser.append("Input user-specified number and click 'Generate'")
        self.textBrowser.append("You don't need to fill in the blanks on the right")


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

