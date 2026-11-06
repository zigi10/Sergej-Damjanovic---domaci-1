# Prosjecna cijena

## Opis projekta

Ovaj projekat predstavlja Python funkciju koja izracunava prosjecnu cijenu na osnovu liste unesenih cijena.

## Funkcionalnosti

- Racunanje prosjecne cijene.
- Provjera da li je lista prazna.
- Prijavljivanje ValueError greske za praznu listu.
- Testiranje funkcije pomocu pytest biblioteke.
- Provjera kvaliteta koda pomocu ruff alata.

## Tehnologije

- Python 3.15
- Visual Studio Code
- pytest
- ruff

## Pokretanje projekta

Instalacija potrebnih biblioteka:

```bash
python -m pip install pytest ruff
```

Pokretanje testova:

```bash
python -m pytest
```

Provjera kvaliteta koda:

```bash
python -m ruff check .
```

## AI upit

Za izradu funkcije koristio/la sam sljedeci upit:

"Napravi Python funkciju prosjecna_cijena koja prima listu cijena i racuna njihovu aritmeticku sredinu. Ako je lista prazna, potrebno je prijaviti ValueError. Napisi i pytest testove koji provjeravaju ispravnost funkcije."

## Uoceni nedostaci generisanog koda

- Funkcija ne provjerava da li su svi elementi liste brojevi.
- Ne provjerava da li su cijene pozitivne.
- Ne obradjuje posebno sve moguce neispravne ulazne podatke.
- Kod je jednostavan i moze se dodatno unaprijediti.

## Autor

Ime i prezime: Sergej Damjanovic
