import pytest
from config.test_data import SEARCH_DATA

class TestSearchUIFunctionality:

    """Тесты поиска на сайте интернет‑магазина."""
    @pytest.mark.ui
    def test_search_cyrillic(self, search_page):
        """Поиск по названию на кириллице."""
        search_page.enter_search_query(SEARCH_DATA['cyrillic'])
        search_page.click_search_button()
        results = search_page.get_search_results()
        assert len(results) > 0, "Не найдены результаты для кириллического запроса"

    @pytest.mark.ui
    def test_search_latin(self, search_page):
        """Поиск по названию на латинице."""
        search_page.enter_search_query(SEARCH_DATA['latin'])
        search_page.click_search_button()
        results = search_page.get_search_results()
        assert len(results) > 0, "Не найдены результаты для латинского запроса"

    @pytest.mark.ui
    def test_search_with_numbers(self, search_page):
        """Поиск по названию с цифрами."""
        search_page.enter_search_query(SEARCH_DATA['with_numbers'])
        search_page.click_search_button()
        results = search_page.get_search_results()
        assert len(results) > 0, "Не найдены результаты для запроса с цифрами"

    @pytest.mark.ui
    def test_search_special_chars(self, search_page):
        """Поиск по произвольному набору символов."""
        search_page.enter_search_query(SEARCH_DATA['special_chars'])
        search_page.click_search_button()
        # Для спецсимволов может не быть результатов — проверяем корректность обработки
        try:
            results = search_page.get_search_results()
            assert True  # Запрос обработан без ошибок
        except Exception as e:
            pytest.fail(f"Ошибка при поиске со спецсимволами: {e}")

    @pytest.mark.ui
    def test_empty_search(self, search_page):
        """Пустой поиск."""
        search_page.enter_search_query(SEARCH_DATA['empty'])
        search_page.click_search_button()
        # Проверяем, что нет фатальной ошибки
        assert search_page.is_results_displayed() is False, "Пустой запрос не должен возвращать результаты"



















# import os
# import pytest
# from selenium import webdriver
# from pages.search_page import SearchPage
# from config.test_data import SEARCH_TERMS
# import allure

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     if os.getenv('HEADLESS', 'false').lower() == 'true':
#         options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

# class TestUISearch:
#     @allure.feature('UI')
#     @allure.story('Поиск по названию на кириллице')
#     def test_search_cyrillic(self, driver):
#         page = SearchPage(driver)
#         driver.get('https://www.chitai-gorod.ru')
#         page.search(SEARCH_TERMS['cyrillic'])
#         assert page.get_results_count() > 0

#     @allure.feature('UI')
#     @allure.story('Поиск по названию на латинице')
#     def test_search_latin(self, driver):
#         page = SearchPage(driver)
#         driver.get('https://www.chitai-gorod.ru')
#         page.search(SEARCH_TERMS['latin'])
#         assert page.get_results_count() > 0

#     @allure.feature('UI')
#     @allure.story('Поиск по названию с цифрами')
#     def test_search_with_numbers(self, driver):
#         page = SearchPage(driver)
#         driver.get('https://www.chitai-gorod.ru')
#         page.search(SEARCH_TERMS['with_numbers'])
#         assert page.get_results_count() >= 0  # Может быть 0 результатов

#     @allure.feature('UI')
#     @allure.story('Поиск по произвольному набору символов')
#     def test_search_special_chars(self, driver):
#         page = SearchPage(driver)
#         driver.get('https://www.chitai-gorod.ru')
#         page.search(SEARCH_TERMS['special_chars'])