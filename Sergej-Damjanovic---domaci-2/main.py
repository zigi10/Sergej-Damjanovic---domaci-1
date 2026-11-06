from datetime import datetime
from src.data_source import CsvDataSource
from src.reporter import TextReporter
from src.processor import ReservationProcessor


def main() -> None:
    source = CsvDataSource("reservations.csv")
    reporter = TextReporter()
    processor = ReservationProcessor(source, reporter)
    report = processor.run(datetime(2026, 11, 1), datetime(2026, 11, 30))
    print(report)


if __name__ == "__main__":
    main()