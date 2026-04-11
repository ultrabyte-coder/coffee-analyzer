"""Тесты для CLI (main.py)."""

import subprocess
import sys


def _run_cli(args: list[str]) -> subprocess.CompletedProcess:
    """Запускает main.py с указанными аргументами."""
    return subprocess.run(
        [sys.executable, "-m", "main"] + args,
        capture_output=True,
        text=True,
    )


def test_successful_run(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-06-01,600,3.0,15,зомби,Математика\n"
        "Иван,2024-06-02,650,2.5,17,зомби,Математика\n"
        "Мария,2024-06-01,100,8.0,3,отл,Математика\n"
        "Мария,2024-06-02,120,8.5,2,отл,Математика\n"
    )

    result = _run_cli(["--files", str(csv_file), "--report", "median-coffee"])

    assert result.returncode == 0
    assert "Иван" in result.stdout
    assert "Мария" in result.stdout
    assert "Студент" in result.stdout


def test_nonexistent_file():
    result = _run_cli(["--files", "nonexistent.csv", "--report", "median-coffee"])

    assert result.returncode == 1
    assert "nonexistent.csv" in result.stderr


def test_unknown_report_type():
    result = _run_cli(["--files", "math.csv", "--report", "unknown-report"])

    assert result.returncode == 2
    assert "invalid choice" in result.stderr
