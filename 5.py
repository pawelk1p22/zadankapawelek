# zadanie_5.py
from collections import defaultdict

# --- wczytanie danych ---
students = {}  # pesel -> (nazwisko, imię)
with open("studenci.txt", encoding="utf-8") as f:
    next(f)
    for line in f:
        pesel, nazw, imie = line.strip().split()
        students[pesel] = (nazw, imie)

rooms = {}  # pesel -> id_pok
with open("meldunek.txt", encoding="utf-8") as f:
    next(f)
    for line in f:
        pesel, pok = line.strip().split()
        rooms[pesel] = pok

borrows = defaultdict(list)  # pesel -> [tytuły]
with open("wypozyczenia.txt", encoding="utf-8") as f:
    next(f)
    for line in f:
        _, pesel, title = line.strip().split(maxsplit=2)
        borrows[pesel].append(title)

with open("wyniki_5.txt", "w", encoding="utf-8") as out:
    # --- 5.1 ---
    max_pesel = max(borrows, key=lambda p: len(borrows[p]))
    nazw, imie = students[max_pesel]
    out.write("5.1\n")
    out.write(f"{imie} {nazw}\n")
    for t in borrows[max_pesel]:
        out.write(f"{t}\n")

    # --- 5.2 ---
    rooms_count = defaultdict(int)
    for pesel in rooms:
        rooms_count[rooms[pesel]] += 1
    avg = sum(rooms_count.values()) / len(rooms_count)
    out.write("5.2\n")
    out.write(f"{avg:.4f}\n")

    # --- 5.3 ---
    women = men = 0
    for pesel in students:
        if int(pesel[-2]) % 2 == 0:
            women += 1
        else:
            men += 1
    out.write("5.3\n")
    out.write(f"Kobiety: {women}, Mężczyźni: {men}\n")

    # --- 5.4 ---
    not_in_dorm = [
        students[p] for p in students if p not in rooms
    ]
    not_in_dorm.sort()
    out.write("5.4\n")
    for nazw, imie in not_in_dorm:
        out.write(f"{nazw} {imie}\n")

    # --- 5.5 ---
    room_titles = defaultdict(set)
    for pesel, titles in borrows.items():
        if pesel in rooms:
            room = rooms[pesel]
            for t in titles:
                room_titles[room].add(t)
    total_books = sum(len(t) for t in room_titles.values())
    out.write("5.5\n")
    out.write(f"{total_books}\n")
