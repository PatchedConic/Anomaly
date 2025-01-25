def is_float(*values: str) -> bool:
    for value in values:
        try:
            float(value)
        except ValueError:
            return False
    return True
