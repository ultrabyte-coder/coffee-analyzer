import csv
from pathlib import Path
from typing import Any


def read_csv_files(file_paths: list[str]) -> list[dict[str, Any]]:
    """Читает CSV-файлы и объединяет строки в один список.

    Предполагается что файлы валидны и содержат заголовок.
    Все строки возвращаются как словари с ключами из заголовка.
    """
    combined = []
    for file_path in file_paths:
        with open(Path(file_path), newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            combined.extend(reader)
    return combined
