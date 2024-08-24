def sayHello(name= 'user'):
    return 'Hello '+ name

msg =sayHello('Yusuf')
msg =sayHello('Çağan')

print(msg)

def total(num1,num2):
    return num1 + num2

result=total(10,20)
result=total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageYusuf = yasHesapla(2013)
ageÇağan = yasHesapla(2014)
ageFurkan = yasHesapla(2000)

print(ageYusuf,ageFurkan,ageÇağan)

#**********************BOZUK***************************
# def EmekliligeKacYilKaldi(dogumYili, yas, emeklilik):
#     yas = yasHesapla(dogumYili,emeklilik,yas)
#     emeklilik = 65 - yas
# if EmekliligeKacYilKaldi > 0:
#         print(f'emekliliğinize {EmekliligeKacYilKaldi} yıl kaldı.')
# else:
#     print('Zaten emekli oldunuz.')


# EmekliligeKacYilKaldi(1983, 'Ali') 
#**********************BOZUK***************************

def yasHesapla(dogumYili, mevcutYil):
    return mevcutYil - dogumYili

def EmekliligeKacYilKaldi(dogumYili, isim, mevcutYil):
    yas = yasHesapla(dogumYili, mevcutYil)
    emeklilik = 65 - yas
'''''
DOCSTRİNG: Doğum yılınıza göre emekliğinize kaç yıl kaldı
INPUT: Doğum yılı
OUTPUT: Hesaplanan yıl bilgisi 

'''''
if emeklilik > 0:
            print(f'{isim}, emekliliğinize {emeklilik} yıl kaldı.')
else:
            print(f'{isim}, zaten emekli oldunuz.')

# Mevcut yılı manuel olarak giriyoruz
mevcutYil = 2024
EmekliligeKacYilKaldi(1983, 'Ali', mevcutYil)
EmekliligeKacYilKaldi(1950, 'Esma', mevcutYil)
EmekliligeKacYilKaldi(1960, 'Mehmet', mevcutYil)
print(help(EmekliligeKacYilKaldi))