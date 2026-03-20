import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from config import MAIN_URL


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    page = MainPage(driver, MAIN_URL)
    yield page
    driver.quit()

@allure.feature("Поиск книг")
@allure.story("UI")
@allure.title("Поиск книги на кириллице, латинице, название с цифрами")
@pytest.mark.positive
@pytest.mark.ui
@pytest.mark.parametrize("phrase", [
    "Горе от ума",
    "Harry Potter",
    "12 стульев"
])
def test_search_book_by_title(main_page,phrase):
    with allure.step("Закрытие всплывающих окон"):
        main_page.close_popups()
    with allure.step("Поиск книги по полному названию"):
        main_page.search_goods(phrase)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0

@allure.feature("Поиск книг")
@allure.story("UI")
@allure.title("Поиск книги по случайному набору символов, пустой поиск")
@pytest.mark.negative
@pytest.mark.ui
@pytest.mark.parametrize("phrase", [
    "@#$%^&*",
    ""

])
def test_search_book_by_negative_title(main_page,phrase):
    with allure.step("Закрытие всплывающих окон"):
        main_page.close_popups()
    with allure.step("Поиск книги по полному названию"):
        main_page.search_goods(phrase)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0



