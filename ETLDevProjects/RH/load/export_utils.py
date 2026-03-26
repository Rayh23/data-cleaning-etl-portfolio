from pathlib import Path

import pandas as pd


def export_cleaned(
    df: pd.DataFrame,
    outputs_dir: Path,
    dataset_name: str,
    logger=None,
) -> Path:
    """
    Write the cleaned DataFrame to outputs/ as a UTF-8 comma-separated CSV.
    Returns the output file path.
    """
    output_file = outputs_dir / f"{dataset_name}_cleaned.csv"
    df.to_csv(output_file, sep=",", encoding="utf-8", index=False)

    if logger:
        logger.info(f"Cleaned output saved → {output_file}")

    return output_file


def summarise_garbage(
    garbage_dir: Path,
    dataset_name: str,
    logger=None,
) -> list:
    """
    List all garbage files matching {dataset_name}_*.csv with their row counts.
    Logs each file if a logger is provided.
    Returns a list of (filename, row_count) tuples.
    """
    garbage_files = sorted(garbage_dir.glob(f"{dataset_name}_*.csv"))
    summary = []

    for f in garbage_files:
        row_count = sum(1 for _ in open(f, encoding="utf-8")) - 1
        summary.append((f.name, row_count))
        if logger:
            logger.info(f"Garbage file confirmed → {f.name} ({row_count:,} rows)")

    return summary


def log_etl_complete(
    dataset_name: str,
    raw_row_count: int,
    clean_row_count: int,
    output_file: Path,
    garbage_count: int,
    logger=None,
) -> None:
    """
    Write a structured ETL COMPLETE summary block to the log.
    """
    if not logger:
        return

    retention = round(clean_row_count / raw_row_count * 100, 2)

    logger.info("=" * 60)
    logger.info("ETL COMPLETE")
    logger.info(f"  Dataset         : {dataset_name}")
    logger.info(f"  Raw rows        : {raw_row_count:,}")
    logger.info(f"  Final clean rows: {clean_row_count:,}")
    logger.info(f"  Retention rate  : {retention}%")
    logger.info(f"  Output file     : {output_file.name}")
    logger.info(f"  Garbage files   : {garbage_count}")
    logger.info("=" * 60)
