# Dosya açmak ve oluşturmak için open fonksiyonu kullanılır
# Kullanımı : open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu : dosyayı hangi amaçla açtığımız anlamına gelir

#'w' (write) yazma modu. 
#   ** Dosya Konumunda oluşur ** 
#   ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file = open("C:/users/YUSUF KAAN/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding=("utf-8"))
# file.write("Yusuf  Kaan")
# file.close()

#'a' (append) ekleme modu. Dosya yoksa oluşur

# file = open("newfile.txt","a",encoding=("utf-8"))
# file.write("Yusuf Kaan\n")
# file.close()

#'x' (create) oluşturma. Dosya zaten varsa hata verir

# file = open("newfile2.txt","x",encoding=("utf-8"))

#'r' (read) okuma modu. Dosya konumunda yoksa hata verir
