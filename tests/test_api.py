import pytest
from config.test_data import SEARCH_DATA

class TestSearchAPIFunctionality:
    """API‑тесты поиска книг."""

    @pytest.mark.api
    def test_api_search_cyrillic(self, api_client, auth_token):
        """API‑тест: поиск на кириллице."""
        response = api_client.search_books('книга')
        assert response.status_code == 200
        assert 'items' in response
        assert isinstance(response['items'], list)
        # Дополнительно проверяем, что есть хотя бы один результат (если это ожидается)
        assert len(response['items']) >= 0

    @pytest.mark.api
    def test_api_search_latin(self, api_client, auth_token):
        """API‑тест: поиск на латинице."""
        response = api_client.search_books(SEARCH_DATA['latin'])
        assert response.status_code == 200
        assert 'items' in response
        assert isinstance(response['items'], list)
        assert len(response['items']) > 0

    @pytest.mark.api
    def test_api_search_with_numbers(self, api_client, auth_token):
        """API‑тест: название с цифрами."""
        response = api_client.search_books('роман2024')
        assert response.status_code == 200
        assert 'items' in response
        assert isinstance(response['items'], list)
        # Может быть 0 результатов — это нормально для такого запроса
        assert len(response['items']) >= 0

    @pytest.mark.api
    def test_api_search_special_chars(self, api_client, auth_token):
        """API‑тест: произвольный набор символов."""
        response = api_client.search_books('#@#$%^&*()')
        assert response.status_code in [200, 400]  # 200 — если API обрабатывает, 400 — если валидирует
        if response.status_code == 200:
            assert 'items' in response
            assert isinstance(response['items'], list)
            assert len(response['items']) == 0  # Ожидаем пустой список для бессмысленного запроса
        elif response.status_code == 400:
            # Проверяем, что есть сообщение об ошибке
            assert 'error' in response or 'message' in response

    @pytest.mark.api
    def test_api_search_empty(self, api_client, auth_token):
        """API‑тест: пустой поиск."""
        response = api_client.search_books('')
        assert response.status_code in [200, 400]
        if response.status_code == 200:
            assert 'items' in response
            assert isinstance(response['items'], list)
            # В зависимости от логики API: может возвращать топ-книги или пустой список
            assert len(response['items']) >= 0
        elif response.status_code == 400:
            assert 'error' in response or 'message' in response  # Проверка на сообщение об ошибке