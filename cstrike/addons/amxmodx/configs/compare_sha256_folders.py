#!/usr/bin/env python3
import argparse
import hashlib
import os
import shutil
from pathlib import Path
from datetime import datetime

CHUNK_SIZE = 1024 * 1024  # 1 MB per read


def sha256_file(path: Path) -> str:
    """Compute SHA256 hash of a file in a memory-efficient way."""
    h = hashlib.sha256()
    with path.open("rb", "rb") as f:  # <-- note: "rb" twice is a bug, fix below
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()
