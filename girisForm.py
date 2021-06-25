from PyQt5.QtWidgets import*
from girisForm_python import Ui_MainWindow
from anaform import MainPage_Anaform
from cevaplarKaydet import MainPage_CevaplariKaydet

class MainPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Test okuma v1")
        stil_dosya_yolu='style/stil.qss'
        styleSheet=open(stil_dosya_yolu,'r').read()
        self.setStyleSheet(styleSheet)
        self.setObjectName('girisForm')
        
       
        self.ui.btnTestOku.clicked.connect(self.testOku)
        self.ui.btnCevapAnahtariOlustur.clicked.connect(self.cevapAnahtariOlustur)
    
    def testOku(self):
        self.testokupenceresi=MainPage_Anaform()
        self.testokupenceresi.exec()    
    def cevapAnahtariOlustur(self):
        self.cevapAnahtariOlusturPenceresi=MainPage_CevaplariKaydet()
        self.cevapAnahtariOlusturPenceresi.exec() 

        

       
        
   