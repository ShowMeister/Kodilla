zakupy = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

print("Lista zakupów")liczba_produktow = 0

for sklep, produkty in zakupy.items():
    produkty_wielkie = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {produkty_wielkie}.")
    liczba_produktow += len(produkty)