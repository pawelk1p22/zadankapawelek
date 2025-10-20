# zadanie_4_1.py
import math

a = b = 200
r = 200

with open("punkty.txt") as f:
    points = [tuple(map(int, line.split())) for line in f]

border_points = []
inside_count = 0

for x, y in points:
    dist2 = (x - a)**2 + (y - b)**2
    if dist2 == r**2:
        border_points.append((x, y))
    elif dist2 < r**2:
        inside_count += 1

with open("wyniki_4.txt", "w") as out:
    out.write("4.1\n")
    out.write("Punkty na brzegu koła:\n")
    for x, y in border_points:
        out.write(f"{x} {y}\n")
    out.write(f"Liczba punktów wewnątrz koła: {inside_count}\n")
