import json

def cevaplariGetir():
    cevaplar=""
    with open ("cevaplar.json") as f:
        dosyadaki_veri = f.read()
    gelencevaplar = json.loads(dosyadaki_veri)
    cevaplar=gelencevaplar['cevapAnahtari']
    print(cevaplar)
    return cevaplar

def cevaplariKaydet(cevaplar):
    cevaplar ={"cevapAnahtari": cevaplar}
    giden_cevaplar=json.dumps(cevaplar)
    with open("cevaplar.json", "w") as outfile: 
        outfile.write(giden_cevaplar)
    return True
