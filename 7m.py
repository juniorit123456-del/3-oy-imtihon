import csv

with open("mahsulotlar.csv", "w", newline="", encoding="utf-8") as f:
    mahsulotlar = [
        ["nomi", "narxi", "miqdori"],
        ["Olma", 8000, 12],
        ["Non", 4000, 20],
        ["Sut", 14000, 5]
    ]

    data = csv.writer(f)
    data.writerows(mahsulotlar)