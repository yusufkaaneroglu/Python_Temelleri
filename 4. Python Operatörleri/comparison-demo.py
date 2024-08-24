#1)
# a = int(input("a: "))
# b = int(input("b: "))

# result= (a > b)
# print(f"a: {a} b: {b} den büyüktür: {result}")

#2)
# vize1= float(input("1. vize: "))
# vize2= float(input("2. vize: "))
# final= float(input("final : "))

# ortalama= (((vize1 + vize2) /2)  * 0.6) + (final * 0.4)

# print(f"not ortalamanız : {ortalama} ve dersten ve dersten geçme durumunuz: {ortalama>=50}")

#3)
# sayi = int(input('sayı: '))

# tekcift = (sayi % 2 == 0)

# print(f"Girilen sayının çift olma durumu: {tekcift}")

#4)
# sayi=int(input('Sayı: '))
# pozitifmi= (sayi > 0)

# print(f"Girilen sayının pozitif olma durumu: {pozitifmi}")

#5)
email = 'email@sadikturan.com'
password = "abc123"

girilenEmail=input('email: ')
girilenPassword=input('parola: ')

isEmail = (email == girilenEmail)
isPassword = (password == girilenPassword)
print(f"Email bilgisi doğrumu: {isEmail} ve parola doğrumu: {isPassword}")


