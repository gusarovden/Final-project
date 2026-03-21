import pytest
import allure
from pages.api_page import ApiPage


@pytest.fixture
def api_page():
    return ApiPage()

@allure.feature("Диагностика API")
@allure.story("Проверка формирования URL")
@pytest.mark.diagnostic
def test_url_encoding_check(api_page):
    """Проверяет корректность кодирования URL для кириллических запросов"""
    test_phrases = ["Гарри Поттер", "Harry Potter", "Книга 2024"]

    for phrase in test_phrases:
        with allure.step(f"Формируем URL для фразы: '{phrase}'"):
            response = api_page.search_goods(77, phrase)

        print(f"\n{'='*60}")
        print(f"ТЕСТ ДЛЯ ФРАЗЫ: '{phrase}'")
        print(f"Сформированный URL: {response.url}")
        print(f"Статус код: {response.status_code}")
        print(f"Тело ответа: {response.text}")
        print(f"{'='*60}\n")

        assert response.status_code == 200, (
            f"Запрос для '{phrase}' вернул статус {response.status_code}"
        )

@allure.feature("API поиск в Читай‑Город")
@allure.story("Тестирование поиска товаров")
@pytest.mark.api
@pytest.mark.parametrize(
    "search_phrase,expected_status,test_type",
    [
        ("Гарри Поттер", [200], "positive"),
        ("Harry Potter", [200], "positive"),
        ("Книга 2024", [200], "positive"),
        ("@#$%^&*", [400, 403, 422], "negative"),
        ("", [400, 422], "negative"),
    ]
)
def test_search_functionality(api_page, search_phrase, expected_status, test_type):
    with allure.step(f"Отправляем запрос на поиск: '{search_phrase}'"):
        response = api_page.search_goods(77, search_phrase)

    with allure.step("Проверяем статус-код"):
        assert response.status_code in expected_status, (
            f"Ожидается статус {expected_status}, но получен {response.status_code}. "
            f"Запрос: '{search_phrase}'. URL: {response.url}"
        )

    # Дополнительная логика для позитивных тестов
    if test_type == "positive" and response.status_code == 200:
        try:
            data = response.json()
            # Здесь можно добавить проверку структуры данных
        except ValueError:
            pytest.fail(f"Ответ не в формате JSON: {response.text}")

    # Логика для негативных тестов
    elif test_type == "negative": 
        with allure.step("Для негативных тестов проверяем сообщение об ошибке"):
            try:
                error_data = response.json()
                # Проверяем наличие полей ошибки
                has_error_info = any(
                    key in error_data
            for key in ['error', 'message', 'errors', 'status']
        )
                assert has_error_info, (
                    "В ответе на негативный запрос нет информации об ошибке. "
            f"Тело ответа: {response.text}"
                )
            except ValueError:
                # Если ответ не JSON, проверяем текст
                assert len(response.text) > 0, "Пустой ответ на негативный запрос"







# @allure.feature("API поиск в Читай‑Город")
# @allure.story("Тестирование поиска товаров с диагностикой")
# @pytest.mark.api
# @pytest.mark.parametrize(
#     "search_phrase,expected_status,test_type",
#     [
#         ("Гарри Поттер", 200, "positive"),
#         ("Harry Potter", 200, "positive"),
#         ("Книга 2024", 200, "positive"),
#         ("@#$%^&*", 400, "negative"),
#         ("", 400, "negative"),
#     ]
# )
# def test_search_functionality(api_page, search_phrase, expected_status, test_type):
#     """
#     Тестирует функционал поиска с диагностикой проблем аутентификации
#     """

#     with allure.step(f"Отправляем запрос на поиск: '{search_phrase}'"):
#         response = api_page.search_goods(77, search_phrase)

#     # Детальная диагностика перед проверкой статуса
#     with allure.step("Детальная диагностика ответа API"):
#         print(f"\n{'='*60}")
#         print(f"ТЕСТ: '{search_phrase}'")
#         print(f"Ожидаемый статус: {expected_status}")
#         print(f"Полученный статус: {response.status_code}")
#         print(f"Заголовки запроса: {api_page.headers}")
#         print(f"URL запроса: {response.url}")
#         print(f"Тело ответа: {response.text}")
#         print(f"{'='*60}\n")

#     # Проверка аутентификации (если 401 — это критическая ошибка)
#     if response.status_code == 401:
#         pytest.fail(
#             f"Ошибка 401 Unauthorized — проблема с аутентификацией. "
#             f"Проверьте MY_HEADERS в config.py. "
#             f"Запрос: '{search_phrase}'"
#         )

#     with allure.step("Проверяем статус-код"):
#         assert response.status_code == expected_status, (
#             f"Ожидается статус {expected_status}, но получен {response.status_code}. "
#             f"Запрос: '{search_phrase}'. "
#             f"URL: {response.url}"
#         )

#     # Дополнительная проверка для позитивных тестов
#     if test_type == "positive" and response.status_code == 200:
#         with allure.step("Для позитивных тестов проверяем наличие результатов"):
#             try:
#                 response_data = response.json()
#             except ValueError:
#                 pytest.fail(f"Ответ не в формате JSON: {response.text}")

#             total_results = 0
#             if isinstance(response_data, dict):
#                 if 'total' in response_data:
#                     total_results = response_data['total']
#                 elif 'data' in response_data and isinstance(response_data['data'], dict):
#                     if 'total' in response_data['data']:
#                         total_results = response_data['data']['total']

#             # Для позитивных тестов допустимо 0 результатов (ничего не найдено)
#             assert total_results >= 0, f"Некорректное количество результатов: {total_results}"

#     else:  # Для негативных тестов
#         with allure.step("Для негативных тестов проверяем сообщение об ошибке"):
#             try:
#                 error_data = response.json()
#                 # Проверяем наличие полей ошибки
#                 has_error_info = any(
#                     key in error_data
#             for key in ['error', 'message', 'errors', 'status']
#         )
#                 assert has_error_info, (
#                     "В ответе на негативный запрос нет информации об ошибке. "
#             f"Тело ответа: {response.text}"
#                 )
#             except ValueError:
#                 # Если ответ не JSON, проверяем текст
#                 assert len(response.text) > 0, "Пустой ответ на негативный запрос"