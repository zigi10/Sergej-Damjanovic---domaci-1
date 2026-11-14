# Zadatak 3 – Mini okvir za ML eksperimente

**Predmet:** Napredno programiranje
**Student:** Sergej Damjanović
**Indeks:** 26/004
**Fakultet:** FIST, UDG
**Vrijednost zadatka:** 6 bodova

## Opis

Cilj zadatka je bio da se napravi mali Python okvir za pokretanje eksperimenata mašinskog učenja, pri čemu su primijenjeni šabloni obrađeni na predmetu. Kao testni skup korišten je Iris, a kroz okvir je moguće lako mijenjati modele i metrike bez diranja glavne logike.

## Korišćeni šabloni

- **Factory** (`models.py`) – klasa `ModelFactory` kreira logističku regresiju, stablo odlučivanja ili kNN po imenu.
- **Strategy** (`metrics.py`) – klase `AccuracyStrategy`, `F1Strategy`, `PrecisionStrategy` i `MSEStrategy` omogućavaju zamjenu metrike u runtime-u preko `MetricContext`.
- **Observer** (`observers.py`) – `TrainingSubject` šalje obavještenja pretplatnicima (`ConsoleObserver`, `HistoryObserver`) o početku, toku i kraju treniranja.
- **Template Method** (`experiment.py`) – apstraktna klasa `Experiment` definiše redoslijed koraka: priprema podataka, kreiranje modela, treniranje, evaluacija i post-procesiranje. Podklase `ClassificationExperiment` i `RegressionExperiment` dopunjuju korake po potrebi.
- **Decorator** (`decorators.py`) – `TimeDecorator` mjeri trajanje eksperimenta bez izmjene same klase eksperimenta.

## Dijagram klasa (Mermaid)

```mermaid
classDiagram
    class ModelFactory {
        +registry: dict
        +create_model(name) BaseEstimator
        +list_models() list
    }

    class MetricStrategy {
        <<abstract>>
        +compute(y_true, y_pred) float
        +name() str
    }

    class AccuracyStrategy {
        +compute(y_true, y_pred) float
        +name() str
    }

    class F1Strategy {
        +compute(y_true, y_pred) float
        +name() str
    }

    class PrecisionStrategy {
        +compute(y_true, y_pred) float
        +name() str
    }

    class MSEStrategy {
        +compute(y_true, y_pred) float
        +name() str
    }

    class MetricContext {
        -_strategy: MetricStrategy
        +set_strategy(strategy)
        +evaluate(y_true, y_pred) dict
    }

    class TrainingObserver {
        <<abstract>>
        +on_train_start(model_name, dataset_info)
        +on_epoch_end(epoch, metrics)
        +on_train_end(results)
    }

    class ConsoleObserver {
        +on_train_start(model_name, dataset_info)
        +on_epoch_end(epoch, metrics)
        +on_train_end(results)
    }

    class HistoryObserver {
        +history: list
        +on_train_start(model_name, dataset_info)
        +on_epoch_end(epoch, metrics)
        +on_train_end(results)
        +get_history() list
    }

    class TrainingSubject {
        -_observers: list
        +attach(observer)
        +detach(observer)
        +notify_train_start(model_name, dataset_info)
        +notify_epoch_end(epoch, metrics)
        +notify_train_end(results)
    }

    class Experiment {
        <<abstract>>
        +model_name: str
        +metric_context: MetricContext
        +subject: TrainingSubject
        +run(X, y) dict
        +prepare_data(X, y, test_size, random_state)
        +create_model() BaseEstimator
        +train(X_train, y_train)
        +evaluate(X_test, y_test) dict
        +post_process(results) dict
    }

    class ClassificationExperiment {
        +__init__(model_name, metric_strategy)
    }

    class RegressionExperiment {
        +__init__(model_name, metric_strategy)
    }

    class TimeDecorator {
        -_experiment: Experiment
        -_execution_time: float
        +execution_time float
        +run(X_train, y_train, X_test, y_test) dict
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

#pokretanje
U terminalu otvoriti folder Sergej-Damjanovic---domaci-3, pa pokrenuti:

pip install -r requirements.txt
python main.py

Za testove:
pytest tests/ -v
Nakon pokretanja, u konzoli se ispisuje tok treniranja za svaki model zajedno sa izmjerenim vremenom i postignutom tačnošću. Da bi rezultati bili uporedivi između pokretanja, koristi se fiksni seed (random_state=42) pri dijeljenju podataka.

#koriscenje aija

AI alat sam koristio tokom cijelog rada na zadatku, prvenstveno da mi pomogne oko strukture projekta i implementacije šablona koje smo učili na predavanjima. Počeo sam tako što sam tražio prijedlog za organizaciju fajlova, a zatim smo zajedno prolazili kroz svaki šablon — Factory, Strategy, Observer, Template Method i Decorator — i prilagođavali kod tako da bude jasan i funkcionalan.

Za Strategy šablon sam razmišljao da li da idem sa rječnikom funkcija ili sa posebnim klasama. Na kraju sam se odlučio za klase jer mi se činilo da to bolje prati ono što smo radili na času i lakše se može proširiti ako dodam nove metrike.

Testove sam takođe pisao uz pomoć AI-a, ali sam ih poslije ručno provjeravao i pokretao da vidim da li sve radi kako treba. Takođe sam pokrenuo main.py na Iris skupu da se uvjerim da rezultati imaju smisla. AI je bio koristan kao polazna tačka, ali konačno rješenje sam sam pregledao i testirao prije predaje.