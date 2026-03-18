import requests
import os
import logging

logger = logging.getLogger(__name__)

class APIClient:
    """Клиент для работы с API интернет‑магазина."""

    def __init__(self):
        # Исправляем os.getenv() на os.environ.get()
        self.base_url = os.environ.get('API_URL', 'https://web-agr.chitai-gorod.ru/web/api/v2')
        self.session = requests.Session()
        self.auth_token = None

    def _check_response(self, response):
        """Проверяет статус ответа и логирует детали при ошибке."""
        try:
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP ошибка: {e}")
            logger.error(f"URL: {response.url}")
            logger.error(f"Статус: {response.status_code}")
            if response.text:
                logger.error(f"Тело ответа: {response.text}")
            raise
        except Exception as e:
            logger.error(f"Неожиданная ошибка при выполнении запроса: {e}")
            raise

    def validate_token(self):
        """Проверяет валидность токена авторизации."""
        url = f"{self.base_url}/auth/validate"
        response = self.session.get(url)
        return self._check_response(response)

    def send_sms_code(self, phone_number: str):
        """Отправляет запрос на получение SMS-кода и возвращает объект Response."""
        sms_url = f"{self.base_url}/auth/send-sms"
        payload = {'phone': phone_number}
        headers = {'Content-Type': 'application/json'}

        logger.info(f"Отправка запроса на SMS для номера {phone_number}")
        response = self.session.post(sms_url, json=payload, headers=headers)
        return self._check_response(response)

    def login_by_phone(self, phone_number: str, sms_code: str) -> str:
        """Выполняет авторизацию по номеру телефона и SMS-коду."""
        login_url = f"{self.base_url}/auth/login-by-phone"
        payload = {
            'phone': phone_number,
            'code': sms_code
        }
        headers = {'Content-Type': 'application/json'}

        logger.info(f"Попытка авторизации для номера {phone_number}")
        response = self.session.post(login_url, json=payload, headers=headers)

        # Проверяем статус ответа через общий метод
        response = self._check_response(response)

        data = response.json()
        token = data.get('token')

        if not token:
            logger.error("Токен авторизации не найден в ответе")
            raise ValueError("Токен авторизации не получен")

        self.auth_token = token
        logger.info("Авторизация по телефону успешна, токен получен")
        return token

    def search_books(self, query: str):
        """Выполняет поиск книг через API и возвращает объект Response."""
        search_url = f"{self.base_url}/search/facet-search"
        params = {'query': query}
        headers = {}

        if self.auth_token:
            headers['Authorization'] = f"Bearer {self.auth_token}"

        logger.info(f"Выполнение поиска: {search_url}?query={query}")
        response = self.session.get(search_url, params=params, headers=headers)
        return self._check_response(response)