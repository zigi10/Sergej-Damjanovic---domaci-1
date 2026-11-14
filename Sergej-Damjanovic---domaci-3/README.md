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
    class ModelFactory {
        +create_model
        +list_models
    }
    class MetricStrategy {
        <<abstract>>
        +compute
        +name
    }
    class AccuracyStrategy {
        +compute
        +name
    }
    class F1Strategy {
        +compute
        +name
    }
    class PrecisionStrategy {
        +compute
        +name
    }
    class MSEStrategy {
        +compute
        +name
    }
    class MetricContext {
        +set_strategy
        +evaluate
    }
    class TrainingObserver {
        <<abstract>>
        +on_train_start
        +on_epoch_end
        +on_train_end
    }
    class ConsoleObserver {
        +on_train_start
        +on_epoch_end
        +on_train_end
    }
    class HistoryObserver {
        +on_train_start
        +on_epoch_end
        +on_train_end
        +get_history
    }
    class TrainingSubject {
        +attach
        +detach
        +notify_train_start
        +notify_epoch_end
        +notify_train_end
    }
    class Experiment {
        <<abstract>>
        +run
        +prepare_data
        +create_model
        +train
        +evaluate
        +post_process
    }
    class ClassificationExperiment {
        +__init__
    }
    class RegressionExperiment {
        +__init__
    }
    class TimeDecorator {
        +run
        +execution_time
    }
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

## Pokretanje

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