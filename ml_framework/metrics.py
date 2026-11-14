from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score, f1_score, precision_score, mean_squared_error


class MetricStrategy(ABC):
    @abstractmethod
    def compute(self, y_true, y_pred):
        pass

    @abstractmethod
    def name(self):
        pass


class AccuracyStrategy(MetricStrategy):
    def compute(self, y_true, y_pred):
        return float(accuracy_score(y_true, y_pred))

    def name(self):
        return "Accuracy"


class F1Strategy(MetricStrategy):
    def compute(self, y_true, y_pred):
        return float(f1_score(y_true, y_pred, average="macro", zero_division=0))

    def name(self):
        return "F1 Score"


class PrecisionStrategy(MetricStrategy):
    def compute(self, y_true, y_pred):
        return float(precision_score(y_true, y_pred, average="macro", zero_division=0))

    def name(self):
        return "Precision"


class MSEStrategy(MetricStrategy):
    def compute(self, y_true, y_pred):
        return float(mean_squared_error(y_true, y_pred))

    def name(self):
        return "MSE"


class MetricContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def evaluate(self, y_true, y_pred):
        value = self._strategy.compute(y_true, y_pred)
        return {"metric": self._strategy.name(), "value": value}