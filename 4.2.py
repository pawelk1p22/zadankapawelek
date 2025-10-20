# zadanie_4_2.py
import math

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
    return 4 * inside / n  # bo (nk/n) = (πr²)/(4r²) => π ≈ 4·nk/n

pi_1000 = round(estimate_pi(1000), 4)
pi_5000 = round(estimate_pi(5000), 4)
pi_all = round(estimate_pi(len(points)), 4)

with open("wyniki_4.txt", "a") as out:
    out.write("4.2\n")
    out.write(f"pi1000 = {pi_1000}\n")
    out.write(f"pi5000 = {pi_5000}\n")
    out.write(f"pi10000 = {pi_all}\n")
