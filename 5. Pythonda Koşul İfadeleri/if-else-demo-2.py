#1)
# sayi =(float(input("Sayı:")))
# result = (sayi>=0) and (sayi<=100)
# if result:
#     print(f'girilen sayı 0 ile 100 arasında.')
# else:
#     print('sayı 0 ile 100 arasında değil')

#2)
# sayi = int(input('Sayı:'))

# if (sayi>0): 
#     if((sayi % 2 ==0)):
#         print('Sayı pozitif çift bir sayıdır.')
#     else:
#         print('Sayı pozitif ancak tek.')
# else:
#     print('Sayı negatif sayı.')

#3)
# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# if (girilenEmail == email):
#     if (girilenPassword == password):
#         print('uygulamaya giriş başarılı.')
#     else:
#         print('parolanız yanlış')
# else:
#     print('email bilginiz yanlış.')

#4)
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a > b) and (a > c):
#     print(f'a en büyük sayıdır.')
# elif (b > a) and (b > c):
#     print(f'b en büyük sayıdır.')
# elif (c > a) and (c > b):
#     print(f'c en büyük sayıdır.')

#5)
# vize1 = float(input('vize1: '))
# vize2 = float(input('vize2: '))
# final = float(input('final: '))

# ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)

# result = (ortalama>=50) and (final>=50)
# result = (ortalama>=50) or (final>=70)
### DURUM 1 !!!!
# if (ortalama>=50):
#     if (final>=50):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı.')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız.Finalden en az 50 almalısınız')
#     print('başarılı')
# else:
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız.')
### DURUM 2 !!!
# if (ortalama>=50):
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı.')
# else:
#     if (final>=70):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı.Finalden en az 70 aldığınız için geçtiniz.')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız.')

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

if (index>=0) and (index<=18.4):
    print(f"{name} kilo indeksin {index} ve kilo değerlendirmen zayıf.")
elif (index>18.4) and (index<=24.9):
    print(f"{name} kilo indeksin {index} ve kilo değerlendirmen normal.")
elif (index>24.9) and (index<=29.9):
    print(f"{name} kilo indeksin {index} ve kilo değerlendirmen kilolu.")
elif (index>=29.9) and (index<=34.9):
    print(f"{name} kilo indeksin {index} ve kilo değerlendirmen obez.")





