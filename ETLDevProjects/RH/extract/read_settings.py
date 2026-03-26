from pathlib import Path

import chardet
import pandas as pd


def check_file_exists(file_path: Path, logger=None) -> None:
    """
    Confirm the raw file exists before attempting to read it.
    Raises FileNotFoundError if missing.
    """
    if not file_path.exists():
        if logger:
            logger.error(f"Raw file not found: {file_path}")
        raise FileNotFoundError(f"Raw file not found: {file_path}")
    if logger:
        logger.info(f"Raw file found: {file_path}")


def detect_encoding(
    file_path: Path,
    sample_size: int = 50_000,
    confidence_threshold: float = 0.80,
    fallback: str = "utf-8",
    logger=None,
) -> str:
    """
    Detect the encoding of a file by sampling the first `sample_size` bytes.
    Falls back to `fallback` encoding if confidence is below `confidence_threshold`.
    Returns the detected (or fallback) encoding as a string.
    """
    with open(file_path, "rb") as f:
        sample = f.read(sample_size)

    detected   = chardet.detect(sample)
    encoding   = detected["encoding"]
    confidence = detected["confidence"]

    if confidence < confidence_threshold:
        if logger:
            logger.warning(
                f"Low encoding confidence ({confidence:.0%}) — detected: {encoding}. "
                f"Falling back to {fallback}."
            )
        return fallback

    if logger:
        logger.info(f"Encoding detected: {encoding} (confidence: {confidence:.0%})")

    return encoding


def load_raw_data(
    file_path: Path,
    delimiter: str,
    encoding: str,
    logger=None,
) -> pd.DataFrame:
    """
    Load a delimited file into a DataFrame.
    All columns are read as strings to prevent silent type coercion.
    Empty strings are preserved as-is (keep_default_na=False).
    """
    df = pd.read_csv(
        file_path,
        sep=delimiter,
        encoding=encoding,
        dtype=str,
        keep_default_na=False,
    )

    if logger:
        logger.info(
            f"Raw data loaded: {df.shape[0]:,} rows × {df.shape[1]} columns"
        )

    return df
