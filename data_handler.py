import csv
import logging
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)


class CoffeeRecord(TypedDict):
    student: str
    date: str
    coffee_spent: str
    sleep_hours: str
    study_hours: str
    mood: str
    exam: str


def read_csv_files(file_paths: list[str]) -> list[CoffeeRecord]:
    """Читает CSV-файлы и объединяет строки в один список.

    Предполагается что файлы валидны и содержат заголовок.
    Все строки возвращаются как словари с ключами из заголовка.
    """
    combined = []
    for file_path in file_paths:
        try:
            with open(Path(file_path), newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                combined.extend(reader)
        except FileNotFoundError:
            logger.critical("Файл не найден: %s", file_path)
            raise
        except PermissionError:
            logger.critical("Нет прав доступа к файлу: %s", file_path)
            raise
        except csv.Error as e:
            logger.error("Ошибка чтения CSV-файла %s: %s", file_path, e)
            raise
    return combined
