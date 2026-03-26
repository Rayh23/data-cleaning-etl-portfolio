import re


def clean_placeholder(val: str, placeholders: set) -> str:
    """
    Return an empty string if `val` (stripped, lowercased) is in `placeholders`.
    Otherwise return the original value unchanged.
    """
    return "" if val.strip().lower() in placeholders else val


def is_valid_name(
    val: str,
    pattern: str,
    min_len: int = 1,
    max_len: int = 70,
) -> bool:
    """
    Validate a name field against a regex pattern and length constraints.
    Empty strings are considered valid — the PII rule handles coverage checks.

    Args:
        val      : The name value to validate.
        pattern  : Compiled or raw regex string for valid name characters.
        min_len  : Minimum character length for a non-empty name.
        max_len  : Maximum character length for a non-empty name.

    Returns:
        True if the value is empty or passes all validation rules.
    """
    if val == "":
        return True
    return min_len <= len(val) <= max_len and bool(re.fullmatch(pattern, val))
