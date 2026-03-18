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

