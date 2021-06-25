from PyQt5.QtWidgets import QApplication
from girisForm import MainPage

import sys
# import os
# os.system('clear')
app=QApplication([])
window=MainPage()
window.show()
sys.exit(app.exec_())