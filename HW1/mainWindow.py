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
    for k in iterations:
        rational_result = np.random.rand(times)
        f = 0
        for i in times:
            if (rational_result[i]>=prob):
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
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #if (self.radioButton.isChecked()):
            
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.PyPlot.clear_plot()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
