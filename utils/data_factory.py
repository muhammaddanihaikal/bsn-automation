import datetime
import uuid


def generate_full_name(prefix: str = "Pengguna") -> str:
    """Generate nama lengkap unik: [AUTO-QA] <Prefix> <Timestamp> sebagai penanda data tumbal."""
    timestamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    return f"[AUTO-QA] {prefix} {timestamp}"


def generate_username(prefix: str = "autoqa") -> str:
    """Generate username unik dengan suffix hex UUID."""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"
