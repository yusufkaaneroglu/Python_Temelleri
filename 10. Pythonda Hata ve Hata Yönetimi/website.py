website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1. Soru
# result = 'Hello World'.strip() 
# # result = " Hello World ".lstrip() 
# # result = " Hello World ".rstrip() 
# print(result)

# #2. Soru
# result = website.lstrip('/:pth')  # 'www.sadikturan.com'
# print(result)

# #3. Soru 
# result="www.sadikturan.com".strip("w.moc")
# print(result)

# #4. Soru
# course=course.lower()
# print(course)

#5. Soru
# result=website.count('a')
# result=website.count("www")
# result=website.count("www",0,10)
# print(result)

#6. Soru
# result=website.startswith("www")
# result=website.endswith("com")
# print(result)

#7. Soru
# result=website.find(".com")
# result=website.find(".com",0,10)
# result=course.find("Python")
# result=course.rfind("Python")

# result=website.index("com")
# result=website.rindex("com")
# result=website.rindex("comm") #exception
# print(result)

#8. Soru
# result=course.isalpha()
# result="Hello".isalpha()
# result=course.isdigit()
# result="1235456".isdigit()
# print(result)

#9. Soru
# result= "Contents".center(50,"*")
# result= "Contents".ljust(50,"*")
# result= "Contents".rjust(50,"*")
# print(result)

#10. Soru
# Result=course.replace(" ","-")
# Result=course.replace(" ","-",5)
# Result=course.replace(" ","")
# print(Result)

#11. Soru
# result="Hello World".replace("World","There")
# print(result)

#12. Soru
result=course.split(" ")
print(result)