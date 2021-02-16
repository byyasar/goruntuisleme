import cv2
import numpy as np
from Anaform_python import Ui_MainWindow
from anaform import *

def durumKontrol(self,_durum):
    durum=_durum
    if durum==True:
        asamalariGoster=True
    else:
        asamalariGoster=False
        cv2.destroyAllWindows()
    return asamalariGoster

