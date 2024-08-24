maasFurkan=5000
maasYusuf=4000
vergi=0.27

print (maasYusuf - (maasYusuf * vergi))
print (maasFurkan - (maasFurkan * vergi))

#Değişken Tanımlama Kuralları

#Rakam ile başlamaz

number1=10
print(number1)
number1=20
print(number1)
number1 +=30
print(number1)

#Büyük Küçük Harf Duyarlılığı

age=20
AGE=30
print(age)
print(AGE)

#Türkçe Karakter Kullanılmaz

yas=20
_age=20

x=1               #int
y=2.3             #float
name = "Çınar "   #string
isStudent = True  #bool

# x, y, name, isStudent, (1, 2.3, "Çınar", True)

a='10'
b='20'
print(a+b) #30 => 1020

firstName= "Yusuf"
secondName= " Kaan"
lastName=" Eroğlu"
print(firstName+secondName+lastName)