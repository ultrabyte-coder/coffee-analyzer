# Анализатор потребления кофе

Консольное приложение для анализа данных о подготовке студентов к экзаменам из CSV-файлов.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python -m main --files math.csv physics.csv programming.csv --report median-coffee
```

### Параметры:
- `--files` — пути к CSV-файлам с данными (можно передать несколько)
- `--report` — тип отчёта (`median-coffee`)

## Обработка ошибок

Приложение корректно обрабатывает ошибки и выводит сообщения в лог:

```bash
# Несуществующий файл
python -m main --files nonexistent.csv --report median-coffee
# CRITICAL — data_handler: Файл не найден: nonexistent.csv

# Неизвестный тип отчёта
python -m main --files math.csv --report unknown-report
# error: argument --report: invalid choice: 'unknown-report' (choose from median-coffee)
```

## Формат данных

CSV-файлы должны содержать колонки: `student`, `date`, `coffee_spent`, `sleep_hours`, `study_hours`, `mood`, `exam`

## Примеры работы

### Основной функционал
![Запуск с тремя файлами](https://drive.google.com/uc?export=view&id=1EnzL5lmbgyI5lIvMgbfo5wQDhwV3_erA)

### Тестирование
![Запуск тестов](https://drive.google.com/uc?export=view&id=1AQZQwbPXMQybicTQ8HAoSrZEzj8Kev_Z)

### Покрытие тестами
![Покрытие кода](https://drive.google.com/uc?export=view&id=1UErl3JoEX56yOtcDDQB7Kng497aehAXh)

### Обработка ошибок
![Обработка ошибки: файл не найден](https://drive.google.com/uc?export=view&id=1mJjAtpH7XKD5MQiu7ZZ4mKo6EELP_KcB))

### Валидация типа отчёта
![Валидация: неизвестный тип отчёта через argparse choices](https://drive.google.com/uc?export=view&id=1Gat51YmS5SpROcv3HVsq-Bsr_lamZ_cH)

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
