
import json 
   
# VERI

def ayarlariKaydet(esikdeger,tresh,focus,isik):
    ayarlar ={"esikdeger": esikdeger,"tresh": tresh,"focus":focus,"isik": isik}
    ayarlar=json.dumps(ayarlar)
    with open("ayarlar.json", "w") as outfile: 
        outfile.write(ayarlar)
    return True

