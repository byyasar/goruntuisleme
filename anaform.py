from PyQt5.QtWidgets import*
from PyQt5.QtGui import QImage,QPixmap,QFont,QIcon
from PyQt5.QtCore import QTimer,pyqtSignal
import cv2
import numpy as np
import utlis
from PIL import Image, ImageDraw, ImageFont
from Anaform_python import Ui_MainWindow
import os
import platform
import ayarlar
import ayarlarigetir
import ayarlarikaydet
from ayarlarpage import SettingsPage


################ RESİM AYARLARI #############
path="1.jpg"
widthImg  =700
heightImg =600
secimSayisi=4
sorusayisi=10
#img = np.zeros((640, 480, 3), np.uint8)
################# CEVAP ANAHATARI ##########
ans=[1, 3, 3, 2, 2, 2, 3, 1, 0, 2, 2, 1, 1, 0, 1, 1, 3, 1, 0,1 ]  
############################################

################# TEST ALANI ###############
y=90
xsol=280
xsag=460
w=132
h=420

############################################
parametreler={}
parametreler=ayarlarigetir.ayarlariGetir()
esikdeger=parametreler[0]
tresh=parametreler[1]
focus=parametreler[2]
isik=parametreler[3]
############################################

################# öĞRENCİ NUMARASI #########
ox=70
oy=105
ow=172
oh=370
############################################

asamalariGoster=False
toogledurum=False
otomatikDurdur=False
################# KAMERA AYARLARI #########
webcamFeed=True
cameraNo=0

cap=cv2.VideoCapture(cameraNo)


############################################


sayac=0
sonbulunanNumara=-1
bulunanNumara=-1
bulunanpuan=-1
sonbulunanpuan=-1

#print(f'Çalışılan işletim sistemi {os.name}')

print(f'Çalışılan işletim sistemi {platform.system()}')


class MainPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Test okuma v1")
        
        self.ayarlarpenceresi=SettingsPage()
        
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.startCam.clicked.connect(self.StartStop)
        self.controlTimer()
        
        self.ui.btnAsamalar.clicked.connect(self.asamalarGosterGizle)      
        self.ui.btnOtomatikDurdur.clicked.connect(self.otomatikDurdur)
        self.ui.btnAyarlar.clicked.connect(self.ayarlarPenceresiniAc)
        self.ayarlarpenceresi.new_isik_signal.connect(self.isikDegisti2)
        
        self.ui.lblogrencicevaplar.setStyleSheet("color: blue;"
                        "font-size:12pt;"
                        "background-color: yellow;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;")

    
    def ayarlarPenceresiniAc(self):
        self.ayarlarpenceresi.show()
        self.ayarlarpenceresi.Parametreler(esikdeger,tresh,focus,isik)
        
  
        
    def ayarKaydet(self):
        print(ayarlarikaydet.ayarlariKaydet(esikdeger,tresh,focus,isik))

    def asamalarGosterGizle(self):
        global asamalariGoster
        if asamalariGoster==False:
            asamalariGoster=True
            self.ui.btnAsamalar.setText('Aşamaları Göster')
            self.ui.btnAsamalar.setIcon(QIcon(":/icon/icons/asamagoster.png"))
            
        else:
            asamalariGoster=False
            self.ui.btnAsamalar.setText('Aşamaları Gizle')
            self.ui.btnAsamalar.setIcon(QIcon(":/icon/icons/asamagizle.png"))


    def otomatikDurdur(self):
        global otomatikDurdur
        if otomatikDurdur==False:
            otomatikDurdur=True
            self.ui.btnOtomatikDurdur.setText('Otomatik Durdur Açık')
            self.ui.btnOtomatikDurdur.setIcon(QIcon(":/icon/icons/autooff.png"))
            
        else:
            otomatikDurdur=False
            self.ui.btnOtomatikDurdur.setText('Otomatik Durdur Kapalı')
            self.ui.btnOtomatikDurdur.setIcon(QIcon(":/icon/icons/autoon.png"))

      
    def isikDegisti2(self,_esikdeger,_tresh,_focus,_isik):
        global esikdeger,tresh,focus,isik
        esikdeger=_esikdeger
        tresh=_tresh
        focus=_focus
        isik=_isik
        
        print(f'ayarlardan gelen değerler {_esikdeger,_tresh,_focus,_isik}')
        
    
    
    # view camera
    def viewCam(self):
        # read image in BGR format
        global cap,path,focus,asamalariGoster
        #print('isik',isik)
        cap.set(10,isik)
        cap.set(28,focus) #focus ayar
        if cameraNo==-1:
            image=cv2.imread(path)            
        else:
            if webcamFeed:success,image=cap.read()
            else:image=cv2.imread(path)
        
        self.GoruntuIsle(image)
        asamalariGoster=ayarlar.durumKontrol(self,asamalariGoster)
        # self.otomatikDurdur()
        #print(f'durum {asamalariGoster}')
      
    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            global cameraNo
            self.cap = cv2.VideoCapture(cameraNo)
            # start timer
            self.timer.start(20)
            # update control_bt text
            #self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            #self.ui.control_bt.setText("Start")

    def StartStop(self):
        global toogledurum
        if toogledurum==False:
            self.timer.stop()
            self.cap.release()
            toogledurum=True
            self.ui.startCam.setText('Başlat')
            self.ui.startCam.setIcon(QIcon(":/icon/icons/General OCR_32px.png"))
        else:
            self.timer.start()
            toogledurum=False
            self.ui.startCam.setText('Duraklat')
            self.ui.startCam.setIcon(QIcon(":/icon/icons/ocrclose.png"))
        
    def GoruntuIsle(self,img):

        try:
            
            global widthImg,heightImg,ans,x,y,xsag,xsol,w,h,esikdeger,ox,oy,ow,oh,secimSayisi,sorusayisi,sayac,sonbulunanNumara,bulunanNumara,sonbulunanpuan,bulunanpuan
            img2=cv2.resize(img,(widthImg ,heightImg))
            if cameraNo==-1:
                pass
            else:
                pass
                # img2=cv2.rotate(img2, cv2.ROTATE_180)
            imgCountours=img2.copy()
            imageFinal=img2.copy()
            imgBiggestCountours=img2.copy()
            imgGray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
            imgCanny=cv2.Canny(imgBlur,10,50)
            #cv2.imshow("test",imgCanny)
        
            try:
                #FIND ALL COUNTERS
                countours,hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(imgCountours,countours,-1,(0,255,0),10)

                #FIND RECTANGLES
                rectCon=utlis.rectContour(countours)
                biggestContour=utlis.getCornerPoints(rectCon[0])
                #print(biggestContour)
                
                if biggestContour.size!=0:
                    cv2.drawContours(imgBiggestCountours,biggestContour,-1,(0,255,0),20)
                    biggestContour=utlis.reorder(biggestContour)
                    pts1 = np.float32(biggestContour) # PREPARE POINTS FOR WARP
                    pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
                    matrix = cv2.getPerspectiveTransform(pts1, pts2) # GET TRANSFORMATION MATRIX
                    imgWarpColored = cv2.warpPerspective(img2, matrix, (widthImg, heightImg)) # APPLY WARP PERSPECTIVE
                    #cv2.imshow("bulunan",imgWarpColored)
                    #APPLY TRESHOLD

                    imgWarpGray=cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
                    imgThresh=cv2.threshold(imgWarpGray,tresh,255,cv2.THRESH_BINARY_INV)[1]

                    #boxes=utlis.splitBoxes(imgThresh)
                    
                
                

                    crop_imgSol = imgThresh[y:y+h, xsol:(xsol+w)]
                    crop_imgSag = imgThresh[y:y+h, xsag:(xsag+w)]
                    crop_imgOgrenciNu = imgThresh[oy:oy+oh, ox:(ox+ow)]

                    #cv2.imshow("cropped", crop_imgSol)
                    #cv2.imwrite("croppedsol.jpg",crop_imgSol)
                    #cv2.imwrite("croppedsag.jpg",crop_imgSag)

                    boxesSol=utlis.splitBoxes(crop_imgSol)
                    boxesSag=utlis.splitBoxes(crop_imgSag)
                    boxesOgrenciNu=utlis.splitBoxesOgrenciNu(crop_imgOgrenciNu)
                    
                
                    sorusayisi=20
                    #GETTING NOPIXEL VALUES OF EACH
                    myPixelVal=np.zeros((sorusayisi,secimSayisi))
                    
                    myPixelValOgrenciNu=np.zeros((4,10))
                    countC=0
                    countR=0

                    for image in boxesOgrenciNu:
                        totalPixels=cv2.countNonZero(image)
                        myPixelValOgrenciNu[countR][countC]=totalPixels
                        countC+=1
                        if(countC==10):countR+=1;countC=0
                    #print(myPixelValOgrenciNu)
                    
                    countC=0
                    countR=0

                    for image in boxesSol:
                        totalPixels=cv2.countNonZero(image)
                        myPixelVal[countR][countC]=totalPixels
                        countC+=1
                        if(countC==secimSayisi):countR+=1;countC=0
                    #print(myPixelVal)
                    
                    for image in boxesSag:
                        totalPixels=cv2.countNonZero(image)
                        myPixelVal[countR][countC]=totalPixels
                        countC+=1
                        if(countC==secimSayisi):countR+=1;countC=0


                    #FINDING INDEX VALUES OF THE MARKINGS

                    myIndexOgrenciNu=[]
                    for x in range(0,4):
                        arr=myPixelValOgrenciNu[x]
                        #print("arr",arr)
                        myIndexVal=np.where(arr==np.amax(arr))
                        #print(myIndexVal[0])
                        myIndexOgrenciNu.append(myIndexVal[0][0])
                    ogrenciNumarasi=str(myIndexOgrenciNu[0])+str(myIndexOgrenciNu[1])+str(myIndexOgrenciNu[2])+str(myIndexOgrenciNu[3])
                    #print('Öğrenci numarası {}'.format(ogrenciNumarasi))

                
                    #cv2.imshow('mum',utlis.showNumber2(imgWarpColored,myIndexOgrenciNu,4,10,ox,oy,ow,oh))
                    
                    myIndex=[]
                    for x in range(0,sorusayisi):
                        isaretsayisi=0
                        arr=myPixelVal[x]
                        #print("arr-"+str(x),arr)
                        #print('max',np.amax(arr))
                        #print('sayı',np.count_nonzero(arr>esikdeger))
                        isaretsayisi=np.count_nonzero(arr>esikdeger)
                        enfazla=np.amax(arr)
                        if isaretsayisi>1:
                            myIndexVal[0][0]=5  #iki ve dahafazla işaretlenmiş
                        elif esikdeger<enfazla:
                            myIndexVal=np.where(arr==np.amax(arr))
                            #print(np.where(arr==np.amax(arr))[0])
                        else:
                            #pass
                            myIndexVal[0][0]=4
                        #print(myIndexVal[0])
                        myIndex.append(myIndexVal[0][0])
                    #print(myIndex)


                    #GRADING
                    grading=[]
                    for x in range(0,sorusayisi):
                        if myIndex[x]==4:
                            grading.append(4)
                        elif myIndex[x]==5:
                            grading.append(5)
                        elif ans[x]==myIndex[x]:
                            grading.append(1)
                        else:grading.append(0)
                    #print(grading)

                    #SCORE
                    DogrularSay=grading.count(1)
                    YanlislariSay=grading.count(0)+grading.count(5)
                    BoslariSay=grading.count(4)
                    score=(DogrularSay/sorusayisi)*100
                    mesaj='No:'+ogrenciNumarasi+' Puan:'+str(score) +' Doğru:'+str(DogrularSay)+' Yanlış:'+str(YanlislariSay)+' Boş:'+str(BoslariSay)
                    #print(score)

                    #DISPLAY ANSWERS
                    #imgResult=imgWarpColored.copy()
                
                    

                    imgResultSol=imgWarpColored.copy()
                    #imgResultSag=imgWarpColored.copy()
                    #imgResult= imgResult[y:y+h, x:x+w]
                    imgResultNu=utlis.showNumber2(imgResultSol,myIndexOgrenciNu,4,10,ox,oy,ow,oh)
                    imgResultSol=utlis.showAnswers2(imgResultSol,myIndex[0:10],grading[0:10],ans[0:10],10,4,xsol,y,w,h)
                    imgResultSag=utlis.showAnswers2(imgResultSol,myIndex[10:20],grading[10:20],ans[10:20],10,4,xsag,y,w,h)
                    
                    
                    #cv2.imshow("imgResultSag",imgResultSag)

                    imRawDrawingSol=np.zeros_like(imgResultSol) 
                    imgResultNu=utlis.showNumber2(imRawDrawingSol,myIndexOgrenciNu,4,10,ox,oy,ow,oh)
                    imRawDrawingSol=utlis.showAnswers2(imRawDrawingSol,myIndex[0:10],grading[0:10],ans[0:10],10,4,xsol,y,w,h)
                    imRawDrawingSag=utlis.showAnswers2(imRawDrawingSol,myIndex[10:20],grading[10:20],ans[10:20],10,4,xsag,y,w,h)
                    
                    

                    #cv2.imshow("imgResult1",imRawDrawing)
                    #pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
                    #pts2s = np.float32([[0, 0],[w, 0], [0, h],[w, h]]) # PREPARE POINTS FOR WARP
                    invMatrix = cv2.getPerspectiveTransform(pts2, pts1) # GET TRANSFORMATION MATRIX
                


                    # font 
                    font = cv2.FONT_HERSHEY_SIMPLEX 
                    
                    # org 
                    org = (50),(heightImg-20)
                    
                    # fontScale 
                    fontScale = 0.8
                    
                    # Blue color in BGR 
                    #b,g,r,a
                    color = (0,0,0,0) 
                    
                    # Line thickness of 2 px 
                    thickness = 2
                    
                    # Using cv2.putText() method 
                    #cv2.putText(imRawDrawingSol, 'No:'+ogrenciNumarasi+' Puan:'+str(score) +' D:'+str(DogrularSay)+' Y:'+str(YanlislariSay)+' B:'+str(BoslariSay), org, font,fontScale, color, thickness, cv2.LINE_AA,) 
                    
                    
                    imgInvWarp = cv2.warpPerspective(imRawDrawingSol, invMatrix, ((widthImg), heightImg)) # APPLY WARP PERSPECTIVE
                    #cv2.putText(imageFinal,str(score),((widthImg-150),(heightImg-100)),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,255),3)
                    imageFinal=cv2.addWeighted(imageFinal,1,imgInvWarp,1,0)
                    imageFinal=cv2.rectangle(imageFinal, (50,(heightImg-50)), (widthImg-50, (heightImg-10)), (255,255,255), -1)
                    imageFinal=utlis.print_utf8_text(imageFinal,mesaj,color,(widthImg/2-(len(mesaj)*6)),(heightImg-50))

                    imageFinal=cv2.rectangle(imageFinal,(150,25),(600,450),(0,255,255),3,cv2.LINE_AA)
                    #cv2.putText(imageFinal,'Deneme',(50,125),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,255),3)
                    #cv2.imshow("Camera",imageFinal)
                    
                    if asamalariGoster==True:
                        imgBlank=np.zeros_like(img2)
                        imageArray=([img2,imgGray,imgBlur,imgCanny],[imgCountours,imgBiggestCountours,imgWarpColored,imgThresh],[imgResultSag,imageFinal,imgBlank,imgBlank])
                        imgStacked=utlis.stackImages(imageArray,.5)
                        cv2.imshow("imgStacked",imgStacked)


                    genislik=int(widthImg/1.5)
                    yukseklik=int(heightImg/1.5)
                    imageFinal=cv2.resize(imageFinal,(genislik,yukseklik))
                    # imageFinal=cv2.rotate(imageFinal, cv2.ROTATE_180)

                    # print(f'yeni gen-yuk {genislik} {yukseklik}')
                    height, width, channel = imageFinal.shape
                    step = channel * width
                    # create QImage from image
                    qImg = QImage(imageFinal.data, width, height, step, QImage.Format_BGR888)
                    # show image in img_label
                    self.ui.imgCamera_2.setPixmap(QPixmap.fromImage(qImg))

                   

                    ogrenciCevapSikleri=[]
                    ogrenciDogruYanlis=[]
                    cevaplar=[]

                    for i in myIndex:
                        if i==0:ogrenciCevapSikleri.append('A')
                        elif i==1:ogrenciCevapSikleri.append('B')
                        elif i==2:ogrenciCevapSikleri.append('C')
                        elif i==3:ogrenciCevapSikleri.append('D')
                        elif i==4:ogrenciCevapSikleri.append('N')
                        elif i==5:ogrenciCevapSikleri.append('M') 


                    for x in range(0,sorusayisi):
                        if myIndex[x]==ans[x]:ogrenciDogruYanlis.append('D')
                        else:ogrenciDogruYanlis.append('Y')
                    
                    for i in myIndex:
                        cevaplar.append(i)
                        

                    #print(ogrenciCevapSikleri)
                    #print(ogrenciDogruYanlis)
                    # self.ui.imgBulunan.setVisible(False)

                    if otomatikDurdur==True:
                        print(f'otomatik durdurma açık')
                        bulunanNumara=ogrenciNumarasi
                        bulunanpuan=score
                        if sayac<5:
                            print(f'sayac {sayac} bulunanpuan {bulunanpuan} sonbulunan {sonbulunanpuan}')
                            if (sonbulunanpuan==bulunanpuan) and (sonbulunanNumara==bulunanNumara) and (int(sonbulunanNumara)>0):
                                sayac+=1
                            else:
                                sayac=0
                                sonbulunanNumara=bulunanNumara
                                sonbulunanpuan=bulunanpuan
                        else:
                            global toogledurum
                            toogledurum=False
                            # self.StartStop()
                            sayac=0
                            print(f'bulundu ')
                            # print(ogrenciCevapSikleri)
                            # print(ogrenciDogruYanlis)
                    
                            b=''
                            for i in range(len(ogrenciCevapSikleri)):
                                b+=(ogrenciCevapSikleri[i]) 
                            self.ui.lblogrencicevaplar.setPlainText(b)

                            imgResultSag=cv2.resize(imgResultSag,(genislik,yukseklik))
                            # print(f'yeni gen-yuk {genislik} {yukseklik}')
                            height, width, channel = imgResultSag.shape
                            step = channel * width
                            # create QImage from image
                            qImg = QImage(imgResultSag.data, width, height, step, QImage.Format_BGR888)
                            # show image in img_label
                            # self.ui.imgBulunan.setVisible(True)
                            self.ui.imgBulunan.setPixmap(QPixmap.fromImage(qImg))

            except Exception as Hata:
                print('Bulma hatası oluştu :',Hata)
        except Exception as Hata:
            print('Hata oluştu :',Hata)

   