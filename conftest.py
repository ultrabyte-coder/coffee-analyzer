import pytest

from reports.coffee_report import MedianCoffeeReport

CSV_HEADER = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam"


@pytest.fixture
def report():
    return MedianCoffeeReport()


@pytest.fixture
def csv_with_data(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        f"{CSV_HEADER}\n"
        "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n"
        "Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n"
    )
    return csv_file


@pytest.fixture
def csv_header_only(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text(f"{CSV_HEADER}\n")
    return csv_file
