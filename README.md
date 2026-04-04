# Анализатор потребления кофе

Консольное приложение для анализа данных о подготовке студентов к экзаменам из CSV-файлов.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python main.py --files math.csv physics.csv programming.csv --report median-coffee
```

### Параметры:
- `--files` — пути к CSV-файлам с данными (можно передать несколько)
- `--report` — тип отчёта (`median-coffee`)

## Формат данных

CSV-файлы должны содержать колонки: `student`, `date`, `coffee_spent`, `sleep_hours`, `study_hours`, `mood`, `exam`

## Примеры работы

### Основной функционал
![Запуск с тремя файлами](screenshots/screenshot1.png)

### Тестирование
![Запуск тестов](screenshots/screenshot2.png)

### Покрытие тестами
![Покрытие кода](screenshots/screenshot3.png)

### Обработка ошибок
![Обработка неверного типа отчета](screenshots/screenshot4.png)

## Линтер и форматирование

```bash
python -m ruff check .   # проверка кода
python -m ruff format .  # форматирование
```

## Запуск тестов

```bash
pytest
pytest --cov=. --cov-report=term-missing
```

## Архитектура

Новые типы отчётов добавляются в `reports/`, регистрируются в словаре `REPORTS` в `main.py` — без изменения остальной логики.
