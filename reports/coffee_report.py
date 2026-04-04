from collections import defaultdict
from statistics import median
from typing import Any


def calculate_median_coffee(data: list[dict[str, Any]]) -> list[tuple[str, float]]:
    """Считает медиану трат на кофе по каждому студенту за весь период.

    Возвращает список кортежей (студент, медиана), отсортированных по убыванию.
    """
    student_spending: dict[str, list[float]] = defaultdict(list)

    for row in data:
        student = row["student"].strip()
        student_spending[student].append(float(row["coffee_spent"]))

    result = [(student, median(values)) for student, values in student_spending.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    return result
