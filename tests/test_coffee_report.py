import pytest


@pytest.mark.parametrize(
    "data,expected",
    [
        pytest.param(
            [{"student": "Алексей", "coffee_spent": "450"}],
            [("Алексей", 450.0)],
            id="single_entry",
        ),
        pytest.param(
            [
                {"student": "Алексей", "coffee_spent": "450"},
                {"student": "Алексей", "coffee_spent": "500"},
                {"student": "Алексей", "coffee_spent": "550"},
            ],
            [("Алексей", 500.0)],
            id="odd_count_median",
        ),
        pytest.param(
            [
                {"student": "Павел", "coffee_spent": "380"},
                {"student": "Павел", "coffee_spent": "420"},
            ],
            [("Павел", 400.0)],
            id="even_count_median",
        ),
    ],
)
def test_median_calculation(report, data, expected):
    result = report.run(data)
    assert result == expected


def test_multiple_students_sorted_descending(report):
    data = [
        {"student": "Иван", "coffee_spent": "600"},
        {"student": "Иван", "coffee_spent": "650"},
        {"student": "Иван", "coffee_spent": "700"},
        {"student": "Мария", "coffee_spent": "100"},
        {"student": "Мария", "coffee_spent": "120"},
        {"student": "Мария", "coffee_spent": "150"},
    ]
    result = report.run(data)
    assert len(result) == 2
    assert result[0][0] == "Иван"
    assert result[0][1] == 650.0
    assert result[1][0] == "Мария"
    assert result[1][1] == 120.0


def test_empty_data(report):
    assert report.run([]) == []


def test_whitespace_in_student_name(report):
    data = [
        {"student": " Алексей ", "coffee_spent": "450"},
        {"student": " Алексей ", "coffee_spent": "550"},
    ]
    result = report.run(data)
    assert len(result) == 1
    assert result[0][0] == "Алексей"


def test_missing_field_raises(report):
    with pytest.raises(KeyError):
        report.run([{"student": "Алексей"}])


def test_invalid_value_raises(report):
    with pytest.raises(ValueError):
        report.run([{"student": "Алексей", "coffee_spent": "abc"}])


def test_file_not_found_logged():
    from data_handler import read_csv_files

    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent.csv"])
