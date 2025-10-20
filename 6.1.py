# zadanie_6_1.py

def caesar_encrypt(word, k):
    k %= 26
    res = ""
    for ch in word:
        new = chr((ord(ch) - 65 + k) % 26 + 65)
        res += new
    return res

with open("dane_6_1.txt", encoding="utf-8") as f:
    words = [line.strip() for line in f]

with open("wyniki_6_1.txt", "w", encoding="utf-8") as out:
    for w in words:
        out.write(caesar_encrypt(w, 107) + "\n")
