import cv2
import numpy as np
import utlis
from PIL import Image, ImageDraw, ImageFont

############################################
path="1.jpg"
widthImg  =700
heightImg =600

secimSayisi=4
sorusayisi=10

#CEVAP ANAHATARI
ans=[1, 3, 3, 2, 2, 2, 3, 1, 0, 2, 2, 1, 1, 0, 1, 1, 3, 1, 0,1 ]  




################# TEST ALANI ###############
y=90
xsol=280
xsag=460
w=132
h=420
esikdeger=200
############################################

################# öĞRENCİ NUMARASI #########
ox=70
oy=105
ow=172
oh=370
############################################

webcamFeed=True
cameraNo=0

cap=cv2.VideoCapture(cameraNo)
cap.set(10,150)
cap.set(28,10) #focus ayar

while True:
    if webcamFeed:success,img=cap.read()
    #if False:img=cv2.imread(path)
    else:img=cv2.imread(path)

    img=cv2.resize(img,(widthImg  ,heightImg))
    img=cv2.rotate(img, cv2.ROTATE_180)
    imgCountours=img.copy()
    imageFinal=img.copy()
    imgBiggestCountours=img.copy()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,10,50)

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
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) # APPLY WARP PERSPECTIVE

            #APPLY TRESHOLD

            imgWarpGray=cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
            imgThresh=cv2.threshold(imgWarpGray,100,255,cv2.THRESH_BINARY_INV)[1]

            #boxes=utlis.splitBoxes(imgThresh)
            #cv2.imshow("test",boxes[1])
        
        

            crop_imgSol = imgThresh[y:y+h, xsol:(xsol+w)]
            crop_imgSag = imgThresh[y:y+h, xsag:(xsag+w)]
            crop_imgOgrenciNu = imgThresh[oy:oy+oh, ox:(ox+ow)]

            #cv2.imshow("cropped", crop_imgOgrenciNu)
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
                print('max',np.amax(arr))
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
            #cv2.putText(imageFinal,'Deneme',(50,125),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,255),3)
            cv2.imshow("Camera",imageFinal)



        imgBlank=np.zeros_like(img)

        imageArray=([img,imgGray,imgBlur,imgCanny],
        [imgCountours,imgBiggestCountours,imgWarpColored,imgThresh]
        ,[imgResultSag,imageFinal,imgBlank,imgBlank]
        )
        imgStacked=utlis.stackImages(imageArray,.5)
        #cv2.imshow("imgStacked",imgStacked)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    except Exception as hata:
        imgBlank=np.zeros_like(img)
        imageArray=([img,imgGray,imgBlur,imgCanny],
        [imgBlank,imgBlank,imgBlank,imgBlank]
        ,[imgBlank,imgBlank,imgBlank,imgBlank]
        )
        imgStacked=utlis.stackImages(imageArray,.5)
        #cv2.imshow("imgStacked",imgStacked)
        cv2.imshow("Camera",img)
        print('hata'+str(hata))
        #break
        #cv2.destroyAllWindows()
    # SAVE IMAGE WHEN 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
            #print("kayıt")
            cv2.imwrite("Final {}.jpg".format(ogrenciNumarasi),imageFinal)
            cv2.waitKey(300)
    
    
        
    

