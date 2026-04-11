from abc import ABC, abstractmethod

from data_handler import CoffeeRecord


class Report(ABC):
    """Базовый класс для всех отчётов.

    Каждый новый отчёт должен наследоваться от Report
    и реализовать метод run.
    """

    @abstractmethod
    def run(self, data: list[CoffeeRecord]) -> list[tuple[str, float]]:
        """Принимает данные, возвращает список кортежей (название, значение)."""
        ...
