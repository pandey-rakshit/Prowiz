import logging
import pandas as pd
from pathlib import Path
from config.paths  import RAW_FILES
from config.schema import DATE_COLS

log = logging.getLogger(__name__)


def _read_csv(name: str, path: Path) -> pd.DataFrame:
    parse_dates = DATE_COLS.get(name, [])
    encodings = ["utf-8", "latin-1", "cp1252"]

    for enc in encodings:
        try:
            df = pd.read_csv(path, parse_dates=parse_dates, low_memory=False, encoding=enc)
            df.columns = df.columns.str.strip()
            log.info("%s read with encoding: %s", name, enc)
            return df
        except UnicodeDecodeError:
            log.warning("%s failed with encoding: %s, trying next", name, enc)

    raise ValueError(f"Could not decode {path} with any of: {encodings}")


def load_one(name: str) -> pd.DataFrame:
    path = RAW_FILES.get(name)
    if path is None:
        raise KeyError(f"Unknown dataset: {name}")
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    df = _read_csv(name, path)
    log.info("%s loaded — shape: %s", name, df.shape)
    return df


def load_all() -> dict:
    datasets = {}
    for name, path in RAW_FILES.items():
        if not path.exists():
            log.warning("%s not found — skipping", name)
            continue
        datasets[name] = _read_csv(name, path)
        log.info("%s loaded — shape: %s", name, datasets[name].shape)
    return datasets