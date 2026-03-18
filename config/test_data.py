import os

# === ДАННЫЕ ДЛЯ АВТОРИЗАЦИИ (по телефону) ===
AUTH_DATA = {
    'phone': os.getenv('PHONE_NUMBER', '+79009368472'),
    'sms_code': os.getenv('SMS_CODE', '1234')
}

# === ТЕСТОВЫЕ ДАННЫЕ ДЛЯ ПОИСКА (API и UI) ===
SEARCH_DATA = {
    'search_cyrillic': {
        'query': 'Война и мир',
        'description': 'Поиск по кириллическому запросу'
    },
    'search_latin': {
        'query': 'Harry Potter',
        'description': 'Поиск по латинскому запросу'
    },
    'search_with_numbers': {
        'query': 'Книга 2024',
        'description': 'Поиск с цифрами в запросе'
    },
    'search_special_chars': {
        'query': '!@#$%^&*()',
        'description': 'Поиск со спецсимволами'
    },
    'search_empty': {
        'query': '',
        'description': 'Пустой поисковый запрос'
    },
    'search_whitespace': {
        'query': '   ',
        'description': 'Запрос из пробелов'
    },
    'search_long_query': {
        'query': 'a' * 100,
        'description': 'Длинный поисковый запрос (100 символов)'
    },
    'search_short_query': {
        'query': 'а',
        'description': 'Короткий поисковый запрос (1 символ)'
    }
}

# === ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ КНИГ ===
BOOK_DATA = {
    'valid_book_title': {
        'title': 'Мастер и Маргарита',
        'description': 'Существующая книга для проверки результатов поиска'
    },
    'invalid_book_id': {
        'id': 999999,
        'description': 'Некорректный ID книги для проверки обработки ошибок'
    }
}

# === НАСТРОЙКИ ДЛЯ API-ТЕСТОВ ===
API_TEST_CONFIG = {
    'min_search_length': 1,
    'max_search_length': 100,
    'timeout_seconds': 30,
    'expected_status_codes': {
        'success': 200,
        'unauthorized': 401,
        'bad_request': 400
    }
}

# === ВСПОМОГАТЕЛЬНЫЕ КОНСТАНТЫ ===
TEST_TIMEOUTS = {
    'api_request': 30,  # секунд
    'page_load': 10,   # секунд
    'element_wait': 5    # секунд
}

# === КОНФИГУРАЦИЯ UI-ТЕСТОВ ===
UI_TEST_DATA = {
    'page_titles': {
        'main': 'Читай-город',
        'search_results': 'Результаты поиска'
    },
    'error_messages': {
        'empty_search': 'Введите запрос для поиска',
        'no_results': 'Ничего не найдено'
    }
}