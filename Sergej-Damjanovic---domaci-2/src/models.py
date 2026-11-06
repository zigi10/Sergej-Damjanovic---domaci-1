from dataclasses import dataclass
from datetime import datetime


@dataclass
class Reservation:
    id: str
    guest_name: str
    check_in: datetime
    check_out: datetime
    room_number: int
    status: str
    amount: float

    @property
    def is_confirmed(self) -> bool:
        return self.status == "confirmed"

    @property
    def nights(self) -> int:
        return (self.check_out - self.check_in).days