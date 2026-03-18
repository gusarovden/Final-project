import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Загружаем переменные из .env-файла, если он существует
load_dotenv()

# Настройки окружения
BASE_URL = os.environ.get('BASE_URL', 'https://www.chitai-gorod.ru')
API_URL = os.environ.get('API_URL', 'https://web-agr.chitai-gorod.ru/web/api/v1') 
BROWSER = os.environ.get('BROWSER', 'chrome')
HEADLESS = os.environ.get('HEADLESS', 'false').lower() == 'true'
COOKIE_DOMAIN = os.environ.get('COOKIE_DOMAIN', '.chitai-gorod.ru')

# Данные для авторизации по телефону (заменяем email/password)
AUTH_DATA = {
    'phone': os.environ.get('PHONE_NUMBER', '+79009368472'),
    'sms_code': os.environ.get('SMS_CODE', '1234')
}

# Валидация обязательных переменных
def validate_settings():
    """Проверяет наличие обязательных переменных окружения."""
    required_vars = ['PHONE_NUMBER', 'API_URL']
    missing_vars = []

    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)

    if missing_vars:
        error_msg = f"Не заданы обязательные переменные окружения: {', '.join(missing_vars)}"
        logger.error(error_msg)
        raise ValueError(error_msg)

# Выполняем валидацию при импорте модуля
try:
    validate_settings()
    logger.info("Настройки успешно загружены и проверены")
except ValueError as e:
    logger.critical(f"Критическая ошибка при загрузке настроек: {e}")
    raise