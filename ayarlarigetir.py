import json

def ayarlariGetir():
    esikdeger=0
    tresh=0
    focus=0
    isik=0
    with open ("ayarlar.json") as f:
        dosyadaki_veri = f.read()
    ayarlar = json.loads(dosyadaki_veri)
    esikdeger=ayarlar['esikdeger']
    tresh=ayarlar['tresh']
    focus=ayarlar['focus']
    isik=ayarlar['isik']
    print(f'Eşikdeger={esikdeger}, Tresh={tresh}, Focus={focus}, Işık={isik}')
    return esikdeger,tresh,focus,isik
