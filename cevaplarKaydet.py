from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QImage,QPixmap,QFont,QIcon
from PyQt5.QtCore import QTimer, center,pyqtSignal
from cevaplarKaydet_python import Ui_Frame
import cevaplar_islemler





class MainPage_CevaplariKaydet(QDialog):
    
    def __init__(self):
        super().__init__()
    
        self.ui=Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("Test okuma v1")
        txt=cevaplar_islemler.cevaplariGetir()
        txt=txt.upper()
        self.ui.txtCevaplar.setText(txt)
        self.ui.btnKaydet.clicked.connect(self.kaydet)
        stil_dosya_yolu='style/stil.qss'
        styleSheet=open(stil_dosya_yolu,'r').read()
        self.setStyleSheet(styleSheet)

    def kaydet(self):
        try:
            kaydedilecekCevaplar=""
            kaydedilecekCevaplar=self.ui.txtCevaplar.toPlainText()
            cevaplar_islemler.cevaplariKaydet(kaydedilecekCevaplar)

            mesajbox=QMessageBox()
            mesajbox.setIcon(QMessageBox.Information)
            mesajbox.setText('Kaydetme başarılı')
            mesajbox.setWindowTitle('Kaydet')
            mesajbox.setStandardButtons(QMessageBox.Ok)
            mesajbox.setEscapeButton(QMessageBox.Ok)
            buton_tamam=mesajbox.button(QMessageBox.Ok)
            buton_tamam.setText('Tamam')
            stil_dosya_yolu='style/stil.qss'
            styleSheet=open(stil_dosya_yolu,'r').read()
            mesajbox.setStyleSheet(styleSheet)
            mesajbox.exec_()



            # .information(self,'Kaydet','Cevaplar kaydedildi.')

            print('kaydedildi')
        except Exception as Hata:
            print(f'Kaydetme hatası {Hata}')


      
        
             
        # self.ui.bt.clicked.connect(self.asamalarGosterGizle)  
        # self.ui.btnTestOku.clicked.connect(self.testOku)


    # def testOku(self):
    #     self.testokupenceresi.exec()    

        

       
        
   