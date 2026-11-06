from datetime import datetime
from typing import List
from .models import Reservation
from .protocols import DataSource


class CsvDataSource:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_reservations(
        self, date_from: datetime, date_to: datetime
    ) -> List[Reservation]:
        return []