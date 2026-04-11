#!/usr/bin/env python3

import argparse
import logging
import sys
from pathlib import Path

from tabulate import tabulate

from data_handler import read_csv_files
from reports.coffee_report import MedianCoffeeReport

logger = logging.getLogger(__name__)

# Новый отчёт: добавить класс в reports/ и зарегистрировать здесь
REPORTS = {
    "median-coffee": MedianCoffeeReport(),
}


def main():
    """Точка входа. Парсит аргументы, валидирует входные данные, печатает отчёт."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s — %(name)s: %(message)s",
    )
    parser = argparse.ArgumentParser(description="Анализатор данных о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам")
    parser.add_argument(
        "--report",
        required=True,
        choices=REPORTS.keys(),
        help="Тип отчёта",
    )
    args = parser.parse_args()

    for file_path in args.files:
        if not Path(file_path).exists():
            logger.critical("Файл не найден: %s", file_path)
            sys.exit(1)

    try:
        data = read_csv_files(args.files)
        report_data = REPORTS[args.report].run(data)
        print(tabulate(report_data, headers=["Студент", "Медиана трат на кофе"], tablefmt="grid"))
    except Exception as e:
        logger.error("%s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
