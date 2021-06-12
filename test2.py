import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # color:#0433ff
        '''
        styleSheet="""background:#0433ff; color:#ffffff"""
        
    
   

        button = QPushButton('PyQt5 button', self)
        button2 = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10,10)
        button2.move(10,30)
        button.clicked.connect(self.on_click)

        label1=QtWidgets.QLabel(self)
        label1.setText("A")
        label1.move(10,50)
        label1.setStyleSheet(styleSheet)'''

        horizontalLayoutWidget = QWidget(self)
        horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        horizontalLayoutWidget.setGeometry(QRect(0, 0, 100, 25))
        horizontalLayout = QBoxLayout(QBoxLayout.Direction.LeftToRight,horizontalLayoutWidget)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
    
      
        styleSheet1="""background:#0433ff; color:#ffffff; font:24 bold"""
        styleSheet2="""background:#F2055C; color:#ffffff; font:24 bold"""

        for i in range(3):  
            dy=i%2
                                                  
            lbl = QtWidgets.QLabel('{}'.format(i +1))
            lbl.setStyleSheet(styleSheet1) if dy==0 else lbl.setStyleSheet(styleSheet2)            
            text =lbl.text()
            horizontalLayout.addWidget(lbl)



       

        '''label0=QtWidgets.QLabel(self)
        label0.setObjectName(u"label0")
        label1=QtWidgets.QLabel(self)
        label1.setObjectName(u"label1")
        for i in range(1):
            # "label"+str(i)=QtWidgets.QLabel(self)
            QtWidgets.QLabel(f"label{i}").setText(" A ")
            QtWidgets.QLabel(f"label{i}").setStyleSheet(styleSheet)
            horizontalLayout.addWidget(QtWidgets.QLabel(f"label{i}"))'''


        '''label1.setText(" A ")
        # label1.move(10,50)
        label1.setStyleSheet(styleSheet)
        horizontalLayout.addWidget(label1)'''
    
       



        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())