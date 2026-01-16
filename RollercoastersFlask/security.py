# ---------- Input validation for length, range 50 op to 250 ---------- #

from config import ALLOWED_KEYS

def validate_length(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return None
    return value if 50 <= value <= 250 else None

# ---------- Allowed keys for tamper protection, protection against unintentional steps ---------- #
def validate_tamper(data):
    """Return None if OK, otherwise an error string."""
    for key in data.keys():
        if key not in ALLOWED_KEYS:
            return "Unexpected input detected ❌"
    return None





