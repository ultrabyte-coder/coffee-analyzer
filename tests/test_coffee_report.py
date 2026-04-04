from reports.coffee_report import calculate_median_coffee


def test_single_student_single_entry():
    # базовый случай — один студент, одна запись
    data = [{"student": "Алексей", "coffee_spent": "450"}]
    result = calculate_median_coffee(data)
    assert result == [("Алексей", 450.0)]


def test_single_student_multiple_entries():
    # нечётное кол-во значений — медиана это средний элемент
    data = [
        {"student": "Алексей", "coffee_spent": "450"},
        {"student": "Алексей", "coffee_spent": "500"},
        {"student": "Алексей", "coffee_spent": "550"},
    ]
    result = calculate_median_coffee(data)
    assert len(result) == 1
    assert result[0] == ("Алексей", 500.0)


def test_multiple_students_sorted_descending():
    # главное здесь — порядок, а не сами значения
    data = [
        {"student": "Иван", "coffee_spent": "600"},
        {"student": "Иван", "coffee_spent": "650"},
        {"student": "Иван", "coffee_spent": "700"},
        {"student": "Мария", "coffee_spent": "100"},
        {"student": "Мария", "coffee_spent": "120"},
        {"student": "Мария", "coffee_spent": "150"},
    ]
    result = calculate_median_coffee(data)
    assert len(result) == 2
    assert result[0][0] == "Иван"
    assert result[0][1] == 650.0
    assert result[1][0] == "Мария"
    assert result[1][1] == 120.0


def test_even_number_of_entries_median():
    # медиана двух значений — среднее между ними
    data = [
        {"student": "Павел", "coffee_spent": "380"},
        {"student": "Павел", "coffee_spent": "420"},
    ]
    result = calculate_median_coffee(data)
    assert result[0][1] == 400.0


def test_empty_data():
    # на всякий случай, вдруг все файлы пустые
    assert calculate_median_coffee([]) == []


def test_whitespace_in_student_name():
    # в реальных данных такое встречается, лучше проверить
    data = [
        {"student": " Алексей ", "coffee_spent": "450"},
        {"student": " Алексей ", "coffee_spent": "550"},
    ]
    result = calculate_median_coffee(data)
    assert len(result) == 1
    assert result[0][0] == "Алексей"
