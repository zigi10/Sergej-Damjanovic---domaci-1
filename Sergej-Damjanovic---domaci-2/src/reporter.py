from typing import List
from .models import Reservation
from .protocols import Reporter


class TextReporter:
    def generate_report(self, reservations: List[Reservation]) -> str:
        lines = ["=== IZVJEŠTAJ O REZERVACIJAMA ==="]
        total = 0.0
        for r in reservations:
            lines.append(
                f"{r.id} | {r.guest_name} | {r.nights} noći | {r.amount} EUR"
            )
            total += r.amount
        lines.append(f"UKUPNO: {total} EUR")
        return "\n".join(lines)