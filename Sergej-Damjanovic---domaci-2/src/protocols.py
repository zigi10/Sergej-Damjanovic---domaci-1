from typing import Protocol, List
from datetime import datetime
from .models import Reservation


class DataSource(Protocol):
    def get_reservations(
        self, date_from: datetime, date_to: datetime
    ) -> List[Reservation]:
        ...


class Reporter(Protocol):
    def generate_report(self, reservations: List[Reservation]) -> str:
        ...