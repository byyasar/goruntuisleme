from PyQt5.QtWidgets import QApplication
from anaform import MainPage
# import system module
import sys
import os
os.system('clear')
app=QApplication([])
window=MainPage()
window.show()
#app.exec_()
sys.exit(app.exec_())