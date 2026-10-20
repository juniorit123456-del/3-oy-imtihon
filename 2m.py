a = {"olma": 5000, "banan": 12000}
b = {"banan": 15000, "anor": 10000}

n = dict(set(a.items()).union(set(b.items())))

print(n)