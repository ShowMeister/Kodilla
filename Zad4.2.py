def czy_palindrom(wyraz):
    wyraz = wyraz.lower()
    return wyraz == wyraz[::-1]


print(czy_palindrom("kajak"))
print(czy_palindrom("potop"))
print(czy_palindrom("python"))
print(czy_palindrom("Kajak"))
print(czy_palindrom("radar"))
print(czy_palindrom("programming"))