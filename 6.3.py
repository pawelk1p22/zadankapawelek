# zadanie_6_3.py

def find_key_diff(a, b):
    """Zwraca przesunięcie między dwoma literami (A-Z)"""
    return (ord(b) - ord(a)) % 26

with open("dane_6_3.txt", encoding="utf-8") as f:
    pairs = [line.strip().split() for line in f]

wrong = []
for plain, cipher in pairs:
    shifts = [find_key_diff(p, c) for p, c in zip(plain, cipher)]
    if len(set(shifts)) != 1:
        wrong.append(plain)

with open("wyniki_6_3.txt", "w", encoding="utf-8") as out:
    for w in wrong:
        out.write(w + "\n")
