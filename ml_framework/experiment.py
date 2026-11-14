from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from .models import ModelFactory
from .metrics import MetricContext, AccuracyStrategy
from .observers import TrainingSubject


class Experiment(ABC):
    def __init__(self, model_name, metric_strategy=None):
        self.model_name = model_name
        self.metric_context = MetricContext(metric_strategy or AccuracyStrategy())
        self.subject = TrainingSubject()
        self.model = None
        self.results = {}

    def run(self, X, y, test_size=0.2, random_state=42):
        X_train, X_test, y_train, y_test = self.prepare_data(X, y, test_size, random_state)
        self.model = self.create_model()
        self.subject.notify_train_start(
            self.model_name,
            {"n_samples": len(X), "n_features": X.shape[1]},
        )
        self.train(X_train, y_train)
        self.results = self.evaluate(X_test, y_test)
        self.results = self.post_process(self.results)
        self.subject.notify_train_end(self.results)
        return self.results

    def prepare_data(self, X, y, test_size, random_state):
        stratify = y if len(set(y)) <= 20 else None
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=stratify
        )
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return X_train, X_test, y_train, y_test

    def create_model(self):
        return ModelFactory.create_model(self.model_name)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.subject.notify_epoch_end(1, {"status": "trained"})

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return self.metric_context.evaluate(y_test, y_pred)

    def post_process(self, results):
        return results


class ClassificationExperiment(Experiment):
    def __init__(self, model_name, metric_strategy=None):
        super().__init__(model_name, metric_strategy or AccuracyStrategy())


class RegressionExperiment(Experiment):
    def __init__(self, model_name, metric_strategy=None):
        from .metrics import MSEStrategy
        super().__init__(model_name, metric_strategy or MSEStrategy())