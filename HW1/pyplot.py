import matplotlib       #导入matplotlib 
matplotlib.use("Qt5Agg")     #声明 matplotlib 使用的是Qt5的库
from PyQt5 import QtCore        
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
import numpy as np    #matplotlib 使用 numpy 进行数组运算 因为numpy太长了 取别名为np
import matplotlib.pyplot as plt   #这个是最重要的画图控件
 
class MyMplCanvas(FigureCanvas):   
#MyMplCanvas 继承了FigureCanvas类，主要用来连接Pyqt与matplotlib。
        def __init__(self, parent=None, width=5, height=4, dpi=100): 
            self.fig = plt.Figure(figsize=(width, height), dpi=dpi)  
#建立figure类的对象 flg, Figure可以看做一个画板，所有的图都要画在画板上。
            self.axes = self.fig.add_subplot(111)
#建立对象 axes 这里的 （111）其实是切分图形的方法，可以将一个画板下分隔出很多的小作图区。我们后面详细说
 
            FigureCanvas.__init__(self, self.fig)   #将父类初始化
            self.setParent(parent) 
        
            FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding) 
#这个主要是将后端的绘图功能同Qt的布局管理器衔接上。以免出现布局上的错误。简单的说，就是widget大的时候，图就大，widget小的时候图就跟着小。实时变化要跟下面的代码同时使用。
            FigureCanvas.updateGeometry(self) 
#这个updateGeometry 主要是在widget有改变的时候，绘图跟着改变。不然你widget拖大了，绘图还是那么小。。。
            
class PyPlot(QWidget): 
# 定义Matplotlibwidget类继承了QWidget类，绘图的主代码写在这个类里。
        def __init__(self, parent=None): 
#不指定父子类关系，布局管理器统一管理。
            super(PyPlot, self).__init__(parent)   #继承父类
            self.initUi() 
            
        def initUi(self):   #对绘制的图形进行布局，并生成MyMplCanvas对象。
            self.layout = QVBoxLayout(self) 
            self.mpl = MyMplCanvas(self, width=0, height=0, dpi=100) 
            self.layout.addWidget(self.mpl)
            
        def plot_hist(self, data, times): 
            self.mpl.axes.hist(data, bins = (len(data)), range=(0, times), density=False )
            self.mpl.draw() 

        def plot(self, data):  
            x_array = np.linspace(1, len(data), len(data))
            self.mpl.axes.plot(x_array,data)   
            self.mpl.draw()   
            for i in range(len(data)):
                data[i] = 1 - data[i] 
            self.mpl.axes.plot(x_array,data)   
            self.mpl.draw()    
            
        def clear_plot(self):
            self.mpl.axes.cla()  #清除全部绘图
            self.mpl.draw()
