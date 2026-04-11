import logging
from collections import defaultdict
from statistics import median

from data_handler import CoffeeRecord
from reports.base import Report

logger = logging.getLogger(__name__)


class MedianCoffeeReport(Report):
    """Считает медиану трат на кофе по каждому студенту за весь период."""

    def run(self, data: list[CoffeeRecord]) -> list[tuple[str, float]]:
        """Возвращает список кортежей (студент, медиана), отсортированных по убыванию."""
        student_spending: dict[str, list[float]] = defaultdict(list)

        for row in data:
            try:
                student = row["student"].strip()
                student_spending[student].append(float(row["coffee_spent"]))
            except KeyError as e:
                logger.error("Отсутствует поле %s в строке: %s", e, row)
                raise
            except ValueError as e:
                value = row.get("coffee_spent", "N/A")
                logger.error("Некорректное значение coffee_spent: %s — %s", value, e)
                raise

        result = [(student, median(values)) for student, values in student_spending.items()]
        result.sort(key=lambda x: x[1], reverse=True)
        return result
