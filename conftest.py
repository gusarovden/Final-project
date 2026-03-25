import allure
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from config import MAIN_URL
from pages.api_page import ApiPage


@pytest.fixture
def main_page():
    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome()
        page = MainPage(driver, MAIN_URL)
        yield page

    with allure.step("Закрыть браузер"):    
        driver.quit()


@pytest.fixture
def api_page():
    with allure.step("Инициализация API‑страницы"):
        api = ApiPage()
        return api