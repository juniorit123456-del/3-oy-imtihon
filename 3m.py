mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

yangi = input("Yangi mahsulot nomini kiriting: ")
narx = int(input("Mahsulot narxini kiriting: "))
if yangi in mahsulotlar:
    mahsulotlar[yangi] = narx
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi")