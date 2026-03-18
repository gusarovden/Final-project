from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from selenium.webdriver.remote.webelement import WebElement

class SearchPage:
    """PageObject для страницы поиска в интернет‑магазине."""
    
    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[name="text"], input[placeholder*="Поиск"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"], .search__button')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.search-result-item, .result-card')
    LOCATION_POPUP = (By.CSS_SELECTOR, '.tippy-box[data-theme="location"]')
    POPUP_YES_BUTTON = (By.CSS_SELECTOR, '.chg-app-button--primary')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_main_page(self) -> None:
        """Открывает главную страницу сайта."""
        self.driver.get(self.base_url)
    
    def close_location_popup(self) -> bool:
        """Закрывает плашку выбора местоположения."""
        try:
            popup = self.wait.until(
                EC.presence_of_element_located(self.LOCATION_POPUP)
            )
            if popup.is_displayed():
                yes_button = self.driver.find_element(*self.POPUP_YES_BUTTON)
                yes_button.click()
                self.wait.until(
                    EC.invisibility_of_element_located(self.LOCATION_POPUP)
        )
                return True
        except:
            return False
    
    def enter_search_query(self, query: str) -> None:
        """Вводит поисковый запрос в поле ввода."""
        search_input = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(query)
    
    def click_search_button(self) -> None:
        """Нажимает кнопку поиска."""
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
    
    def get_search_results(self) -> List[WebElement]:
        """Возвращает элементы с результатами поиска."""
        return self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS))
    
    def is_results_displayed(self) -> bool:
        """Проверяет, отображаются ли результаты поиска."""
        try:
            results = self.get_search_results()
            return len(results) > 0
        except:
            return False








# from .base_page import BasePage
# from selenium.webdriver.common.by import By
# import allure

# class SearchPage(BasePage):
#     SEARCH_INPUT = (By.CSS_SELECTOR, '#app-search')
#     SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-form__icon-search')
#     RESULTS_COUNT = (By.CSS_SELECTOR, '.filter-search-categories-item__label')
#     NO_RESULTS = (By.CSS_SELECTOR, '.search-not-found__image')
#     LOADING_SPINNER = (By.CSS_SELECTOR, '.flockapi-spinner')

#     @allure.step('Открытие главной страницы: {url}')
#     def open_main_page(self, url: str):
#         """Открывает главную страницу сайта.

#         Args:
#             url (str): URL для открытия
#         """
#         self.driver.get(url)

#     @allure.step('Ввод поискового запроса: "{search_term}"')
#     def search(self, search_term: str):
#         """Выполняет поиск по указанному запросу.

#         Args:
#             search_term (str): поисковый запрос
#         """
#         input_field = self.find_element(self.SEARCH_INPUT)
#         input_field.clear()
#         input_field.send_keys(search_term)

#         button = self.find_element(self.SEARCH_BUTTON)
#         button.click()

#     @allure.step('Получение количества результатов поиска')
#     def get_results_count(self) -> int:
#         """Возвращает количество найденных результатов.

#         Returns:
#             int: количество найденных товаров
#         """
#         if self.is_element_visible(self.NO_RESULTS):
#             return 0

#         if not self.is_element_visible(self.RESULTS_COUNT, timeout=5):
#             return -1  # Элемент не найден

#         element = self.find_element(self.RESULTS_COUNT)
#         text = element.text
#         import re
#         numbers = re.findall(r'\d+', text)
#         return int(numbers[0]) if numbers else 0

#     @allure.step('Проверка наличия сообщения "Ничего не найдено"')
#     def is_no_results_displayed(self) -> bool:
#         """Проверяет, отображается ли сообщение об отсутствии результатов.

#         Returns:
#             bool: True если сообщение видно, False в противном случае
#         """
#         return self.is_element_visible(self.NO_RESULTS)






















