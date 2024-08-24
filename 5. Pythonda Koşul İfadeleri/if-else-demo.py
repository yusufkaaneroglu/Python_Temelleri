# isim = input('isminiz: ')
# yas = int(input('yaşınız: '))
# egitim = input('eğitim: ')

# if (yas>=18):
#     if (egitim=='lise'or egitim=='üniversite'):
#          print(f'{isim} ehliyet alabilirsin.')
#     else:
#         print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
# else:
#     print(f'{isim} Ehliyet alamazsın yaşın tutmuyor.')

#2)
# yazili1 = float(input('1. yazılı: '))
# yazili2 = float(input('2. yazılı: '))
# sözlü = float(input('Sözlü: '))

# ortalama = (yazili1 + yazili2 + sözlü)/3

# if (ortalama>=0) and (ortalama<25):
#     print(f'ortalama: {ortalama} notunuz: 0')
# elif (ortalama>=25) and (ortalama<45):
#     print(f'ortalama: {ortalama} notunuz: 1')
# elif (ortalama>=45) and (ortalama<55):
#     print(f'ortalama: {ortalama} notunuz: 2')
# elif (ortalama>=55) and (ortalama<70):
#     print(f'ortalama: {ortalama} notunuz: 3')    
# elif (ortalama>=70) and (ortalama<85):
#     print(f'ortalama: {ortalama} notunuz: 4')
# elif (ortalama>=85) and (ortalama<=100):
#     print(f'ortalama: {ortalama} notunuz: 5')
# else:
#     print('yanlış bilgi girdiniz.')

#3)
import datetime

tarih = (input('Aracınız hangi tarihte trafiğe çıktı (2018/8/9): '))
tarih =  tarih.split("/")
print(tarih[0])
print(tarih[1])
print(tarih[2])



# if  days<= 365:
#     print('1. servis aralığı')
# elif days > 365 and days <= 365*2:
#     print('2. servis aralığı')
# elif days > 365*2 and days <= 365*3:
#     print('3. servis aralığı')
# else:
#     print('Hatalı süre girdi')
