from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """
    Класс страницы калькулятора
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/"
                         "selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def input_delay(self):
        """
        Установка времени задержки 45 секунд
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def input_keys(self):
        """
        Ввод слагаемых и вычисление результата
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_delay(self):
        """
        Ожидание прохождения таймаута
        """
        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
            )

    def wait_result(self):
        """
        Явное ожидание появления результата
        """
        WebDriverWait(self._driver, 60).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
            ))

    def res(self) -> str:
        """
        Возврат результата вычисления
        """
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
