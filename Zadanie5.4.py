import random


class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = 0
    
    def play(self):
        self.liczba_odtworzen += 1
    
    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"


class Serial(Film):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu):
        super().__init__(tytul, rok_wydania, gatunek)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    
    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02d}E{self.numer_odcinka:02d}"


biblioteka = []

biblioteka.append(Film("Pulp Fiction", 1994, "Dramat"))
biblioteka.append(Film("Shrek", 2001, "Animacja"))
biblioteka.append(Film("Matrix", 1999, "Sci-Fi"))
biblioteka.append(Serial("The Simpsons", 1989, "Animacja", 5, 1))
biblioteka.append(Serial("Breaking Bad", 2008, "Dramat", 1, 1))
biblioteka.append(Serial("Friends", 1994, "Komedia", 3, 2))


def get_movies():
    filmy = [item for item in biblioteka if isinstance(item, Film) and not isinstance(item, Serial)]
    return sorted(filmy, key=lambda x: x.tytul)


def get_series():
    seriale = [item for item in biblioteka if isinstance(item, Serial)]
    return sorted(seriale, key=lambda x: x.tytul)


def search(tytul):
    for item in biblioteka:
        if item.tytul.lower() == tytul.lower():
            return item
    return None


def generate_views():
    element = random.choice(biblioteka)
    liczba = random.randint(1, 100)
    element.liczba_odtworzen += liczba


def generate_views_10():
    for _ in range(10):
        generate_views()


def top_titles(n, content_type=None):
    if content_type == "film":
        lista = get_movies()
    elif content_type == "serial":
        lista = get_series()
    else:
        lista = biblioteka
    
    return sorted(lista, key=lambda x: x.liczba_odtworzen, reverse=True)[:n]


# Przykłady użycia:
print("Biblioteka:")
for item in biblioteka:
    print(item)

print("\nTest metody play:")
biblioteka[0].play()
print(f"{biblioteka[0]} ma {biblioteka[0].liczba_odtworzen} odtworzeń")

print("\nFilmy:")
for film in get_movies():
    print(film)

print("\nSeriale:")
for serial in get_series():
    print(serial)

print("\nWyszukiwanie:")
wynik = search("Matrix")
print(f"Znaleziono: {wynik}")

print("\nGenerowanie odtworzeń:")
generate_views_10()

print("\nTop 3 tytuły:")
for item in top_titles(3):
    print(f"{item} - {item.liczba_odtworzen} odtworzeń")

print("\nTop 2 filmy:")
for item in top_titles(2, content_type="film"):
    print(f"{item} - {item.liczba_odtworzen} odtworzeń")