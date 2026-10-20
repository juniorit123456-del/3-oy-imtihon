sonlar = [12, 7, 5, 18, 9, 4]

juft_yigindi = 0
toq_yigindi = 0

for i in sonlar:
    if i % 2 == 0:
        juft_yigindi+=i
    elif  i % 2 == 1:
        toq_yigindi+=i

katta  = max(sonlar)

print(f"Royhatdagi juft sonlar yigindisi: {juft_yigindi}")
print(f"Royhatdagi toq sonlar yigindisi: {toq_yigindi}")
print(f"Royhatdagi eng katta son: {katta}")