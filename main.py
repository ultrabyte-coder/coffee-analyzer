#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from tabulate import tabulate

from data_handler import read_csv_files
from reports.coffee_report import calculate_median_coffee

# Новый отчёт: добавить функцию в reports/ и зарегистрировать здесь
REPORTS = {
    "median-coffee": calculate_median_coffee,
}


def main():
    """Точка входа. Парсит аргументы, валидирует входные данные, печатает отчёт."""
    parser = argparse.ArgumentParser(description="Анализатор данных о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="Тип отчёта (median-coffee)")
    args = parser.parse_args()

    if args.report not in REPORTS:
        print(f"Ошибка: неизвестный тип отчёта '{args.report}'", file=sys.stderr)
        sys.exit(1)

    for file_path in args.files:
        if not Path(file_path).exists():
            print(f"Ошибка: файл не найден: {file_path}", file=sys.stderr)
            sys.exit(1)

    data = read_csv_files(args.files)
    report_data = REPORTS[args.report](data)
    print(tabulate(report_data, headers=["Студент", "Медиана трат на кофе"], tablefmt="grid"))


if __name__ == "__main__":
    main()
