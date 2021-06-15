import json

def ayarlariGetir():
    esikdeger=0
    tresh=0
    focus=0
    isik=0
    kamera_acisi=False

    with open ("ayarlar.json") as f:
        dosyadaki_veri = f.read()
    ayarlar = json.loads(dosyadaki_veri)
    esikdeger=ayarlar['esikdeger']
    tresh=ayarlar['tresh']
    focus=ayarlar['focus']
    isik=ayarlar['isik']
    kamera_acisi=ayarlar['kamera_acisi']
    # print(f'Eşikdeger={esikdeger}, Tresh={tresh}, Focus={focus}, Işık={isik}, Kameraaçısı={kamera_acisi}')
    return esikdeger,tresh,focus,isik,kamera_acisi
