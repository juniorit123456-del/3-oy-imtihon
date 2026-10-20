import csv

with open("mahsulotlar.csv", 'w', newline='') as f:
    mahsulotlar = [
        ["nomi","narxi","miqdori"],
        ["Olma", 8000, 12],
        ["Non", 4000, 20],
        ["Sut", 14000, 5]
        ]
    data = csv.writer(f)
    for i in mahsulotlar:
        data.writerow(i)