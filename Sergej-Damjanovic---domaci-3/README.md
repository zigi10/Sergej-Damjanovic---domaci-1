# Zadatak 3 – Mini okvir za ML eksperimente

**Predmet:** Napredno programiranje  
**Student:** Sergej Damjanović  
**Indeks:** 26/004  
**Fakultet:** FIST, UDG  
**Vrijednost zadatka:** 6 bodova

## Opis

Cilj ovog zadatka je bio da se implementira jednostavan Python okvir za izvođenje eksperimenata mašinskog učenja na Iris skupu podataka. Implementacija se oslanja na projektne šablone kako bi se postigla fleksibilnost pri zamjeni modela i metrika bez potrebe za refaktorisanjem cijelog koda.

## Korišćeni šabloni

- **Factory** (`models.py`) – klasa `ModelFactory` služi za kreiranje instanci modela (logistička regresija, decision tree, kNN) na osnovu proslijeđenog imena.
- **Strategy** (`metrics.py`) – konkretne strategije (`AccuracyStrategy`, `F1Strategy`, itd.) se proslijeđuju kontekstu (`MetricContext`) kako bi se dinamički birala metrika za evaluaciju.
- **Observer** (`observers.py`) – subjekat (`TrainingSubject`) šalje notifikacije svim registrovanim pretplatnicima (npr. `ConsoleObserver`, `HistoryObserver`) o fazama treniranja.
- **Template Method** (`experiment.py`) – bazna klasa `Experiment` definiše skelet algoritma (priprema, treniranje, evaluacija), dok podklase poput `ClassificationExperiment` mogu dopuniti specifične korake.
- **Decorator** (`decorators.py`) – `TimeDecorator` proširuje funkcionalnost eksperimenta mjerenjem vremena izvršavanja bez direktnog mijenjanja njegove klase.

## Dijagram klasa (Mermaid)
```mermaid
classDiagram
    class ModelFactory
    class MetricStrategy
    class AccuracyStrategy
    class F1Strategy
    class PrecisionStrategy
    class MSEStrategy
    class MetricContext
    class TrainingObserver
    class ConsoleObserver
    class HistoryObserver
    class TrainingSubject
    class Experiment
    class ClassificationExperiment
    class RegressionExperiment
    class TimeDecorator
    MetricStrategy <|-- AccuracyStrategy
    MetricStrategy <|-- F1Strategy
    MetricStrategy <|-- PrecisionStrategy
    MetricStrategy <|-- MSEStrategy
    MetricContext --> MetricStrategy
    TrainingObserver <|-- ConsoleObserver
    TrainingObserver <|-- HistoryObserver
    TrainingSubject --> TrainingObserver
    Experiment <|-- ClassificationExperiment
    Experiment <|-- RegressionExperiment
    TimeDecorator --> Experiment
    ClassificationExperiment ..> ModelFactory

#Pokretanje

Za pokretanje projekta, u terminalu ući u folder `Sergej-Damjanovic---domaci-3` i izvršiti:

```bash
pip install -r requirements.txt
python main.py

Testovi se pokreću komandom:
pytest tests/ -v

Izlaz iz programa prikazuje faze treniranja, izmjereno vrijeme i tačnost modela. Korišten je random_state=42 kako bi podjela podataka bila deterministička.

#koriscenje aija

AI alat je korišćen kao asistent pri strukturiranju projekta i generisanju početnog koda za implementaciju šablona. Tražio sam da se kod drži principa obrađenih na predavanjima.
Kod Strategy šablona, razmatrao sam opciju korišćenja rječnika naspram hijerarhije klasa. Odlučio sam se za klase jer to bolje demonstrira polimorfizam i olakšava dodavanje novih metrika u budućnosti.
Iako su testovi i osnovna struktura generisani uz pomoć AI-a, svaki dio koda je ručno analiziran, testiran i pokrenut lokalno kako bi se verifikovala ispravnost. AI je poslužio kao ubrzanje, ali finalna logika i provjera su urađeni ručno.