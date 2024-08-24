liste = ["1","2","5a","10b","abc","10","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

while True:
    sayi = input('sayı: ')
    if sayi == 'q': 
        break

    try:
        result = float(sayi)
        print('girdiğiniz sayı: ', result) 
        break
    except ValueError:
        print('geçersiz sayı')
        continue