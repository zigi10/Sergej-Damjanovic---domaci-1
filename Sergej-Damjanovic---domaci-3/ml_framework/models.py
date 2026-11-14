from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


class ModelFactory:
    registry = {
        "linear": LinearRegression,
        "logistic": LogisticRegression,
        "decision_tree": DecisionTreeClassifier,
        "knn": KNeighborsClassifier,
    }

    @classmethod
    def create_model(cls, name, **kwargs):
        if name not in cls.registry:
            raise ValueError(f"Nepoznat model: {name}")
        return cls.registry[name](**kwargs)

    @classmethod
    def list_models(cls):
        return list(cls.registry.keys())