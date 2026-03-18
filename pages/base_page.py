# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# class BasePage:
#     def __init__(self, driver: WebDriver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 15)

#     def find_element(self, locator):
#         """Находит элемент по локатору.

#         Args:
#             locator (tuple): кортеж с типом локатора и значением (By.CSS_SELECTOR, '.class')

#         Returns:
#             WebElement: найденный элемент
#         """
#         return self.wait.until(EC.presence_of_element_located(locator))

#     def is_element_visible(self, locator, timeout=10):
#         """Проверяет видимость элемента.

#         Args:
#             locator (tuple): локатор элемента
#             timeout (int): таймаут ожидания

#         Returns:
#             bool: True если элемент виден, False в противном случае
#         """
#         try:
#             self.wait = WebDriverWait(self.driver, timeout)
#             return EC.visibility_of_element_located(locator)(self.driver)
#         except TimeoutException:
#             return False