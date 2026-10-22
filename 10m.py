import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

plt.plot(kunlar,daromad, color='black', label="Statistika")
plt.title("Bir haftalaik daraomad:")
plt.xlabel("Kunlar")
plt.ylabel("Daromad")
plt.grid(True)
plt.legend()
plt.savefig('daromad.png')