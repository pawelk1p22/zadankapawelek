import math

def sum_proper_divisors(n):
    # suma dzielników dodatnich mniejszych od n (czyli właściwych)
    if n <= 1:
        return 0
    s = 1  # 1 jest dzielnikiem wszystkich n>1
    root = int(math.isqrt(n))
    for d in range(2, root+1):
        if n % d == 0:
            s += d
            other = n // d
            if other != d and other != n:
                s += other
    # uwaga: gdy n jest kwadratem, dodaliśmy d tylko raz; 1 dodane wcześniej
    return s

def find_associated(a):
    if a <= 1:
        return "NIE"
    s_a = sum_proper_divisors(a)
    b = s_a - 1
    if b <= 1 or b == a:
        return "NIE"
    s_b = sum_proper_divisors(b)
    if s_b == a + 1:
        return b
    else:
        return "NIE"

# przykłady:
for a in [140, 75, 20]:
    print(a, "->", find_associated(a))
# oczekiwane m.in.: 140 -> 195, 75 -> 48
