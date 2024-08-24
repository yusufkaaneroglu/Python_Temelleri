# import string
# import random

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(characters) for _ in range(length))
# print(generate_password(10))  # Örneğin: `a8Z!r&5xS@`

# outcomes = ['Yazı', 'Tura']
# print(random.choice(outcomes))  # Örneğin: 'Tura'


import random

sayi = random.randint(1, 10)
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz.Toplam Puanınız {100 - (100/can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')

    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')

