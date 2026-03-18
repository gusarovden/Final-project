import pytest
import os
from dotenv import load_dotenv
import requests
from selenium import webdriver
from utils.api_client import APIClient
from utils.cookie_manager import CookieManager
from pages.search_page import SearchPage
import logging

# Загружаем переменные из .env-файла
load_dotenv()

# Настройки загружаем через os.environ.get()
BASE_URL = os.environ.get('BASE_URL', 'https://www.chitai-gorod.ru')
API_URL = os.environ.get('API_URL', 'https://web-agr.chitai-gorod.ru/web/api/v1')
COOKIE_DOMAIN = os.environ.get('COOKIE_DOMAIN', '.chitai-gorod.ru')
HEADLESS = os.environ.get('HEADLESS', 'false').lower() == 'true'

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_execution.log', encoding='utf-8'),
        logging.StreamHandler()  # Вывод в консоль
    ]
)
logger = logging.getLogger(__name__)

def validate_required_env_vars():
    """Проверяет наличие обязательных переменных окружения."""
    required_vars = ['PHONE_NUMBER', 'API_URL']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    if missing_vars:
        error_msg = f"Не заданы обязательные переменные окружения: {', '.join(missing_vars)}"
        logger.critical(error_msg)
        raise ValueError(error_msg)

# Выполняем валидацию при импорте модуля
validate_required_env_vars()

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API‑клиента."""
    logger.info("Инициализация API-клиента...")
    client = APIClient()
    logger.info(f"API-клиент успешно создан. Базовый URL: {client.base_url}")
    return client

@pytest.fixture(scope="session")
def auth_token(api_client):
    """Фикстура для получения токена авторизации по телефону."""
    logger.info("=== НАЧАЛО ПОЛУЧЕНИЯ ТОКЕНА АВТОРИЗАЦИИ ===")

    # Проверяем наличие обязательных переменных окружения
    phone = os.environ.get('PHONE_NUMBER')
    if not phone:
        logger.error("Переменная окружения PHONE_NUMBER не задана!")
        raise ValueError("PHONE_NUMBER не задан в окружении")

    sms_code = os.environ.get('SMS_CODE', '1234')
    logger.info(f"Используем номер телефона: {phone}")
    logger.info(f"Используем SMS-код: {sms_code}")

    try:
        # Отправляем запрос на получение SMS-кода
        logger.info("Отправка запроса на получение SMS-кода...")
        sms_response = api_client.send_sms_code(phone)

        if sms_response.status_code != 200:
            logger.error(f"Ошибка отправки SMS-кода: {sms_response.text}")
            raise Exception("Ошибка отправки SMS-кода")

        logger.info("SMS-код успешно отправлен, выполняем авторизацию...")

        # Выполняем авторизацию
        auth_response = api_client.login_by_phone(phone, sms_code)

        if auth_response.status_code != 200:
            logger.error(f"Ошибка авторизации: {auth_response.text}")
            raise ValueError("Не удалось получить токен авторизации")

        token = auth_response.json().get('token')

        # Проверяем, что токен получен и не пустой
        if not token:
            logger.error("Токен получен, но он пустой!")
            raise ValueError("Пустой токен авторизации")

        logger.info(f"Токен успешно получен: {token[:15]}...")
        return token

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP ошибка при авторизации: {e}")
        if e.response:
            logger.error(f"Статус код: {e.response.status_code}")
            logger.error(f"Тело ответа: {e.response.text}")
        raise

    except Exception as e:
        logger.error(f"Неожиданная ошибка при получении токена: {e}")
        raise

@pytest.fixture
def driver():
    """Фикстура для управления браузером."""
    logger.info("Запуск браузера...")
    options = webdriver.ChromeOptions()
    headless_mode = os.environ.get('HEADLESS', 'false').lower() == 'true'
    if headless_mode:
        options.add_argument('--headless')
        logger.info("Режим headless включён")

    driver = webdriver.Chrome(options=options)
    logger.info("Браузер успешно запущен")
    yield driver
    logger.info("Закрытие браузера...")
    driver.quit()
    logger.info("Браузер закрыт")

@pytest.fixture
def search_page(driver, auth_token):
    """Фикстура для инициализации страницы поиска с авторизацией."""
    logger.info("Создание экземпляра SearchPage...")
    page = SearchPage(driver)

    if auth_token:
        logger.info("Добавление cookie авторизации...")
        CookieManager.add_auth_cookie(driver, auth_token)
    else:
        logger.warning("Токен авторизации не получен, пропускаем добавление cookie")

    logger.info("Открытие главной страницы...")
    page.open_main_page()
    logger.info("SearchPage успешно инициализирован")
    return page