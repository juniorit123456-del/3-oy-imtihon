import json

with open("products.json", "r") as f:
    data = json.load(f)

nom = input("Mahsulot nomi: ")
miqdor = int(input("Yangi miqdor: "))

for mahsulot in data:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = miqdor

        with open("products.json", "w") as f:
            json.dump(data, f)

        print("Yangilandi")
        break
else:
    print("Mahsulot topilmadi")