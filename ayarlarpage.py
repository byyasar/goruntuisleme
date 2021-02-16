from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSignal
from ayarlarPage_python import Ui_Form
import ayarlarikaydet

esikdeger=0
tresh=0
focus=0
isik=0

class SettingsPage(QWidget):

    new_isik_signal=pyqtSignal(int,int,int,int)
    def __init__(self):
        super().__init__()
        
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.sliderEsik.valueChanged.connect(self.esikDegisti)     
        self.ui.sliderTresh.valueChanged.connect(self.treshDegisti)     
        self.ui.sliderFocus.valueChanged.connect(self.focusDegisti)     
        self.ui.sliderIsik.valueChanged.connect(self.isikDegisti)  
        self.ui.btnAyarlariKaydet.clicked.connect(self.ayarKaydet)   
        # self.ui.sliderIsik.setValue(isik)

    def ayarKaydet(self):
        print(ayarlarikaydet.ayarlariKaydet(esikdeger,tresh,focus,isik))

    def isikDegisti(self):
        global isik
        isik=self.ui.sliderIsik.value()
        self.ui.lblIsik.setText('Işık değeri :'+str(isik))
        self.new_isik_signal.emit(esikdeger,tresh,focus,isik)
        #print('isik',isik)
    def focusDegisti(self):
        global focus
        focus=self.ui.sliderFocus.value()
        self.ui.lblFocus.setText('Focus :'+str(focus))
        self.new_isik_signal.emit(esikdeger,tresh,focus,isik)
        #print('focus',focus)
    def treshDegisti(self):
        global tresh
        tresh=self.ui.sliderTresh.value()
        self.ui.lblTresh.setText('Tresh :'+str(tresh))
        self.new_isik_signal.emit(esikdeger,tresh,focus,isik)
        #print('tresh',tresh)
    def esikDegisti(self):
        global esikdeger
        esikdeger=self.ui.sliderEsik.value()
        self.ui.lblEsik.setText('Eşik değeri :'+str(esikdeger))
        self.new_isik_signal.emit(esikdeger,tresh,focus,isik)
        #print('esik',esikdeger)

        
    def Parametreler(self,_esikdeger,_tresh,_focus,_isik):
        global esikdeger,tresh,focus,isik
        esikdeger=_esikdeger
        tresh=_tresh
        focus=_focus
        isik=_isik
        self.ui.sliderEsik.setValue(esikdeger)
        self.ui.lblEsik.setText('Eşik değeri :'+str(esikdeger))
        self.ui.sliderTresh.setValue(tresh)
        self.ui.lblTresh.setText('Tresh :'+str(tresh))
        self.ui.sliderFocus.setValue(focus)
        self.ui.lblFocus.setText('Focus :'+str(focus))
        self.ui.sliderIsik.setValue(isik)
        self.ui.lblIsik.setText('Işık değeri :'+str(isik))
        print(f'gelen isik{_esikdeger,_tresh,_focus,_isik}')

    

