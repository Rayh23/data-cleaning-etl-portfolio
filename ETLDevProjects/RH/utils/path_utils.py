from pathlib import Path


def find_repo_root(start: Path) -> Path:
    """
    Walk up the directory tree from `start` until a .git folder is found.
    Returns the repo root as a Path object.

    Raises FileNotFoundError if no .git directory is found in any parent.
    """
    for path in [start, *start.parents]:
        if (path / ".git").exists():
            return path
    raise FileNotFoundError(
        "Repo root not found — .git directory missing from all parent paths."
    )
