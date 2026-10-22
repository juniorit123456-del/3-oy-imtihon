def sonlar_tahlil(juft_yigindi, toq_yigindi, sonlar):
    katta = max(sonlar)

    for i in sonlar:
        if i % 2 == 0:
            juft_yigindi += i
        else:
            toq_yigindi += i

    print(f"Royhatdagi juft sonlar yigindisi: {juft_yigindi}")
    print(f"Royhatdagi toq sonlar yigindisi: {toq_yigindi}")
    print(f"Royhatdagi eng katta son: {katta}")


sonlar = [12, 7, 5, 18, 9, 4]

sonlar_tahlil(0, 0, sonlar)