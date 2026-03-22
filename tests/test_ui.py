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
@pytest.mark.ui
@pytest.mark.parametrize("phrase, expected_results, test_type", [
    ("Горе от ума", lambda count: count > 0, "positive"),
    ("Harry Potter", lambda count: count > 0, "positive"),
    ("12 стульев", lambda count: count > 0, "positive"),
    ("@#$%^&*", lambda count: count == 0, "negative"),
    ("", lambda count: count == 0, "negative")
])
def test_search_books(main_page, phrase, expected_results, test_type):
    display_phrase = phrase if phrase else "ПУСТОЙ ЗАПРОС"

    with allure.step(f"Шаг 1: Закрытие всплывающих окон перед {test_type} поиском '{display_phrase}'"):
        main_page.close_popups()

    with allure.step(f"Шаг 2: Поиск книги по фразе '{display_phrase}'"):
        main_page.search_goods(phrase)

    with allure.step(f"Шаг 3: Проверка результатов для '{display_phrase}'"):
        results_count = main_page.get_search_results_count()
        assert expected_results(results_count), (
            f"Для запроса '{display_phrase}' найдено {results_count} результатов. "
            f"Ожидалось выполнение условия для {test_type} теста."
        )










# @allure.feature("Поиск книг")
# @allure.story("UI")
# @allure.title("Поиск книги на кириллице, латинице, название с цифрами")
# @pytest.mark.positive
# @pytest.mark.ui
# @pytest.mark.parametrize("phrase", [
#     "Горе от ума",
#     "Harry Potter",
#     "12 стульев"
# ])
# def test_search_book_by_title(main_page,phrase):
#     with allure.step("Закрытие всплывающих окон"):
#         main_page.close_popups()
#     with allure.step("Поиск книги по полному названию"):
#         main_page.search_goods(phrase)
#     with allure.step("Количество результатов больше 0"):
#         assert main_page.get_search_results_count() > 0

# @allure.feature("Поиск книг")
# @allure.story("UI")
# @allure.title("Поиск книги по случайному набору символов, пустой поиск")
# @pytest.mark.negative
# @pytest.mark.ui
# @pytest.mark.parametrize("phrase", [
#     "@#$%^&*",
#     ""

# ])
# def test_search_book_by_negative_title(main_page,phrase):
#     with allure.step("Закрытие всплывающих окон"):
#         main_page.close_popups()
#     with allure.step("Поиск книги по полному названию"):
#         main_page.search_goods(phrase)
#     with allure.step("Количество результатов больше 0"):
#         assert main_page.get_search_results_count() > 0