"""Core logic: password evaluation and generation.

This module has no GUI dependencies: it returns data and never prints,
so the same functions can be used by the desktop UI, a CLI or tests.
"""

import secrets
import string
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

COMMON_PASSWORDS_FILE = Path(__file__).parent / "commonPasswords.txt"
MAX_SCORE = 8  # 1 (not common) + 4 (length) + 3 (character variety)

CHARSETS = {
    "upper": string.ascii_uppercase,
    "lower": string.ascii_lowercase,
    "digit": string.digits,
    "special": string.punctuation,
}


@dataclass
class PasswordEvaluation:
    score: int
    is_common: bool
    length: int
    char_types: int
    label: str
    max_score: int = MAX_SCORE


@lru_cache(maxsize=1)
def load_common_passwords() -> frozenset[str]:
    """Load the common-password list once and keep it in memory."""
    try:
        with open(COMMON_PASSWORDS_FILE, encoding="utf-8", errors="ignore") as f:
            return frozenset(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return frozenset()


def _label(score: int, is_common: bool) -> str:
    if is_common:
        return "Compromised: found in a common password list"
    if score < 4:
        return "Very weak"
    if score == 4:
        return "Weak"
    if score == 5:
        return "Fairly strong"
    return "Very strong"


def evaluate_password(password: str) -> PasswordEvaluation:
    length = len(password)
    char_types = sum(
        any(c in charset for c in password) for charset in CHARSETS.values()
    )
    is_common = password in load_common_passwords()

    if is_common:
        score = 0
    else:
        score = 1                                            # not in common list
        score += sum(length > n for n in (8, 12, 17, 20))    # length
        score += max(char_types - 1, 0)                      # variety

    return PasswordEvaluation(
        score, is_common, length, char_types, _label(score, is_common)
    )


def generate_password(length: int, upper=True, lower=True,
                      digit=True, special=True) -> str:
    """Cryptographically secure password with at least one char per chosen type."""
    flags = {"upper": upper, "lower": lower, "digit": digit, "special": special}
    pools = [CHARSETS[name] for name, enabled in flags.items() if enabled]
    if not pools:
        raise ValueError("Select at least one character type.")
    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)}.")

    chars = [secrets.choice(pool) for pool in pools]
    alphabet = "".join(pools)
    chars += [secrets.choice(alphabet) for _ in range(length - len(pools))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def generate_passwords(min_len: int, max_len: int, amount: int, upper=True,
                       lower=True, digit=True, special=True
                       ) -> list[tuple[str, PasswordEvaluation]]:
    if min_len > max_len:
        raise ValueError("Minimum length cannot exceed maximum length.")
    results = []
    for _ in range(amount):
        length = min_len + secrets.randbelow(max_len - min_len + 1)  # max included
        pwd = generate_password(length, upper, lower, digit, special)
        results.append((pwd, evaluate_password(pwd)))
    return results