from datetime import datetime
from typing import List
from src.models import Reservation
from src.processor import ReservationProcessor
from src.reporter import TextReporter


class FakeDataSource:
    def __init__(self, data: List[Reservation]) -> None:
        self.data = data

    def get_reservations(
        self, date_from: datetime, date_to: datetime
    ) -> List[Reservation]:
        return self.data


def _make_reservation(
    id: str, status: str = "confirmed", amount: float = 100.0
) -> Reservation:
    return Reservation(
        id=id,
        guest_name="Test Guest",
        check_in=datetime(2026, 11, 1),
        check_out=datetime(2026, 11, 4),
        room_number=101,
        status=status,
        amount=amount,
    )


def test_total_revenue_counts_only_confirmed() -> None:
    source = FakeDataSource(
        [
            _make_reservation("R1", "confirmed", 200.0),
            _make_reservation("R2", "cancelled", 200.0),
            _make_reservation("R3", "confirmed", 300.0),
        ]
    )
    processor = ReservationProcessor(source, TextReporter())
    reservations = processor.fetch(datetime(2026, 11, 1), datetime(2026, 11, 30))
    assert processor.total_revenue(reservations) == 500.0


def test_active_count() -> None:
    source = FakeDataSource(
        [
            _make_reservation("R1", "confirmed"),
            _make_reservation("R2", "confirmed"),
            _make_reservation("R3", "pending"),
        ]
    )
    processor = ReservationProcessor(source, TextReporter())
    reservations = processor.fetch(datetime(2026, 11, 1), datetime(2026, 11, 30))
    assert processor.active_count(reservations) == 2


def test_report_contains_total() -> None:
    source = FakeDataSource([_make_reservation("R1", "confirmed", 250.0)])
    processor = ReservationProcessor(source, TextReporter())
    report = processor.run(datetime(2026, 11, 1), datetime(2026, 11, 30))
    assert "250" in report
    assert "IZVJEŠTAJ" in report