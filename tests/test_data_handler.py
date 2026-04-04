from data_handler import read_csv_files

CSV_HEADER = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam"


def test_read_single_file(tmp_path):
    # просто убедиться что читается и поля на месте
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        f"{CSV_HEADER}\n"
        "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n"
        "Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n"
    )

    result = read_csv_files([str(csv_file)])

    assert len(result) == 2
    assert result[0]["student"] == "Алексей Смирнов"
    assert result[0]["coffee_spent"] == "450"


def test_read_multiple_files(tmp_path):
    # основной сценарий использования — несколько файлов сразу
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    file1.write_text(f"{CSV_HEADER}\nАлексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n")
    file2.write_text(f"{CSV_HEADER}\nДарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n")

    result = read_csv_files([str(file1), str(file2)])

    assert len(result) == 2
    students = [r["student"] for r in result]
    assert "Алексей Смирнов" in students
    assert "Дарья Петрова" in students


def test_read_empty_file(tmp_path):
    # если в файле только заголовок — возвращаем пустой список, не падаем
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text(f"{CSV_HEADER}\n")

    result = read_csv_files([str(csv_file)])

    assert result == []
