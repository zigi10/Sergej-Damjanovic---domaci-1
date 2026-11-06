def prosjecna_cijena(cijene):
    """Racuna prosjecnu cijenu iz liste cijena."""
    if not cijene:
        raise ValueError("Lista cijena ne smije biti prazna.")

    return sum(cijene) / len(cijene)