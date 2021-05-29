
import json 
   
# VERI

def ayarlariKaydet(esikdeger,tresh,focus,isik,kamera_acisi):
    ayarlar ={"esikdeger": esikdeger,"tresh": tresh,"focus":focus,"isik": isik,"kamera_acisi":kamera_acisi}
    ayarlar=json.dumps(ayarlar)
    with open("ayarlar.json", "w") as outfile: 
        outfile.write(ayarlar)
    return True

