from datetime import datetime
from typing import List
from .models import Reservation
from .protocols import DataSource, Reporter


class ReservationProcessor:
    def __init__(self, source: DataSource, reporter: Reporter) -> None:
        self.source = source
        self.reporter = reporter

    def fetch(
        self, date_from: datetime, date_to: datetime
    ) -> List[Reservation]:
        return self.source.get_reservations(date_from, date_to)

    def total_revenue(self, reservations: List[Reservation]) -> float:
        return sum(r.amount for r in reservations if r.is_confirmed)

    def active_count(self, reservations: List[Reservation]) -> int:
        return sum(1 for r in reservations if r.is_confirmed)

    def run(self, date_from: datetime, date_to: datetime) -> str:
        reservations = self.fetch(date_from, date_to)
        return self.reporter.generate_report(reservations)