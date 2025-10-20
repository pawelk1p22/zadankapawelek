# zadanie_6_2.py

def caesar_decrypt(word, k):
    k %= 26
    res = ""
    for ch in word:
        new = chr((ord(ch) - 65 - k) % 26 + 65)
        res += new
    return res

with open("dane_6_2.txt", encoding="utf-8") as f:
    lines = [line.strip().split() for line in f]

with open("wyniki_6_2.txt", "w", encoding="utf-8") as out:
    for word, key in lines:
        out.write(caesar_decrypt(word, int(key)) + "\n")
