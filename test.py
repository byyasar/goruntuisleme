import cv2


def list_ports():
    is_working = True
    dev_port = 0
    working_ports = []
    available_ports = []
    while is_working:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            is_working = False
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports,working_ports

list_ports()


'''def closeEvent(self, event):
        close = QMessageBox()
        close.setWindowTitle("Dikkat")
        close.setWindowIcon((QIcon(":/icon/icons/ask.png")))
        close.setText("Programı Kapatmak İstediğinize Emin misiniz?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonYes = close.button(QMessageBox.Yes)
        buttonYes.setText('Evet')
        buttonHayir = close.button(QMessageBox.No)
        buttonHayir.setText('Hayır')
        close = close.exec()
        if close == QMessageBox.Yes:
            event.accept()
            # self.VeritabaniniKapat()
        else:
            event.ignore()'''