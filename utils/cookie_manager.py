import os
from selenium.webdriver.remote.webdriver import WebDriver


class CookieManager:
    @staticmethod
    def add_auth_cookie(driver: WebDriver, auth_token: str, domain: str = '.chitai-gorod.ru') -> None:
        """Добавляет cookie авторизации в браузер."""
        domain = os.getenv('COOKIE_DOMAIN', '.chitai-gorod.ru')
        driver.add_cookie({
            'name': 'auth_token',
            'value': auth_token,
            'domain': domain,
            'path': '/'
        })





# class CookieManager:
#     """Менеджер для работы с куки браузера."""
    
#     @staticmethod
#     def add_auth_cookie(driver, token: str) -> None:
#         """Добавляет куки авторизации в браузер."""
#         driver.add_cookie({
#             'name': 'auth_token',
#             'value': token,
#             'domain': settings.BASE_URL.replace('https://', ''),
#             'path': '/'
#         })
#         driver.refresh()