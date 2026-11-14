from sklearn.datasets import load_iris
from ml_framework.models import ModelFactory
from ml_framework.metrics import AccuracyStrategy, F1Strategy
from ml_framework.observers import ConsoleObserver, HistoryObserver
from ml_framework.experiment import ClassificationExperiment
from ml_framework.decorators import TimeDecorator


def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    print("=== Dostupni modeli ===")
    print(ModelFactory.list_models())
    print()

    for model_name in ["logistic", "knn", "decision_tree"]:
        print(f"--- Eksperiment: {model_name} ---")

        strategy = AccuracyStrategy() if model_name != "knn" else F1Strategy()
        exp = ClassificationExperiment(model_name, metric_strategy=strategy)

        console = ConsoleObserver()
        history = HistoryObserver()
        exp.subject.attach(console)
        exp.subject.attach(history)

        wrapped_exp = TimeDecorator(exp)
        results = wrapped_exp.run(X, y)

        print(f"Vrijeme izvrsavanja: {results['execution_time']}s")
        print(f"Istorija treninga: {len(history.get_history())} zapisa")
        print()


if __name__ == "__main__":
    main()