import pytest
import allure


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







