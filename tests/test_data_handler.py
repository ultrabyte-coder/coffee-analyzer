from data_handler import read_csv_files


def test_read_single_file(csv_with_data):
    result = read_csv_files([str(csv_with_data)])
    assert len(result) == 2
    assert result[0]["student"] == "Алексей Смирнов"
    assert result[0]["coffee_spent"] == "450"


def test_read_multiple_files(tmp_path):
    header = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam"
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    file1.write_text(f"{header}\nАлексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n")
    file2.write_text(f"{header}\nДарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n")

    result = read_csv_files([str(file1), str(file2)])

    assert len(result) == 2
    students = [r["student"] for r in result]
    assert "Алексей Смирнов" in students
    assert "Дарья Петрова" in students


def test_read_empty_file(csv_header_only):
    result = read_csv_files([str(csv_header_only)])
    assert result == []
