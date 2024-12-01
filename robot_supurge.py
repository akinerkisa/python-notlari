import time

a = "A odası"
b = "B odası"
a_durum = "kirli"
b_durum = "kirli"
a_kirlenme_suresi = time.time() + 10  
b_kirlenme_suresi = time.time() + 10

while True:
    bulunan_oda = a
    print("Oda: ", bulunan_oda, "| Odanın durumu:", a_durum)
    if a_durum == "kirli":
        print(bulunan_oda, "temizleniyor.")
        time.sleep(1)
        a_durum = "temiz"
        print(bulunan_oda, "temizlendi.")
        print("Oda: ", bulunan_oda, "| Odanın durumu:", a_durum)
    elif time.time() >= a_kirlenme_suresi:
        a_durum = "kirli"
        print(bulunan_oda, "kirlendi.")
        a_kirlenme_suresi = time.time() + 10
    print("Oda değiştiriliyor.")
    time.sleep(2)

    bulunan_oda = b
    print("Oda: ", bulunan_oda, "| Odanın durumu:", b_durum)
    if b_durum == "kirli":
        print(bulunan_oda, "temizleniyor.")
        time.sleep(1)
        b_durum = "temiz"
        print(bulunan_oda, "temizlendi.")
        print("Oda: ", bulunan_oda, "| Odanın durumu:", b_durum)
    elif time.time() >= b_kirlenme_suresi:
        b_durum = "kirli"
        print(bulunan_oda, "kirlendi.")
        b_kirlenme_suresi = time.time() + 10
    print("Oda değiştiriliyor.")
    time.sleep(2)
