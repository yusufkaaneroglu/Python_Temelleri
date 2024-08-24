#1)
arabalar=["Bmw","Mercedes","Opel","Mazda"]
# print(arabalar)
#2)
# result=(len(arabalar))
#3)
# result=arabalar[0]
# result=arabalar[3]
# result=arabalar[-1]
#4)
# arabalar[-1]="Supra MK4"
# result=arabalar
#5)
# result="Mercedes" in arabalar
#6)
# result=arabalar[-2]
# #7)
# result=arabalar[0:3]
# result=arabalar[:3]
#8)
# arabalar[-2:] = ["Toyota","Renault"]
# result=arabalar
#9)
# result = arabalar + ["Audi","Nissan"]
#10)
# del(arabalar[-1])
# result=arabalar
#11)
# result=arabalar[::-1]
#12)
studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan",1998,[80,70,90]]

result=studentA[0]
result=studentB[1]
result=studentC[3][1]
result =f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalamsı {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)