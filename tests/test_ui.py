import pytest
import allure


@allure.feature("Поиск книг")
@allure.story("UI")
@pytest.mark.ui
@pytest.mark.parametrize("phrase, expected_results", [
    ("Горе от ума", lambda count: count > 0 ),
    ("Harry Potter", lambda count: count > 0 ),
    ("2012", lambda count: count > 0 ),
    (" Python", lambda count: count > 0 ),
    ("_Python", lambda count: count > 0 )
])


def test_search_books(main_page, phrase, expected_results):
    display_phrase = phrase if phrase else "ПУСТОЙ ЗАПРОС"

    with allure.step(f"Шаг 0: Диагностика начальной страницы"):
        print(f"DEBUG: Текущий URL: {main_page.driver.current_url}")
        print(f"DEBUG: Заголовок страницы: {main_page.driver.title}")

    with allure.step(f"Шаг 1: Закрытие всплывающих окон перед поиском '{display_phrase}'"):
        main_page.close_popups()

    with allure.step(f"Шаг 2: Поиск книги по фразе '{display_phrase}'"):
        try:
            main_page.search_goods(phrase)
            print(f"DEBUG: URL после поиска: {main_page.driver.current_url}")
            print(f"DEBUG: Заголовок после поиска: {main_page.driver.title}")

        except Exception as e:
            allure.attach(
                main_page.driver.get_screenshot_as_png(),
                f"Скриншот ошибки на шаге поиска '{display_phrase}'",
                allure.attachment_type.PNG
            )
            raise e

    with allure.step(f"Шаг 3: Проверка результатов для '{display_phrase}'"):
        try:
            results_count = main_page.get_search_results_count()
            print(f"DEBUG: Найдено результатов: {results_count}")
            assert expected_results(results_count), (
                f"Для запроса '{display_phrase}' найдено {results_count} результатов. "
                f"Ожидалось, что количество > 0."
            )
        except AssertionError:
            allure.attach(
                main_page.driver.get_screenshot_as_png(),
                f"Скриншот при ошибке проверки результатов для '{display_phrase}'",
                allure.attachment_type.PNG
            )
            raise




