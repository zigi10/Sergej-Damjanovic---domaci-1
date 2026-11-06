# Sistem za obradu rezervacija

## Upotrijebljeni upiti (SQL ekvivalenti)
- `SELECT * FROM reservations WHERE check_in BETWEEN ? AND ?` 
  → implementirano u `CsvDataSource.get_reservations()`
- `SUM(amount) FROM reservations WHERE status = 'confirmed'` 
  → implementirano u `ReservationProcessor.total_revenue()`
- `COUNT(*) FROM reservations WHERE status = 'confirmed'` 
  → implementirano u `ReservationProcessor.active_count()`

## Primijenjeni SOLID principi
- **S (Single Responsibility):** Svaka klasa ima jednu odgovornost:
  - `ReservationProcessor` - obrada logike
  - `CsvDataSource` - čitanje podataka
  - `TextReporter` - formatiranje izvještaja
- **D (Dependency Inversion):** `ReservationProcessor` zavisi od `Protocol`-a (`DataSource`, `Reporter`), ne od konkretnih klasa.

## Ispravke generisanog koda (AI)
1. AI je u početku vratio `DataSource` kao `ABC` sa `@abstractmethod` - ispravljeno u `Protocol` jer zadatak to eksplicitno traži.
2. AI je stavljao `print()` direktno u procesor - izdvojeno u `Reporter` radi razdvajanja odgovornosti.
3. AI nije tipizirao povratne vrijednosti - dodani `-> float`, `-> int`, `-> str` radi čitljivosti i tipova.

## Pokretanje testova
\`\`\`bash
pip install pytest
python -m pytest tests/ -v
\`\`\`