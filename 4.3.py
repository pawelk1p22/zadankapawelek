# zadanie_4_3.py
import math
import matplotlib.pyplot as plt

a = b = 200
r = 200

with open("punkty.txt") as f:
    points = [tuple(map(int, line.split())) for line in f]

def estimate_pi(n):
    inside = 0
    for i in range(n):
        x, y = points[i]
        if (x - a)**2 + (y - b)**2 < r**2:
            inside += 1
    return 4 * inside / n

epsilons = []
for n in range(1, 1701):
    pi_n = estimate_pi(n)
    eps = abs(math.pi - pi_n)
    epsilons.append(eps)

# wykres
plt.figure(figsize=(8, 4))
plt.plot(range(1, 1701), epsilons, color='blue')
plt.xlabel("n")
plt.ylabel("εn")
plt.title("Błąd bezwzględny przybliżenia liczby π")
plt.grid(True)
plt.tight_layout()
plt.savefig("wykres_4_3.png")

with open("wyniki_4.txt", "a") as out:
    out.write("4.3\n")
    out.write(f"ε1000 = {round(epsilons[999],4)}\n")
    out.write(f"ε1700 = {round(epsilons[1699],4)}\n")
