from abc import ABC, abstractmethod


class TrainingObserver(ABC):
    @abstractmethod
    def on_train_start(self, model_name, dataset_info):
        pass

    @abstractmethod
    def on_epoch_end(self, epoch, metrics):
        pass

    @abstractmethod
    def on_train_end(self, results):
        pass


class ConsoleObserver(TrainingObserver):
    def on_train_start(self, model_name, dataset_info):
        print(f"Početak treninga: {model_name}")
        print(f"Uzoraka: {dataset_info.get('n_samples', '?')}, osobina: {dataset_info.get('n_features', '?')}")

    def on_epoch_end(self, epoch, metrics):
        parts = []
        for k, v in metrics.items():
            if isinstance(v, (int, float)):
                parts.append(f"{k}={v:.4f}")
            else:
                parts.append(f"{k}={v}")
        metric_str = ", ".join(parts)
        print(f"Korak {epoch}: {metric_str}")

    def on_train_end(self, results):
        print(f"Trening završen. Rezultati: {results}")


class HistoryObserver(TrainingObserver):
    def __init__(self):
        self.history = []
        self.train_info = {}

    def on_train_start(self, model_name, dataset_info):
        self.train_info = {"model": model_name}
        self.train_info.update(dataset_info)
        self.history = []
        self.history.append({"type": "start", "model": model_name, **dataset_info})

    def on_epoch_end(self, epoch, metrics):
        self.history.append({"epoch": epoch, **metrics})

    def on_train_end(self, results):
        self.history.append({"type": "final", **results})

    def get_history(self):
        return self.history


class TrainingSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify_train_start(self, model_name, dataset_info):
        for observer in self._observers:
            observer.on_train_start(model_name, dataset_info)

    def notify_epoch_end(self, epoch, metrics):
        for observer in self._observers:
            observer.on_epoch_end(epoch, metrics)

    def notify_train_end(self, results):
        for observer in self._observers:
            observer.on_train_end(results)