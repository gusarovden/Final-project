import allure
import requests
from config import MY_HEADERS, API_URL
from urllib.parse import urlencode


class ApiPage:
    def __init__(self):
        self.base_url = API_URL.rstrip('/')
        self.headers = MY_HEADERS

    @allure.step("Отправка запроса на поиск")
    def search_goods(self, city_id, phrase):
        """Универсальный метод для поиска"""
        search_url = f"{self.base_url}/search/facet-search"  
        search_params = {
            'customerCityId': city_id,
            'products[page]': 1,
            'products[per-page]': 60,
            'phrase': phrase,
            'abTestGroup': 1
        }

        # Кодируем параметры вручную для корректной передачи кириллицы
        encoded_params = urlencode(search_params, safe='[]')
        full_url = f"{search_url}?{encoded_params}"
        return requests.get(full_url, headers=self.headers, timeout=10 )