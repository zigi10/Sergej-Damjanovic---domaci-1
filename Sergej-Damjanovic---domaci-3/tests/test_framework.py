import pytest
import numpy as np
from sklearn.datasets import load_iris
from ml_framework.models import ModelFactory
from ml_framework.metrics import MetricContext, AccuracyStrategy, F1Strategy, MSEStrategy
from ml_framework.observers import TrainingSubject, HistoryObserver, ConsoleObserver
from ml_framework.experiment import ClassificationExperiment
from ml_framework.decorators import measure_time, TimeDecorator


def get_iris_data():
    iris = load_iris()
    return iris.data, iris.target


class TestModelFactory:
    def test_create_logistic_model(self):
        model = ModelFactory.create_model("logistic")
        assert model is not None
        assert hasattr(model, "fit")

    def test_create_knn_model(self):
        model = ModelFactory.create_model("knn", n_neighbors=5)
        assert model is not None

    def test_create_unknown_model_raises(self):
        with pytest.raises(ValueError):
            ModelFactory.create_model("nepoznat_model")

    def test_list_models(self):
        models = ModelFactory.list_models()
        assert "linear" in models
        assert "logistic" in models
        assert "knn" in models


class TestMetrics:
    def test_accuracy_strategy(self):
        y_true = np.array([0, 1, 1, 0])
        y_pred = np.array([0, 1, 0, 0])
        ctx = MetricContext(AccuracyStrategy())
        result = ctx.evaluate(y_true, y_pred)
        assert result["metric"] == "Accuracy"
        assert result["value"] == 0.75

    def test_f1_strategy(self):
        y_true = np.array([0, 1, 1, 0])
        y_pred = np.array([0, 1, 0, 0])
        ctx = MetricContext(F1Strategy())
        result = ctx.evaluate(y_true, y_pred)
        assert result["metric"] == "F1 Score"
        assert 0 <= result["value"] <= 1


class TestObservers:
    def test_history_observer(self):
        subject = TrainingSubject()
        history = HistoryObserver()
        subject.attach(history)
        subject.notify_train_start("logistic", {"n_samples": 150, "n_features": 4})
        subject.notify_epoch_end(1, {"loss": 0.5})
        subject.notify_train_end({"accuracy": 0.95})
        assert len(history.get_history()) == 3


class TestExperiment:
    def test_classification_experiment(self):
        X, y = get_iris_data()
        exp = ClassificationExperiment("logistic")
        console = ConsoleObserver()
        exp.subject.attach(console)
        results = exp.run(X, y)
        assert "value" in results
        assert results["value"] > 0.8

    def test_experiment_with_knn(self):
        X, y = get_iris_data()
        exp = ClassificationExperiment("knn")
        results = exp.run(X, y)
        assert results["value"] > 0.8


class TestDecorator:
    def test_measure_time_decorator(self):
        @measure_time
        def dummy():
            return {"score": 0.9}
        result = dummy()
        assert "execution_time" in result
        assert result["score"] == 0.9

    def test_time_decorator_class(self):
        X, y = get_iris_data()
        exp = ClassificationExperiment("logistic")
        wrapped = TimeDecorator(exp)
        result = wrapped.run(X, y)
        assert "execution_time" in result
        assert result["execution_time"] >= 0