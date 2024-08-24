
Sadikhesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap':2000,

} 


Alihesap = {
    'ad': 'Ali Turan',
    'hesapNo': '13245678',
    'bakiye': 2000,
    'ekHesap':1000,

} 

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h): ')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']}")
                print('paranızı alabilirsiniz.')
                print(f"{hesap['hesapNo']} nolu hesabızda {hesap['bakiye']} ₺ bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')            

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} ₺ bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} ₺ bulunmaktadır")
      

paraCek(Sadikhesap, 3000)
bakiyeSorgula(Sadikhesap)

print('***************************')

paraCek(Sadikhesap, 2000)
bakiyeSorgula(Sadikhesap)

