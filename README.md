# Дипломная работа с сайтом "Читай-город"

## Документация проекта

### Оглавление

- Описание
- Структура
- Инструкция по работе с тестами
- Стек технологий
- Установка библиотек

### Описание

Финальная работа по ручному тестированию: <https://qadz12.yonote.ru/share/e3d9b34b-d71e-48f9-8522-2cebd3d906db>

Автотесты для сайта Читай-Город.

Сайт: https://www.chitai-gorod.ru/

Функционал:

Поиск книг

### Структура

pages - классы
- pages/api_page.py
- pages/main_page.py

tests - тесты
- tests/test_api.py
- tests/test_ui.py

pytest.ini - маркеры для запуска pytest

README.md - отчет-инструкция к работе

config.py - конфигурации

requirements.txt - зависимости

 ### Шаги по работе с тестами
 #### Подготовка:

 1. Запускаем VS Code или PyCharm
 2. Нажимаем Ctrl+Shift+P (или Cmd+Shift+P на macOS), чтобы открыть командную панель
1. Склонировать проект 'git clone https://github.com/gusarovden/Final-project.git'
4. Создаем и активируем виртуальное окружение python -m venv venv venv\Scripts\activate
5. Устанавливаем зависимости из файла requirements.txt. Команда pip install -r requirements.txt

#### Запуск API тестов:

1. Команда pytest tests/test_api.py --alluredir=./allure_result_api
2. После завершения тестирования вводим команду allure serve allure_result_api для просмотра отчета о тестировании

#### Запуск UI тестов:

1. Команда pytest tests/test_ui.py --alluredir=./allure_result_ui
2. После завершения тестирования вводим команду allure serve allure_result_ui для просмотра отчета о тестировании

#### Запуск всех тестов:

1. Команду pytest --alluredir=./allure_result_all
2. После завершения тестирования вводим команду allure serve allure_result_all для просмотра отчета о тестировании

### Стек технологий

- pytest - основная библиотека для написания и выполнения тестов.
- selenium - библиотека для автоматизации UI тестирования.
- requests - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- allure - библиотека для генерации отчетов
 о выполнении тестов.

